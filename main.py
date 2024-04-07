import os
import pickle

from character import Character
from dice import roll_dice, display_dice_images
from Global import Global_Attributes, Global_Skills


CHARACTERS_FOLDER = "characters"

def create_character():
    name = input("Enter character name: ")
    attributes = {}
    print("Enter attribute values:")
    for attribute_name in Global_Attributes:
        value = int(input(f"{attribute_name}: "))
        attributes[attribute_name] = value
    skills = {}
    print("Enter skill values (0-5):")
    for skill_name in Global_Skills:
        value = int(input(f"{skill_name}: "))
        skills[skill_name] = value
    return Character(name, attributes, skills)

def save_character(character):
    if not os.path.exists(CHARACTERS_FOLDER):
        os.makedirs(CHARACTERS_FOLDER)
    file_path = os.path.join(CHARACTERS_FOLDER, character.name + ".dat")
    with open(file_path, 'wb') as file:
        pickle.dump(character, file)
    print("Character saved successfully!")

def load_characters():
    characters = []
    if not os.path.exists(CHARACTERS_FOLDER):
        return characters
    for file_name in os.listdir(CHARACTERS_FOLDER):
        if file_name.endswith(".dat"):
            file_path = os.path.join(CHARACTERS_FOLDER, file_name)
            with open(file_path, 'rb') as file:
                character = pickle.load(file)
                characters.append(character)
    return characters

def main():
    characters = load_characters()

    while True:
        print("\nMenu:")
        print("1. Create a new character")
        print("2. Edit a character")
        print("3. Roll dice for a character")
        print("4. List all characters")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            character = create_character()
            characters.append(character)
            save_character(character)
            print("Character created successfully!")
            print(character.__dict__)
        elif choice == "2":
            if not characters:
                print("No characters available. Please create a character first.")
            else:
                print("Select a character to edit:")
                for i, character in enumerate(characters, 1):
                    print(f"{i}. {character.name}")
                selection = int(input("Enter the number of the character: ")) - 1
                if selection < 0 or selection >= len(characters):
                    print("Invalid selection.")
                else:
                    character = characters[selection]
                    print(f"Character selected: {character.name}")
                    character.edit_attribute_or_skill()
                    save_character(character)
        elif choice == "3":
            if not characters:
                print("No characters available. Please create a character first.")
            else:
                print("Select a character to roll for:")
                for i, character in enumerate(characters):
                    print(f"{i + 1}. {character.name}")
                selection = int(input("Enter the number of the character: ")) - 1
                if selection < 0 or selection >= len(characters):
                    print("Invalid selection.")
                else:
                    character = characters[selection]
                    selected_attribute, selected_skill = character.select_attribute_and_skill()
                    dice_pool = character.attributes.get(selected_attribute, 0) + character.skills.get(selected_skill, 0)
                    hunger = int(input("Enter your hunger level (0-5): "))
                    black_results = roll_dice(dice_pool - hunger, "Black")
                    red_results = roll_dice(hunger, "Red")
                    display_dice_images(black_results, red_results)
        elif choice == "4":
            print("List of all characters:")
            for character in characters:
                print(character.name)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()