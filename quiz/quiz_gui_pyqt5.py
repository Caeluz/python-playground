import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QPushButton, QVBoxLayout, QRadioButton, QButtonGroup, QMessageBox
from quiz_data import quiz_data  # Assuming you have quiz data in a separate file

# Function to shuffle questions within each section


def shuffle_questions(data):
    for section in data:
        random.shuffle(section["questions"])
        for question in section["questions"]:
            random.shuffle(question["options"])


# Shuffle the order of questions and sections
shuffle_questions(quiz_data)

# Create a list of sections in the order they appear in quiz_data
sections_order = [section["section"] for section in quiz_data]


class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.current_section = None
        self.current_question_index = 0
        self.sections_to_test = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Quiz App")

        layout = QVBoxLayout()

        self.section_label = QLabel("Sections:")
        layout.addWidget(self.section_label)

        self.section_listbox = QListWidget()
        for i, section in enumerate(sections_order, start=1):
            self.section_listbox.addItem(f"{i}. {section}")
        self.section_listbox.addItem("0. Test All Sections")
        layout.addWidget(self.section_listbox)

        self.start_button = QPushButton("Start Quiz")
        self.start_button.clicked.connect(self.start_quiz)
        layout.addWidget(self.start_button)

        self.question_label = QLabel("")
        layout.addWidget(self.question_label)

        self.options_group = QButtonGroup(self)
        self.option_buttons = []
        for i in range(4):
            btn = QRadioButton("")
            self.options_group.addButton(btn)
            layout.addWidget(btn)
            self.option_buttons.append(btn)

        self.submit_button = QPushButton("Submit Answer")
        self.submit_button.clicked.connect(self.submit_answer)
        layout.addWidget(self.submit_button)

        self.score_label = QLabel("")
        layout.addWidget(self.score_label)

        self.setLayout(layout)

    def start_quiz(self):
        user_choice = self.section_listbox.currentRow()
        if user_choice == -1:
            QMessageBox.critical(self, "Error", "Please select a section.")
            return

        if user_choice == len(sections_order):
            self.sections_to_test = quiz_data  # Test all sections
        else:
            section_name = sections_order[user_choice]
            self.sections_to_test = [
                section for section in quiz_data if section["section"] == section_name]

        self.score = 0
        self.current_question_index = 0
        self.show_question()

    def show_question(self):
        if self.current_question_index < len(self.sections_to_test[0]["questions"]):
            question = self.sections_to_test[0]["questions"][self.current_question_index]
            self.question_label.setText(
                f"{self.current_question_index + 1}. {question['question']}")
            for i, option in enumerate(question["options"]):
                self.option_buttons[i].setText(option)
                self.option_buttons[i].setChecked(False)
        else:
            self.show_score()

    def submit_answer(self):
        selected_button = self.options_group.checkedButton()
        if not selected_button:
            QMessageBox.critical(self, "Error", "Please select an answer.")
            return

        question = self.sections_to_test[0]["questions"][self.current_question_index]
        user_answer = selected_button.text()
        if user_answer == question["correct_answer"]:
            self.score += 1

        self.current_question_index += 1
        self.show_question()

    def show_score(self):
        self.question_label.setText("")
        for btn in self.option_buttons:
            btn.setText("")
        self.score_label.setText(
            f"Your final score is: {self.score}/{len(self.sections_to_test[0]['questions'])}")
        self.submit_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    quiz_app = QuizApp()
    quiz_app.show()
    sys.exit(app.exec_())
