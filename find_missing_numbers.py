import random
import time
# pip install pandas
import pandas as pd
import os

leaderboard_file = "leaderboard.csv"


def load_leaderboard():
    if os.path.isfile(leaderboard_file):
        leaderboard = pd.read_csv(leaderboard_file)
    elif (FileNotFoundError):
        leaderboard = pd.DataFrame(columns=["Username", "Time"])
    return leaderboard


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
                random_num_arr = random.sample(num_arr, random.randint(1, 9))
                # random_num_arr = [0, 1, 2, 3, 4, 5, 6, 7,]
                return num_arr, random_num_arr, difficulty
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue


def add_missing_num():
    num_arr, random_num_arr, difficulty = difficulty_level()

    print(difficulty)
    
    # Time penalty for entering a duplicate number
    penalty_time = 0.0
    
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
                print(f"Number {missing_num} already in array. Time penalty of {penalty_time} seconds added.")
            elif missing_num not in num_arr:
                print(f"Number {missing_num} not in array. Try again.")
            else:
                random_num_arr.append(missing_num)

        # Sort the array after each addition
        random_num_arr.sort()  

    end_time = time.time()
    elapsed_time = round(end_time - start_time + penalty_time, 2)

    print(f"You completed the array in {elapsed_time} seconds!")
    print("You have successfully added the missing number(s) to the array:", random_num_arr)

    while True:
        try:
            username = input("Enter your username: ")
            if not username:
                raise ValueError("Username cannot be empty.")
            break
        except ValueError as ve:
            print(f"Error: {ve}")
            
    new_leaderboard = pd.DataFrame({"Username": username, "Time": elapsed_time}, index=[0])
    new_leaderboard.to_csv(leaderboard_file, mode='a', header=False, index=False)

    leaderboard = load_leaderboard()
    sorted_leaderboard = leaderboard.sort_values(by=["Time"])
    
    print("\nLeaderboard:")
    print(sorted_leaderboard)


def main():
    print("Input missing number from array")
    load_leaderboard()  # Ensure leaderboard is loaded, but no need to save it separately
    add_missing_num()


if __name__ == "__main__":
    main()
