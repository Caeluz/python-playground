import random
import time
# pip install pandas
import pandas as pd
import os

# Get the directory of the script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the leaderboard.csv file
leaderboard_file = os.path.join(script_directory, "leaderboard.csv")


leaderboard_file = "find_missing_numbers/leaderboard.csv"

def load_leaderboard():
    if os.path.isfile(leaderboard_file):
        leaderboard = pd.read_csv(leaderboard_file)
    elif (FileNotFoundError):
        leaderboard = pd.DataFrame(columns=["Username", "Difficulty", "Time", "Numbers_Missing", "Numbers_Array", "Mistake_Count"])
    return leaderboard


def display_leaderboard(leaderboard, username):
    # Sort the leaderboard by Difficulty and Time
    sorted_leaderboard = leaderboard.sort_values(by=["Difficulty", "Time"])

    # Display only the top 10 entries
    top_10_leaderboard = sorted_leaderboard.head(10)
    print("\nTop 10 Leaderboard:")
    print(top_10_leaderboard)

    # Show the current user's position
    sorted_leaderboard.to_csv(leaderboard_file, index=False) 
    user_position = sorted_leaderboard[sorted_leaderboard['Username'] == username].index.item() + 1
    # print(f"\nYour Position, {username}: #{user_position}")

def difficulty_level():
    while True:
        try:
            difficulty = int(input("Difficulty level (1-3): "))
            if difficulty < 1 or difficulty > 3:
                print("Invalid input. Please enter a valid integer.")
                continue
            else:
                array_length = 10 * difficulty
                num_arr = random.sample(range(0, array_length), array_length)
                random_num_arr = random.sample(num_arr, random.randint(1, len(num_arr) - 1))
                # random_num_arr = [0, 1, 2, 3, 4, 5, 6, 7,]
                return num_arr, random_num_arr, difficulty
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue


def add_missing_num():
    num_arr, random_num_arr, difficulty = difficulty_level()

    numbers_missing_len = len(num_arr) - len(random_num_arr)
    numbers_array_len = len(num_arr)
    # Ensure leaderboard is loaded, but no need to save it separately
    leaderboard = load_leaderboard() 
    
    # Time penalty for entering a duplicate number
    penalty_time = 0.0
    
    # Penalty time for each mistake (entering a duplicate number)
    mistake_count = 0
    
    # Start the timer when missing numbers input shows up on screen
    start_time = time.time()  

    while len(random_num_arr) < len(num_arr):
        while True:
            try:
                print(random_num_arr)
                missing_nums_input = input("Missing numbers (separated by commas or spaces): ")
                missing_nums = [int(num.strip()) for num in missing_nums_input.replace(',', ' ').split()]
                break
            except ValueError:
                print("Invalid input. Please enter valid integers separated by commas or spaces.")
                continue

        for missing_num in missing_nums:
            if missing_num in random_num_arr:
                penalty_time += 2.0
                mistake_count += 1
                print(f"Number {missing_num} already in array. Time penalty of {penalty_time} seconds added.")
            elif missing_num not in num_arr:
                print(f"Number {missing_num} not in array. Try again.")
            else:
                random_num_arr.append(missing_num)

        # Sort the array after each addition
        # random_num_arr.sort()  

    end_time = time.time()
    elapsed_time = round(end_time - start_time + penalty_time, 2)

    print(f"You completed the array in {elapsed_time} seconds!")
    print("You have successfully added the missing number(s) to the array:", random_num_arr)

    while True:
        try:
            username = input("Enter your username: ")
            if not username:
                raise ValueError("Username cannot be empty.")
            elif username in leaderboard['Username'].values:
                raise ValueError("Username already exists. Please enter a different username.")
            break
        except ValueError as ve:
            print(f"Error: {ve}")
            
    new_leaderboard = pd.DataFrame({"Username": username, "Difficulty": difficulty, "Time": elapsed_time, "Numbers_Missing": numbers_missing_len, "Numbers_Array": numbers_array_len, "Mistake_count": mistake_count }, index=[0])
    new_leaderboard.to_csv(leaderboard_file, mode='a', header=False, index=False)

    leaderboard = load_leaderboard()
    display_leaderboard(leaderboard, username)


def main():
    while True:
        print("Input missing number from array")
        add_missing_num()
        
        play_again = input("Do you want to play again? (1/0): ")
        if play_again != '1':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
