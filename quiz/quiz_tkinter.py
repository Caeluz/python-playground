import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from quiz_data import quiz_data  # Assuming you have quiz data in a separate file
import random

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


class QuizApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Quiz App")
        self.style = ttk.Style(self)
        self.style.theme_use("clam")  # Use a modern theme
        self.score = 0
        self.current_section = None
        self.current_question_index = 0
        self.sections_to_test = []

        # Set window size and disable resizing
        self.geometry("500x1000")
        # self.resizable(False, False)

        self.initUI()

    def initUI(self):
        self.section_label = ttk.Label(
            self, text="Sections:", font=("Helvetica", 16))
        self.section_label.pack(pady=10, fill='x')

        self.section_listbox = tk.Listbox(self, font=("Helvetica", 12))
        for i, section in enumerate(sections_order, start=1):
            self.section_listbox.insert(tk.END, f"{i}. {section}")
        self.section_listbox.insert(tk.END, "0. Test All Sections")
        self.section_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        # Add a scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.section_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.section_listbox.yview)

        self.start_button = ttk.Button(
            self, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack(pady=10)

        self.question_label = ttk.Label(
            self, text="", font=("Helvetica", 14), wraplength=450)
        self.question_label.pack(pady=10, fill=tk.BOTH, expand=True)

        self.options_var = tk.StringVar()
        self.options_frame = ttk.Frame(self)
        self.options_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.feedback_label = ttk.Label(
            self, text="", font=("Helvetica", 12), wraplength=450)
        self.feedback_label.pack(pady=10, fill=tk.BOTH, expand=True)

        self.option_buttons = []
        for i in range(4):
            btn = ttk.Radiobutton(
                self.options_frame, text="", variable=self.options_var, value=i+1)
            btn.pack(anchor=tk.W, pady=5, fill=tk.BOTH, expand=True)
            self.option_buttons.append(btn)


        # Create a frame to hold the buttons
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=10, fill=tk.X, expand=True)

        # Create the Submit Answer button and pack it to the left
        self.submit_button = ttk.Button(
            self.button_frame, text="Submit Answer", command=self.submit_answer)
        self.submit_button.pack(side=tk.LEFT, padx=10, fill=tk.Y, expand=True)

        # Create the Next Question button, initially disabled, and pack it to the right
        self.next_button = ttk.Button(
            self.button_frame, text="Next Question", command=self.show_next_question, state=tk.DISABLED)
        self.next_button.pack(side=tk.RIGHT, padx=10, fill=tk.Y, expand=True)

        self.score_label = ttk.Label(self, text="", font=("Helvetica", 14))
        self.score_label.pack(pady=10, fill=tk.Y, expand=True)

    def start_quiz(self):
        user_choice = self.section_listbox.curselection()
        if not user_choice:
            messagebox.showerror("Error", "Please select a section.")
            return

        user_choice = user_choice[0]
        if user_choice == len(sections_order):
            self.sections_to_test = quiz_data  # Test all sections
        else:
            section_name = sections_order[user_choice]
            self.sections_to_test = [
                section for section in quiz_data if section["section"] == section_name]

        self.score = 0
        self.current_question_index = 0
        self.show_question()

    # def show_question(self):
    #     if self.current_question_index < len(self.sections_to_test[0]["questions"]):
    #         question = self.sections_to_test[0]["questions"][self.current_question_index]
    #         self.question_label.config(
    #             text=f"{self.current_question_index + 1}. {question['question']}")
    #         for i, option in enumerate(question["options"]):
    #             self.option_buttons[i].config(text=option)
    #         self.options_var.set("")
    #         self.feedback_label.config(text="")  # Clear the feedback label
    #     else:
    #         self.show_score()

    def submit_answer(self):
        if not self.options_var.get():
            messagebox.showerror("Error", "Please select an answer.")
            return

        question = self.sections_to_test[0]["questions"][self.current_question_index]
        user_answer = int(self.options_var.get())
        if question["options"][user_answer - 1] == question["correct_answer"]:
            self.score += 1
            self.feedback_label.config(text="Correct!", foreground="green")
        else:
            self.feedback_label.config(
                text=f"Wrong! The correct answer is: {question['correct_answer']}\n"
                f"Your answer: {question['options'][user_answer - 1]}\n"
                f"Explanation: {question['explanation']}",
                foreground="red"
            )

        # Disable the Submit button after submission
        self.submit_button.config(state=tk.DISABLED)

        # Enable the Next Question button
        self.next_button.config(state=tk.NORMAL)

    def show_next_question(self):
        # Reset feedback and buttons for the next question
        self.current_question_index += 1
        self.show_question()

        # Disable Next Question button and re-enable Submit button
        self.next_button.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.NORMAL)

    def show_score(self):
        self.question_label.config(text="")
        for btn in self.option_buttons:
            btn.config(text="")
        self.score_label.config(
            text=f"Your final score is: {self.score}/{len(self.sections_to_test[0]['questions'])}")
        self.submit_button.config(state=tk.DISABLED)

    def show_question(self):
        if self.current_question_index < len(self.sections_to_test[0]["questions"]):
            question = self.sections_to_test[0]["questions"][self.current_question_index]
            self.question_label.config(
                text=f"{self.current_question_index + 1}. {question['question']}")
            for i, option in enumerate(question["options"]):
                self.option_buttons[i].config(text=option)
            self.options_var.set("")
            # Clear feedback for the new question
            self.feedback_label.config(text="")
        else:
            self.show_score()


if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
