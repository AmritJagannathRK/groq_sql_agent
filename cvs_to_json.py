import csv
import json
import os

def csv_to_json(csv_file_path, json_file_path):
    
    json_data = []

   
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

       
        for row in csv_reader:
            json_data.append(row)


    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"Successfully converted '{csv_file_path}' to '{json_file_path}'.")

if __name__ == "__main__":
    
    csv_file = input("Enter the path to the input CSV file: ")  
    json_file = os.path.splitext(csv_file)[0] + '.json' 
    
    # Check if the JSON file already exists and delete it if it does
    if os.path.exists(json_file):
        os.remove(json_file)
        print(f"Deleted existing JSON file: '{json_file}'.")

   
    csv_to_json(csv_file, json_file)