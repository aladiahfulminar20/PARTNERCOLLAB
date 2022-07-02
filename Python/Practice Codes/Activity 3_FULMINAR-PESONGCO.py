
#
# BSIS-2AB : Activity 3: Python -- Object Oriented Programming
#

#
# Submitted By: Fulminar, Aladiah Mehriel P. & Pesongco, Daniel Y.
#

# Character class that receives the different character classes, weapons, and abilities.

class character:

    def __init__(self, class_name, class_weapon, class_ability1, class_ability2):
        self.class_name = class_name
        self.class_weapon = class_weapon
        self.class_ability1 = class_ability1
        self.class_ability2 = class_ability2

    def setClass(self):
        return self.class_name

    def setWeapon(self):
        return self.class_weapon

    def setAbility1(self):
        return self.class_ability1

    def setAbility2(self):
        return self.class_ability2

# We created a character creation function in order to reuse the function without looping the input functions.


def newChar():

    print("")
    print(" Character Class Selection: Enter the number of the specific character class.")
    print("                            ")
    print(" 1. Wizard ")
    print(" 2. Knight ")
    print(" 3. Archer ")
    print(" 4. Assassin")
    print("")
    print(" Example: Wizard")
    print("                            ")

    class_selection = input("Enter your class: ")

    print("")
    print(" Select your weapon: ")
    print(" Instruction: Enter the number of the specific weapon.")
    print("                            ")
    print(" 1. Wizard Staff")
    print(" 2. Sword")
    print(" 3. Bow & Arrow")
    print(" 4. Katar")
    print("                            ")

    weapon_selection = input("Enter your weapon: ")

    if weapon_selection == "1":
        class_weapon = "Wizard Staff"
    elif weapon_selection == "2":
        class_weapon = "Sword"
    elif weapon_selection == "3":
        class_weapon = "Bow & Arrow"
    elif weapon_selection == "4":
        class_weapon = "Katar"

    if class_selection == "1":
        print("")
        print(" Select your two abilities as a Wizard: ")
        print(" Instruction: Enter the number of the specific ability.")
        print("                            ")
        print(" 1. Energy Ball")
        print(" 2. Dragons Breath ")
        print(" 3. Crown of Flame ")
        print(" 4. Hail Storm")
        print("                            ")

        ability_selection1 = input("Enter your first chosen ability: ")
        ability_selection2 = input("Enter your second chosen ability: ")

        if ability_selection1 == "1":
            class_ability1 = "Energy Ball"

        elif ability_selection1 == "2":
            class_ability1 = "Dragons Breath"

        elif ability_selection1 == "3":
            class_ability1 = "Crown of Flame"

        elif ability_selection1 == "4":
            class_ability1 = "Hail Storm"

        if ability_selection2 == "1":
            class_ability2 = "Energy Ball"

        elif ability_selection2 == "2":
            class_ability2 = "Dragons Breath"

        elif ability_selection2 == "3":
            class_ability2 = "Crown of Flame"

        elif ability_selection2 == "4":
            class_ability2 = "Hail Storm"

        if ability_selection1 == ability_selection2:
            while(ability_selection1 == ability_selection2):
                print("")
                print(" Ability already selected, please choose a different ability.")
                ability_selection2 = input("Enter your second ability: ")

                if ability_selection2 == "1":
                    class_ability2 = "Energy Ball"

                elif ability_selection2 == "2":
                    class_ability2 = "Dragons Breath"

                elif ability_selection2 == "3":
                    class_ability2 = "Crown of Flame"

                elif ability_selection2 == "4":
                    class_ability2 = "Hail Storm"

                if(ability_selection1 != ability_selection2):
                    return character("Wizard", class_weapon, class_ability1, class_ability2)
                    break

        elif(ability_selection1 != ability_selection2):

            return character("Wizard", class_weapon, class_ability1, class_ability2)

    elif class_selection == "2":
        print("")
        print(" Select your two abilities as a Knight: ")
        print(" Instruction: Instruction: Enter the number of the specific ability.")
        print("                            ")
        print(" 1. Fire Slash")
        print(" 2. Power Slash ")
        print(" 3. Gigantic Storm ")
        print(" 4. Chaotic Disaster")
        print("                            ")

        ability_selection1 = input("Enter your first chosen ability: ")
        ability_selection2 = input("Enter your second chosen ability: ")

        if ability_selection1 == "1":
            class_ability1 = "Fire Slash"

        elif ability_selection1 == "2":
            class_ability1 = "Power Slash"

        elif ability_selection1 == "3":
            class_ability1 = "Gigantic Storm"

        elif ability_selection1 == "4":
            class_ability1 = "Chaotic Disaster"

        if ability_selection2 == "1":
            class_ability2 = "Fire Slash"

        elif ability_selection2 == "2":
            class_ability2 = "Power Slash"

        elif ability_selection2 == "3":
            class_ability2 = "Gigantic Storm"

        elif ability_selection2 == "4":
            class_ability2 = "Chaotic Disaster"

        if ability_selection1 == ability_selection2:
            while(ability_selection1 == ability_selection2):
                print("")
                print(" Ability already selected, please choose a different ability.")
                ability_selection2 = input("Enter your second ability: ")

                if ability_selection2 == "1":
                    class_ability2 = "Fire Slash"

                elif ability_selection2 == "2":
                    class_ability2 = "Power Slash"

                elif ability_selection2 == "3":
                    class_ability2 = "Gigantic Storm"

                elif ability_selection2 == "4":
                    class_ability2 = "Chaotic Disaster"

                if(ability_selection1 != ability_selection2):
                    return character("Knight", class_weapon, class_ability1, class_ability2)
                    break

        elif(ability_selection1 != ability_selection2):

            return character("Knight", class_weapon, class_ability1, class_ability2)

    elif class_selection == "3":
        print("")
        print(" Select your two abilities as a Archer: ")
        print(" Instruction: Instruction: Enter the number of the specific ability.")
        print("                            ")
        print(" 1. Take Aim")
        print(" 2. Quick Shot")
        print(" 3. Blazing Arrow")
        print(" 4. Frost Arrow")
        print("                            ")

        ability_selection1 = input("Enter your first chosen ability: ")
        ability_selection2 = input("Enter your second chosen ability: ")

        if ability_selection1 == "1":
            class_ability1 = "Take Aim"

        elif ability_selection1 == "2":
            class_ability1 = "Quick Shot"

        elif ability_selection1 == "3":
            class_ability1 = "Blazing Arrow"

        elif ability_selection1 == "4":
            class_ability1 = "Frost Arrow"

        if ability_selection2 == "1":
            class_ability2 = "Take Aim"

        elif ability_selection2 == "2":
            class_ability2 = "Quick Shot"

        elif ability_selection2 == "3":
            class_ability2 = "Blazing Arrow"

        elif ability_selection2 == "4":
            class_ability2 = "Frost Arrow"

        if ability_selection1 == ability_selection2:
            while(ability_selection1 == ability_selection2):
                print("")
                print(" Ability already selected, please choose a different ability.")
                ability_selection2 = input("Enter your second ability: ")

                if ability_selection2 == "1":
                    class_ability2 = "Take Aim"

                elif ability_selection2 == "2":
                    class_ability2 = "Quick Shot"

                elif ability_selection2 == "3":
                    class_ability2 = "Blazing Arrow"

                elif ability_selection2 == "4":
                    class_ability2 = "Frost Arrow"

                if(ability_selection1 != ability_selection2):
                    return character("Archer", class_weapon, class_ability1, class_ability2)
                    break

        elif(ability_selection1 != ability_selection2):

            return character("Archer", class_weapon, class_ability1, class_ability2)

    elif class_selection == "4":
        print("")
        print(" Select your two abilities as a Assassin: ")
        print(" Instruction: Instruction: Enter the number of the specific ability.")
        print("                            ")
        print(" 1. Cloaking")
        print(" 2. Enchant Poison")
        print(" 3. Sonic Acceleration")
        print(" 4. Meteor Assault")
        print("                            ")

        ability_selection1 = input("Enter your first ability: ")
        ability_selection2 = input("Enter your second ability: ")

        if ability_selection1 == "1":
            class_ability1 = "Cloaking"

        elif ability_selection1 == "2":
            class_ability1 = "Enchant Poison"

        elif ability_selection1 == "3":
            class_ability1 = "Sonic Acceleration"

        elif ability_selection1 == "4":
            class_ability1 = "Frost Arrow"

        if ability_selection2 == "1":
            class_ability2 = "Cloaking"

        elif ability_selection2 == "2":
            class_ability2 = "Enchant Poison"

        elif ability_selection2 == "3":
            class_ability2 = "Sonic Acceleration"

        elif ability_selection2 == "4":
            class_ability2 = "Meteor Assault"

        if ability_selection1 == ability_selection2:
            while(ability_selection1 == ability_selection2):
                print("")
                print(" Ability already selected, please choose a different ability.")
                ability_selection2 = input("Enter your second ability: ")

                if ability_selection2 == "1":
                    class_ability2 = "Cloaking"

                elif ability_selection2 == "2":
                    class_ability2 = "Enchant Poison"

                elif ability_selection2 == "3":
                    class_ability2 = "Sonic Acceleration"

                elif ability_selection2 == "4":
                    class_ability2 = "Meteor Assault"

                if(ability_selection1 != ability_selection2):
                    return character("Assassin", class_weapon, class_ability1, class_ability2)
                    break

        elif(ability_selection1 != ability_selection2):

            return character("Assassin", class_weapon, class_ability1, class_ability2)


# To have two character inputs, we used to variables to initialize the function newChar(), alternative to looping and to avoid outdated variables when passed inside the class Character.
o = newChar()  # initilization of newChar() in variable 'o'
p = newChar()  # initilization of newChar() in variable 'p'

# Output functions to print character class under the variable 'o' and 'p' initialization.

print("")
print("")
print("Character 1: ")
print("")
print("Class: ", o.setClass())
print("Class Weapon: ", o.setWeapon())
print("Class Abilities: {} & {}" .format(o.setAbility1(), o.setAbility2()))

print("")
print("")
print("Character 2: ")
print("")
print("Class: ", p.setClass())
print("Class Weapon: ", p.setWeapon())
print("Class Abilities: {} & {}" .format(p.setAbility1(), p.setAbility2()))
