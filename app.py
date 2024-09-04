import os
import h5py
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

# Function to add a new videogame to the HDF5 file
def add_to_hdf5():
    videogame_name = input('Enter videogame name: ')
    year_release = input('Enter release year: ')

    new_data = pd.DataFrame([[videogame_name, year_release]], columns=['Videogame Name', 'Release Year'])

    with h5py.File('videogames.h5', 'a') as hf:
        if 'videogames' in hf:
            df = pd.read_hdf('videogames.h5', 'videogames')
            df = pd.concat([df, new_data], ignore_index=True)
        else:
            df = new_data

        df.to_hdf('videogames.h5', key='videogames', mode='w')

    print("Videogame added to HDF5!")

# Function to display the contents of the HDF5 file
def show_hdf5():
    if os.path.isfile('videogames.h5'):
        df = pd.read_hdf('videogames.h5', 'videogames')
        print(df)
    else:
        print("No HDF5 file found.")

# Function to delete a videogame from the HDF5 file
def delete_from_hdf5():
    if not os.path.isfile('videogames.h5'):
        print("No HDF5 file found.")
        return

    df = pd.read_hdf('videogames.h5', 'videogames')
    print(df)

    game_to_delete = input("Enter the name of the videogame to delete: ")

    if game_to_delete in df['Videogame Name'].values:
        df = df[df['Videogame Name'] != game_to_delete]
        df.to_hdf('videogames.h5', key='videogames', mode='w')
        print(f"{game_to_delete} was deleted from HDF5.")
    else:
        print(f"{game_to_delete} not found in HDF5.")

# Function to update an existing videogame in the HDF5 file
def update_hdf5():
    if not os.path.isfile('videogames.h5'):
        print("No HDF5 file found.")
        return

    df = pd.read_hdf('videogames.h5', 'videogames')
    print(df)

    game_to_update = input("Enter the name of the videogame to update: ")

    if game_to_update in df['Videogame Name'].values:
        new_name = input("Enter new name (leave blank to keep current name): ")
        new_year = input("Enter new release year (leave blank to keep current year): ")

        if new_name:
            df.loc[df['Videogame Name'] == game_to_update, 'Videogame Name'] = new_name
        if new_year:
            df.loc[df['Videogame Name'] == game_to_update, 'Release Year'] = int(new_year)

        df.to_hdf('videogames.h5', key='videogames', mode='w')
        print(f"{game_to_update} was updated in HDF5.")
    else:
        print(f"{game_to_update} not found in HDF5.")

# Function to search for a videogame in the HDF5 file
def search_hdf5():
    if not os.path.isfile('videogames.h5'):
        print("No HDF5 file found.")
        return

    df = pd.read_hdf('videogames.h5', 'videogames')
    search_query = input("Enter the name of the videogame to search for: ")

    result = df[df['Videogame Name'] == search_query]

    if not result.empty:
        print(result)
    else:
        print(f"{search_query} not found in HDF5.")

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
        add_to_hdf5()  # Add a new videogame
    elif user_selection == Selection.DELETE:
        delete_from_hdf5()  # Delete a videogame
    elif user_selection == Selection.SHOW:
        show_hdf5()  # Show all videogames
    elif user_selection == Selection.EXIT:
        exit_program()  # Exit the program
    elif user_selection == Selection.UPDATE:
        update_hdf5()  # Update an existing videogame
    elif user_selection == Selection.SEARCH:
        search_hdf5()  # Search for a videogame
