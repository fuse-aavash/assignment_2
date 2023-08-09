import json


def filter_adults(input_file, output_file):
    """
    Reads a CSV file and filters rows for individuals who are 18 years or older.
    Writes the filtered data to a new CSV file.

    Parameters:
        input_file (str): The name of the input CSV file.
        output_file (str): The name of the output CSV file.
    """
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
                open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            
            header = infile.readline().strip()
            print(header)
            outfile.write(header + '\n')
            for line in infile:
                print(line)
                name, age = line.strip().split(',')
                age = int(age)
                if age >= 18:
                    outfile.write(line)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        print("Error: Invalid data in the 'Age' column. Expected an integer.")


INPUT_FILENAME = "data.csv"
OUTPUT_FILENAME = "adults.csv"
filter_adults(INPUT_FILENAME, OUTPUT_FILENAME)


def add_to_json(filename, new_data):
    """
    Reads JSON data from the file, adds the new dictionary to it, and writes the updated data back to the same file.

    Parameters:
        filename (str): The name of the JSON file.
        new_data (dict): The dictionary to be added to the JSON data.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)

        existing_data.append(new_data)  # Append the new dictionary to the existing list

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, indent=4)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON data in file '{filename}'.")


data = {"name": "Aavash Bhattarai", "age": 23}
add_to_json("data.json", data)


def search_log(log_file, search_keyword):
    """
    Searches for lines containing the search keyword in the log file and displays the matching lines.

    Parameters:
        log_file (str): The name of the log file.
        search_keyword (str): The keyword to search for.
    """
    try:
        with open(log_file, 'r', encoding='utf-8') as file:
            for line in file:
                if search_keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")


LOG_FILENAME = "app.log"
KEYWORD_TO_SEARCH = "ERROR"
search_log(LOG_FILENAME, KEYWORD_TO_SEARCH)
