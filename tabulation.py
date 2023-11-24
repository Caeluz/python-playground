# Create a list of sheet names
sheet_names = ["Sheet2", "Sheet3", "Sheet4"]

# Initialize the starting row number
row_number = 15

# Number of rows to print
num_rows = 40

# Initialize the starting column letter index
column_index = 0

# Define the columns to include in the pattern
columns = ['B', 'C', 'D', 'E', 'H', 'I', 'J', 'K']

# Loop through the columns
for column_index in range(len(columns)):
    # Get the current column letter
    current_column = columns[column_index]

    # Loop through the rows
    for row_index in range(num_rows):
        # Loop through the sheets
        for i, sheet_name in enumerate(sheet_names):
            # Print the pattern with an equals sign for the first sheet
            if i == 0:
                print(f"={sheet_name}!{current_column}{row_number}", end="")
            else:
                print(f"{sheet_name}!{current_column}{row_number}", end="")

            # Print a plus sign if it's not the last sheet
            if i < len(sheet_names) - 1:
                print("+ ", end="")

        # Move to the next row
        row_number += 5

        # Print a newline if it's not the last row
        if row_index < num_rows - 1:
            print()

    # Reset the row number to 15 for the next column
    row_number = 15

    # Print a newline if it's not the last column
    if column_index < len(columns) - 1:
        print()
