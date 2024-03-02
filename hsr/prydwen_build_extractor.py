import os
import pandas as pd

# https://docs.google.com/spreadsheets/d/1SQK2xihURxiA2PTp0lAiRYXlphnm-EFa3CoKaUO7UOc/edit#gid=0
def file_to_json(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    # Determine file type (Excel or CSV) based on file extension
    if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        # Read Excel file
        df = pd.read_excel(file_path)
    elif file_name.endswith('.csv'):
        # Read CSV file
        df = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide an Excel (.xlsx, .xls) or CSV (.csv) file.")

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    return json_data

def save_json(json_data, output_file):
    with open(output_file, 'w') as f:
        f.write(json_data)

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    input_file_name = 'prydwen_builds.csv'  # Replace with your input file name
    output_file_name = 'prydwen_builds.json'  # Replace with the desired output file name

    json_data = file_to_json(input_file_name)
    output_file_path = os.path.join(script_dir, output_file_name)
    save_json(json_data, output_file_path)

    print(f"JSON data has been saved to {output_file_path}.")
