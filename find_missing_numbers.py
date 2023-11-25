import random
import time
import msvcrt

# pip install pywin32
import win32api

# working on
def get_input_without_enter():
    result = ""
    while True:
        for i in range(256):
            if win32api.GetAsyncKeyState(i) & 1:
                # Check if Enter key is pressed
                if i == 13:
                    return result
                char = chr(i)
                result += char
        time.sleep(0.01)  # Add a small delay to avoid high CPU usage
    

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
                return num_arr, random_num_arr, difficulty
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue



def add_missing_num():
    num_arr, random_num_arr, difficulty = difficulty_level()
    
    print(difficulty)
    start_time = time.time()

    while len(random_num_arr) < len(num_arr):
        while True:
            try:
                print(random_num_arr)
                missing_num = int(input("Missing number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

        if missing_num in random_num_arr:
            print("Number already in array.")
        else:
            random_num_arr.append(missing_num)
            random_num_arr.sort()  # Sort the array after each addition

            # remaining_numbers = set(num_arr) - set(random_num_arr)
            # print(f"Numbers remaining: {sorted(remaining_numbers)}")

    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    
    print(f"You completed the array in {elapsed_time} seconds!")
    print("You have successfully added the missing number(s) to the array:", random_num_arr)


def main():
    user_input = get_input_without_enter()
    print(user_input)
    print("Input missing number from array")
    add_missing_num()


if __name__ == "__main__":
    main()