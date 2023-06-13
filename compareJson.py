import json

filename = "list1.json"
filename1 = "list2.json"

def main():
    try:
        with open(filename, 'r') as file:
            data1 = json.load(file)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    try:
        with open(filename1, 'r') as file:
            data2 = json.load(file)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")

    # Extract usernames from the first JSON object
    usernames1 = {obj["username"] for obj in data1}

    # Extract usernames from the second JSON object
    usernames2 = {obj["username"] for obj in data2}

    if data1 == data2:
        print("THe JSON objects are equal.")
    else:
        print("The JSON objects are not equal.")
    
    if len(data1) < len(data2):
        print("One more following.")
    else:
        print("One less following")

    names_not_equal = usernames1.symmetric_difference(usernames2)
    # Print the names that are not equal
    for name in names_not_equal:
        print(name)

# Check if the script is being run directly
if __name__ == "__main__":
    main()