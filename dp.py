import os
import pandas as pd
from enum import Enum

# Creating the menu options using Enum
class Selection(Enum):
    ADD = 1      # Add a new videogame
    DELETE = 2   # Delete an existing videogame
    SHOW = 3     # Show all videogames
    EXIT = 4     # Exit the program
    UPDATE = 5   # Update an existing videogame
    SEARCH = 6   # Search for a videogame

# Function to display the menu and return the user's selection
def menu():
    for i in Selection:
        print(f'{i.value} - {i.name}')
    return Selection(int(input('Your selection: ')))

# Function to add a new videogame to the JSON
def add_to_json():
    videogame_name = input('Enter videogame name: ')
    year_release = input('Enter release year: ')

    new_data = pd.DataFrame([[videogame_name, year_release]], columns=['Videogame Name', 'Release Year'])

    if os.path.isfile('videogames.json'):
        df = pd.read_json('videogames.json', lines=True)
        df = pd.concat([df, new_data], ignore_index=True)
    else:
        df = new_data

    df.to_json('videogames.json', orient='records', lines=True)
    print("Videogame added to JSON!")

# Function to display the contents of the JSON file
def show_json():
    if os.path.isfile('videogames.json'):
        df = pd.read_json('videogames.json', lines=True)
        print(df)
    else:
        print("No JSON file found.")

# Function to delete a videogame from the JSON file
def delete_from_json():
    if not os.path.isfile('videogames.json'):
        print("No JSON file found.")
        return

    df = pd.read_json('videogames.json', lines=True)
    print(df)

    game_to_delete = input("Enter the name of the videogame to delete: ")

    if game_to_delete in df['Videogame Name'].values:
        df = df[df['Videogame Name'] != game_to_delete]
        df.to_json('videogames.json', orient='records', lines=True)
        print(f"{game_to_delete} was deleted from JSON.")
    else:
        print(f"{game_to_delete} not found in JSON.")

# Function to update an existing videogame in the JSON file
def update_json():
    if not os.path.isfile('videogames.json'):
        print("No JSON file found.")
        return

    df = pd.read_json('videogames.json', lines=True)
    print(df)

    game_to_update = input("Enter the name of the videogame to update: ")

    if game_to_update in df['Videogame Name'].values:
        new_name = input("Enter new name (leave blank to keep current name): ")
        new_year = input("Enter new release year (leave blank to keep current year): ")

        if new_name:
            df.loc[df['Videogame Name'] == game_to_update, 'Videogame Name'] = new_name
        if new_year:
            df.loc[df['Videogame Name'] == game_to_update, 'Release Year'] = int(new_year)

        df.to_json('videogames.json', orient='records', lines=True)
        print(f"{game_to_update} was updated in JSON.")
    else:
        print(f"{game_to_update} not found in JSON.")

# Function to search for a videogame in the JSON file
def search_json():
    if not os.path.isfile('videogames.json'):
        print("No JSON file found.")
        return

    df = pd.read_json('videogames.json', lines=True)
    search_query = input("Enter the name of the videogame to search for: ")

    result = df[df['Videogame Name'] == search_query]

    if not result.empty:
        print(result)
    else:
        print(f"{search_query} not found in JSON.")

# Function to clear the screen based on the operating system
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear command for Windows or Unix-based OS

# Function to exit the program with screen clearing
def exit_program():
    print("Saving data and exiting...")
    clear_screen()  # Clear the screen
    exit()  # Exit the program

# Main loop to run the menu
while True:
    user_selection = menu()  # Display the menu and get the user's choice
    if user_selection == Selection.ADD:
        add_to_json()  # Add a new videogame
    elif user_selection == Selection.DELETE:
        delete_from_json()  # Delete a videogame
    elif user_selection == Selection.SHOW:
        show_json()  # Show all videogames
    elif user_selection == Selection.EXIT:
        exit_program()  # Exit the program
    elif user_selection == Selection.UPDATE:
        update_json()  # Update an existing videogame
    elif user_selection == Selection.SEARCH:
        search_json()  # Search for a videogame
