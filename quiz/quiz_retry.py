# Assuming you have quiz data in a separate file
from quiz_data import quiz_data
import random

# Function to shuffle questions within each section


def shuffle_questions(data):
    for section in data:
        # Shuffle the questions within each section
        random.shuffle(section["questions"])
        for question in section["questions"]:
            # Shuffle the options within each question
            random.shuffle(question["options"])


# Shuffle the order of questions and sections
# random.shuffle(quiz_data)
shuffle_questions(quiz_data)

# Create a list of sections in the order they appear in quiz_data
sections_order = [section["section"] for section in quiz_data]

# Quiz loop
while True:
    score = 0  # Reset the score for each section
    wrong_questions = []  # Keep track of wrong questions

    print("Sections:")
    for i, section in enumerate(sections_order, start=1):
        print(f"{i}. {section}")
    print("0. Test All Sections")

    user_choice = input("Choose a section to test (enter the number): ")

    if user_choice.isdigit():
        user_choice = int(user_choice)
        if 0 <= user_choice <= len(sections_order):
            if user_choice == 0:
                sections_to_test = quiz_data  # Test all sections
            else:
                section_name = sections_order[user_choice - 1]
                # Test a specific section
                sections_to_test = [
                    section for section in quiz_data if section["section"] == section_name]
        else:
            print(
                "Invalid section number. Please choose a valid section or 0 for all sections.")
            continue
    else:
        print("Invalid input. Please enter a valid number.")
        continue

    for section in sections_to_test:
        section_name = section['section']
        print(f"Testing Section: {section_name}\n")

        question_number = 0  # Initialize the question number
        print("q. Quit this section\n")

        for question in section["questions"]:
            question_number += 1  # Increment the question number
            # Display the question number and question with a new line
            print(f"{question_number}. {question['question']}\n")
            for i, option in enumerate(question["options"], start=1):
                print(f"{i}. {option}")

            while True:
                user_answer = input(
                    f"Your choice for question {question_number} (enter the option number): ")

                if user_answer == 'q' or user_answer == 'Q':
                    break  # Quit this section and return to section selection menu
                elif user_answer.isdigit():
                    user_answer = int(user_answer)
                    if 1 <= user_answer <= len(question["options"]):
                        break  # Valid input, exit the loop
                    else:
                        print(
                            "Not on the options. Please enter a number within the valid range.")
                else:
                    print(
                        "Invalid input. Please enter a number or 'q' to quit this section.")

            if user_answer == 'q' or user_answer == 'Q':
                break  # Quit this section and return to section selection menu

            if question["options"][user_answer - 1] == question["correct_answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(
                    f"Wrong! The correct answer is: {question['correct_answer']}\n {question['explanation']}")
                # Add wrong question to the list
                wrong_questions.append(question)

    if user_answer == 'q' or user_answer == 'Q':
        continue  # Return to section selection menu

    section_total_questions = len(section["questions"])
    section_score = score
    section_percentage = (section_score / section_total_questions) * 100

    print(
        f"Your final score for this section is: {score}/{section_total_questions} ({section_percentage:.2f}%)")

    # Retry wrong questions
    if wrong_questions:
        print("\nRetry the wrong questions:\n")
        for question in wrong_questions:
            print(question["question"])
            for i, option in enumerate(question["options"], start=1):
                print(f"{i}. {option}")

            while True:
                user_answer = input(
                    "Your choice (enter the option number): ")

                if user_answer.isdigit():
                    user_answer = int(user_answer)
                    if 1 <= user_answer <= len(question["options"]):
                        break  # Valid input, exit the loop
                    else:
                        print(
                            "Not on the options. Please enter a number within the valid range.")
                else:
                    print("Invalid input. Please enter a number only.")

            if question["options"][user_answer - 1] == question["correct_answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(
                    f"Wrong! The correct answer is: {question['correct_answer']}\n {question['explanation']}")

    print(
        f"Your final score for this section is: {score}/{section_total_questions} ({section_percentage:.2f}%)")

    play_again = input(
        "Do you want to try another section? (1 or 0): ").lower()
    if play_again != '1':
        break
