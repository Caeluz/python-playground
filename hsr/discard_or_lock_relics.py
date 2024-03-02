import os
import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def process_relics(relics_data, prydwen_data):
    for relic in relics_data['relics']:
        matched = False
        for prydwen_relic in prydwen_data:
            if prydwen_relic['Relic Set'] == relic['set'] and prydwen_relic[relic['slot']] == relic['mainstat']:
                print(f"This relic id ({relic['_id']}) can be used by {prydwen_relic['Name']} based on:")
                print(f"- Set: {relic['set']}")
                print(f"- Slot: {relic['slot']}")
                print(f"- Main Stat: {relic['mainstat']}")
                print("Substats:")
                for substat in relic['substats']:
                    print(f"  - {substat['key']}: {substat['value']}")
                print()
                matched = True
                break
        if not matched:
            print(f"This relic id ({relic['_id']}) cannot be used by anyone")
            print()

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relics_file = os.path.join(script_dir, 'HSRScanData_20240302_202626.json')
    prydwen_file = os.path.join(script_dir, 'prydwen_data.json')

    relics_data = load_json(relics_file)
    prydwen_data = load_json(prydwen_file)

    process_relics(relics_data, prydwen_data)
