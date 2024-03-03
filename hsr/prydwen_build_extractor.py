import os
import pandas as pd
import re

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

    # Remove percentage signs from 'Body', 'Feet', 'Planar Sphere', and 'Link Rope' columns
    df['Body'] = df['Body'].str.replace('%', '')
    df['Feet'] = df['Feet'].str.replace('%', '')
    df['Feet'] = df['Feet'].str.replace('Speed', 'SPD')
    
    df['Planar Sphere'] = df['Planar Sphere'].str.replace('%', '')
    df['Planar Sphere'] = df['Planar Sphere'].str.replace('DMG', 'DMG Boost')
    df['Link Rope'] = df['Link Rope'].str.replace('%', '')
    df['Link Rope'] = df['Link Rope'].str.replace('Energy Regen Rate', 'Energy Regeneration Rate')  
    
    # Add "Head":"HP" and "Hands":"ATK" to all builds
    df['Head'] = 'HP'
    df['Hands'] = 'ATK'
    
    # Convert columns with commas into arrays and remove spaces
    df['Relic Set'] = df['Relic Set'].apply(lambda x: [s.strip() for s in x.split(',')])
    df['Body'] = df['Body'].apply(lambda x: [s.strip() for s in x.split(',')])
    df['Feet'] = df['Feet'].apply(lambda x: [s.strip() for s in x.split(',')])
    df['Planetary Set'] = df['Planetary Set'].apply(lambda x: [s.strip() for s in x.split(',')])
    df['Planar Sphere'] = df['Planar Sphere'].apply(lambda x: [s.strip() for s in x.split(',')] if pd.notna(x) else None)
    df['Link Rope'] = df['Link Rope'].apply(lambda x: [s.strip() for s in x.split(',')])


    # Add 'Boost' after 'Physical DMG' in 'Planar Sphere' column

    # Modify 'Substats' column
    df['Substats'] = df['Substats'].str.replace('%', '_')  # Replace '%' with '_'
    df['Substats'] = df['Substats'].str.replace('CRIT RATE', 'CRIT Rate_')
    df['Substats'] = df['Substats'].str.replace('CRIT DMG', 'CRIT DMG_')
    df['Substats'] = df['Substats'].apply(lambda x: re.sub(r'\([^)]*\)', '', x))  # Remove text within parentheses
    df['Substats'] = df['Substats'].apply(lambda x: re.split(r' > | = | >= ', x))
    
    # Remove leading and trailing spaces from each substat
    df['Substats'] = df['Substats'].apply(lambda x: [substat.strip() for substat in x])

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
