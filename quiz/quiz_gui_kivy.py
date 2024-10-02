import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.togglebutton import ToggleButtonBehavior
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty, ObjectProperty
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


class QuizApp(App):
    def build(self):
        self.score = 0
        self.current_section = None
        self.current_question_index = 0
        self.sections_to_test = []

        self.root = BoxLayout(orientation='vertical')

        self.section_label = Label(text="Sections:")
        self.root.add_widget(self.section_label)

        self.section_listbox = GridLayout(cols=1, size_hint_y=None)
        self.section_listbox.bind(
            minimum_height=self.section_listbox.setter('height'))

        for i, section in enumerate(sections_order, start=1):
            btn = ToggleButton(text=f"{i}. {section}", group='sections')
            btn.bind(on_press=self.on_section_select)
            self.section_listbox.add_widget(btn)
        btn = ToggleButton(text="0. Test All Sections", group='sections')
        btn.bind(on_press=self.on_section_select)
        self.section_listbox.add_widget(btn)

        scrollview = ScrollView(size_hint=(
            1, None), size=(self.root.width, 200))
        scrollview.add_widget(self.section_listbox)
        self.root.add_widget(scrollview)

        self.start_button = Button(text="Start Quiz")
        self.start_button.bind(on_press=self.start_quiz)
        self.root.add_widget(self.start_button)

        self.question_label = Label(text="")
        self.root.add_widget(self.question_label)

        self.options_group = BoxLayout(orientation='vertical')
        self.option_buttons = []
        for i in range(4):
            btn = ToggleButton(group='options')
            self.options_group.add_widget(btn)
            self.option_buttons.append(btn)
        self.root.add_widget(self.options_group)

        self.submit_button = Button(text="Submit Answer")
        self.submit_button.bind(on_press=self.submit_answer)
        self.root.add_widget(self.submit_button)

        self.score_label = Label(text="")
        self.root.add_widget(self.score_label)

        return self.root

    def on_section_select(self, instance):
        self.selected_section = instance.text

    def start_quiz(self, instance):
        if not hasattr(self, 'selected_section'):
            popup = Popup(title='Error', content=Label(
                text='Please select a section.'), size_hint=(None, None), size=(400, 200))
            popup.open()
            return

        user_choice = self.selected_section.split(".")[0]
        if user_choice == "0":
            self.sections_to_test = quiz_data  # Test all sections
        else:
            section_name = sections_order[int(user_choice) - 1]
            self.sections_to_test = [
                section for section in quiz_data if section["section"] == section_name]

        self.score = 0
        self.current_question_index = 0
        self.show_question()

    def show_question(self):
        if self.current_question_index < len(self.sections_to_test[0]["questions"]):
            question = self.sections_to_test[0]["questions"][self.current_question_index]
            self.question_label.text = f"{self.current_question_index + 1}. {question['question']}"
            for i, option in enumerate(question["options"]):
                self.option_buttons[i].text = option
                self.option_buttons[i].state = 'normal'
        else:
            self.show_score()

    def submit_answer(self, instance):
        selected_button = next(
            (btn for btn in self.option_buttons if btn.state == 'down'), None)
        if not selected_button:
            popup = Popup(title='Error', content=Label(
                text='Please select an answer.'), size_hint=(None, None), size=(400, 200))
            popup.open()
            return

        question = self.sections_to_test[0]["questions"][self.current_question_index]
        user_answer = selected_button.text
        if user_answer == question["correct_answer"]:
            self.score += 1

        self.current_question_index += 1
        self.show_question()

    def show_score(self):
        self.question_label.text = ""
        for btn in self.option_buttons:
            btn.text = ""
        self.score_label.text = f"Your final score is: {self.score}/{len(self.sections_to_test[0]['questions'])}"
        self.submit_button.disabled = True


if __name__ == "__main__":
    QuizApp().run()
