import json
import os

def load_json_file():
    folder_name=input('Enter folder name where JSON file is located: ')
    file_name= 'sai_varshith_meka_adoptions.json'
    file_location= "C:/Users/varsh/Desktop/sd_repositaries/files_assignment/sai_varshith_meka_adoptions.json"
    try:
        with open(file_location, 'r') as file:
            data = json.load(file)
            print('file loaded succesfully')
        return data    
    except FileNotFoundError as fnf_error:
        print(f'file{file_location} not found')
    except json.JSONDecodeError as json_error:
        print(f"Error decoding JSON: {json_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
data = load_json_file()