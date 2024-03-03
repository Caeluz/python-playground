import json
import os
import pandas as pd

def compare_relics(prydwen_data, relics_data):
    rank_values = {'SSS': 4, 'S': 3, 'A': 2, 'B': 1}
    relic_slot_order = {'Head': 1, 'Hands': 2, 'Body': 3, 'Feet': 4, 'Planar Sphere': 5, 'Link Rope': 6}
    results = []
    for relic in relics_data['relics']:
        matched = False
        
        # Compare relic with Prydwen builds
        for prydwen_relic in prydwen_data:
            # Skip if the relic is already used (Not Available)
            
            # Skip if the relic level is not 0
            if relic['level'] != 0:
                continue
            
            if relic['set'] in prydwen_relic['Relic Set'] and relic['mainstat'] in prydwen_relic[relic['slot']]:
                
                substats_match = 0
                for substat in relic['substats']:
                    for prydwen_substat in prydwen_relic['Substats']:
                        if substat['key'] in prydwen_substat:
                            substats_match += 1
                            break
                if substats_match == 4:
                    rank = 'SSS'
                elif substats_match == 3:
                    rank = 'S'
                elif substats_match == 2:
                    rank = 'A'
                elif substats_match == 1:
                    rank = 'B'
                else:
                    rank = 'Cannot be used'
                
                

                # Append results to the list
                results.append({
                    'Relic ID': relic['_id'],
                    'Relic Set': relic['set'], 
                    'Relic Slot': relic['slot'],  
                    'Relic Level': relic['level'],  
                    'Character': prydwen_relic['Name'],
                    'Rank': rank,
                    'Mainstat': relic['mainstat'],
                    'Relic Set': relic['set'],
                    'Substats': ', '.join([substat['key'] for substat in relic['substats']])
                })
                matched = True
                
        if not matched:
            # If no match found, add to results with 'Cannot be used'
            results.append({
                'Relic ID': relic['_id'],
                'Character': 'None',
                'Rank': 'Cannot be used',
                'Mainstat': relic['mainstat'],
                'Relic Set': relic['set'],
                'Relic Slot': relic['slot'],
                'Substats': ', '.join([substat['key'] for substat in relic['substats']])
            })
    
        # Sort results for each relic based on rank
    # results.sort(key=lambda x: rank_values.get(x['Rank'], 0), reverse=True)
    # results.sort(key=lambda x: (-rank_values.get(x['Rank'], 0), x['Relic Set'], x['Relic Slot']))
    results.sort(key=lambda x: (-rank_values.get(x['Rank'], 0), relic_slot_order.get(x['Relic Slot'], 0), x['Relic Set']))
    

    return results

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    prydwen_file_name = 'hsr/prydwen_builds.json'  # Replace with your Prydwen build JSON file name
    relics_file_name = 'hsr/relics.json'  # Replace with your relics JSON file name

    with open(prydwen_file_name, 'r') as file:
        prydwen_json_data = json.load(file)

    with open(relics_file_name, 'r') as file:
        relics_json_data = json.load(file)

    comparison_results = compare_relics(prydwen_json_data, relics_json_data)

    # Save to JSON file
    output_json_file = os.path.join(script_dir, 'relic_comparison.json')
    with open(output_json_file, 'w') as file:
        json.dump(comparison_results, file, indent=4)

    # Convert to DataFrame and save to Excel file
    # df = pd.DataFrame(comparison_results)
    # df.to_excel('relic_comparison.xlsx', index=False)

    print("Comparison results saved to relic_comparison.json and relic_comparison.xlsx")
