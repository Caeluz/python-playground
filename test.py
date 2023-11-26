import pandas as pd
import os

# Specify the file path
file_path = 'leaderboard.csv'

# Check if the file exists
if os.path.isfile(file_path):
    # Read the existing CSV file into a DataFrame
    existing_df = pd.read_csv(file_path)

    # Display the existing DataFrame
    print('Existing DataFrame:')
    print(existing_df)

    # Create new data to append
    new_data = {'Username': [4, 5],
                'Time': ['D', 'E']}

    # Create a DataFrame from the new data
    new_df = pd.DataFrame(new_data)

    # Append the new data to the existing DataFrame
    updated_df = new_df.to_csv(file_path, mode='a', header=False, index=False)

