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

# Function to add a new videogame to the CSV
def add_to_csv():
    # Get input from the user for the videogame name and release year
    videogame_name = input('Enter videogame name: ')
    year_release = input('Enter release year: ')

    # Create a DataFrame with the new data
    df = pd.DataFrame([[videogame_name, year_release]], columns=['Videogame Name', 'Release Year'])
    
    # Check if the CSV file exists, if not, create a new file
    if not os.path.isfile('videogames.csv'):
        df.to_csv('videogames.csv', index=False)  # Create a new file
    else:
        df.to_csv('videogames.csv', mode='a', header=False, index=False)  # Append the record to the existing file

    print("Videogame added to CSV!")

# Function to display the contents of the CSV file
def show_csv():
    # Check if the CSV file exists
    if os.path.isfile('videogames.csv'):
        df = pd.read_csv('videogames.csv')
        print(df)  # Display the content of the file
    else:
        print("No CSV file found.")  # Message if the file does not exist

# Function to delete a videogame from the CSV file
def delete_from_csv():
    # Check if the CSV file exists
    if not os.path.isfile('videogames.csv'):
        print("No CSV file found.")
        return
    
    # Read the CSV file and display its contents
    df = pd.read_csv('videogames.csv')
    print(df)

    # Ask for the name of the videogame to delete
    game_to_delete = input("Enter the name of the videogame to delete: ")

    # Check if the game exists in the file
    if game_to_delete in df['Videogame Name'].values:
        # Delete the game from the DataFrame and save to the file
        df = df[df['Videogame Name'] != game_to_delete]
        df.to_csv('videogames.csv', index=False)
        print(f"{game_to_delete} was deleted from the CSV.")
    else:
        print(f"{game_to_delete} not found in the CSV.")  # Message if the game is not found

# Function to update an existing videogame in the CSV file
def update_csv():
    # Check if the CSV file exists
    if not os.path.isfile('videogames.csv'):
        print("No CSV file found.")
        return

    # Read the file and display its contents
    df = pd.read_csv('videogames.csv')
    print(df)

    # Ask for the name of the videogame to update
    game_to_update = input("Enter the name of the videogame to update: ")

    # Check if the game exists in the file
    if game_to_update in df['Videogame Name'].values:
        # Ask for new data from the user (leave blank to keep current data)
        new_name = input("Enter new name (leave blank to keep current name): ")
        new_year = input("Enter new release year (leave blank to keep current year): ")

        # Update the data only if the user entered new values
        if new_name:
            df.loc[df['Videogame Name'] == game_to_update, 'Videogame Name'] = new_name
        if new_year:
            df.loc[df['Videogame Name'] == game_to_update, 'Release Year'] = int(new_year)

        # Save the updated data to the file
        df.to_csv('videogames.csv', index=False)
        print(f"{game_to_update} was updated.")
    else:
        print(f"{game_to_update} not found in the CSV.")  # Message if the game is not found

# Function to search for a videogame in the CSV file
def search_csv():
    # Check if the CSV file exists
    if not os.path.isfile('videogames.csv'):
        print("No CSV file found.")
        return

    # Read the file and ask for the game name to search for
    df = pd.read_csv('videogames.csv')
    search_query = input("Enter the name of the videogame to search for: ")

    # Check if the game is found and display the result
    if search_query in df['Videogame Name'].values:
        result = df[df['Videogame Name'] == search_query]
        print(result)
    else:
        print(f"{search_query} not found in the CSV.")  # Message if the game is not found

# Function to clear the screen based on the operating system
def clear_screen():os.system('clear')  # Command to clear screen on Mac/Linux

# Function to exit the program with screen clearing
def exit_program():
    print("Saving data and exiting...")
    clear_screen()  # Clear the screen
    exit()  # Exit the program

# Main loop to run the menu
while True:
    user_selection = menu()  # Display the menu and get the user's choice
    if user_selection == Selection.ADD:add_to_csv()  # Add a new videogame
    if user_selection == Selection.DELETE:
        delete_from_csv()  # Delete a videogame
    if user_selection == Selection.SHOW:
        show_csv()  # Show all videogames
    if user_selection == Selection.EXIT:
        exit_program()  # Exit the program
    if user_selection == Selection.UPDATE:
        update_csv()  # Update an existing videogame
    if user_selection == Selection.SEARCH:
        search_csv()  # Search for a videogame