from Global import Global_Attributes, Global_Skills

class Character:
    def __init__(self, name, attributes, skills):
        self.name = name
        self.attributes = attributes     
        self.skills = skills
    
    @property
    def max_willpower(self):
        return self.attributes.get("Resolve", 0) + self.attributes.get("Composure", 0)

    @property
    def max_health(self):
        return self.attributes.get("Stamina", 0) + 3
    
    def __str__(self):
        return f"Character(name={self.name}, attributes={self.attributes}, skills={self.skills})"
    
    def select_attribute_and_skill(self):
        print("Select an attribute to use:")
        for i, attribute_name in enumerate(Global_Attributes, 1):
            print(f"{i}. {attribute_name}: {self.attributes.get(attribute_name, 0)}")
        attribute_index = int(input("Enter the number of the attribute: ")) - 1
        selected_attribute = Global_Attributes[attribute_index]
        
        print("Select a skill to use:")
        for i, skill_name in enumerate(Global_Skills, 1):
            print(f"{i}. {skill_name}: {self.skills.get(skill_name, 0)}")
        skill_index = int(input("Enter the number of the skill: ")) - 1
        selected_skill = Global_Skills[skill_index]
        
        return selected_attribute, selected_skill
    
    def edit_attribute_or_skill(self):
        print("Select an option:")
        print("1. Edit attribute")
        print("2. Edit skill")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Select an attribute to edit:")
            for i, attribute_name in enumerate(Global_Attributes, 1):
                print(f"{i}. {attribute_name}: {self.attributes.get(attribute_name, 0)}")
            attribute_index = int(input("Enter the number of the attribute: ")) - 1
            selected_attribute = Global_Attributes[attribute_index]
            new_value = int(input("Enter the new value for the attribute: "))
            self.attributes[selected_attribute] = new_value
            print(f"{selected_attribute} updated to {new_value}.")
        elif choice == "2":
            print("Select a skill to edit:")
            for i, skill_name in enumerate(Global_Skills, 1):
                print(f"{i}. {skill_name}: {self.skills.get(skill_name, 0)}")
            skill_index = int(input("Enter the number of the skill: ")) - 1
            selected_skill = Global_Skills[skill_index]
            new_value = int(input("Enter the new value for the skill: "))
            self.skills[selected_skill] = new_value
            print(f"{selected_skill} updated to {new_value}.")
        else:
            print("Invalid choice. Please enter 1 or 2.")
