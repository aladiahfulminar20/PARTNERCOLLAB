
#
##
#

class character:

    def __init__(self, class_name, class_weapon, class_ability):
        self.class_name = class_name
        self.class_weapon = class_weapon
        self.class_ability = class_ability

    def setClass(self):
        return self.class_name

    def setWeapon(self):
        return self.class_weapon

    def setAbility(self):
        return self.class_ability


def newChar():

    print("")
    print(" Character Class Selection: (Enter the exact class name)")
    print("                            ")
    print(" 1. Wizard ")
    print(" 2. Knight ")
    print(" 3. Archer ")
    print(" 4. Assassin")
    print("")
    print(" Example: Wizard")
    print("                            ")

    class_name = input("Enter your class: ")

    print("")
    print(" Select your weapon: ")
    print(" Instruction: Enter out the exact weapon name, ex: Katar")
    print("                            ")
    print(" 1. Wizard Staff")
    print(" 2. Sword")
    print(" 3. Bow & Arrow")
    print(" 4. Katar")
    print("                            ")

    class_weapon = input("Enter your weapon: ")

    if class_name == "Wizard":
        print("")
        print(" Select your two abilities as a Wizard: ")
        print(" Instruction: Enter out the exact two abilities, ex: Energy Ball and Hail Storm")
        print("                            ")
        print(" 1. Energy Ball")
        print(" 2. Dragons Breath ")
        print(" 3. Crown of Flame ")
        print(" 4. Hail Storm")
        print("                            ")

    elif class_name == "Knight":
        print("")
        print(" Select your two abilities as a Knight: ")
        print(" Instruction: Enter out the exact two abilities, ex: Energy Ball and Hail Storm")
        print("                            ")
        print(" 1. Fire Slash")
        print(" 2. Power Slash ")
        print(" 3. Gigantic Storm ")
        print(" 4. Chaotic Disaster")
        print("                            ")

    elif class_name == "Archer":
        print("")
        print(" Select your two abilities as a Archer: ")
        print(" Instruction: Enter out the exact two abilities, ex: Energy Ball and Hail Storm")
        print("                            ")
        print(" 1. Take Aim")
        print(" 2. Quick Shot")
        print(" 3. Blazing Arrow")
        print(" 4. Frost Arrow")
        print("                            ")

    elif class_name == "Assassin":
        print("")
        print(" Select your two abilities as a Assassin: ")
        print(" Instruction: Enter out the exact two abilities, ex: Energy Ball and Hail Storm")
        print("                            ")
        print(" 1. Cloaking")
        print(" 2. Enchant Poison")
        print(" 3. Sonic Acceleration")
        print(" 4. Meteor Assault")
        print("                            ")

    class_ability = input("Enter your 2 abilities: ")

    return character(class_name, class_weapon, class_ability)


o = newChar()
p = newChar()

print("")
print("")
print("Character 1: ")
print("")
print("Class: ", o.setClass())
print("Class Weapon: ", o.setWeapon())
print("Class Abilities: ", o.setAbility())

print("")
print("")
print("Character 2: ")
print("")
print("Class: ", p.setClass())
print("Class Weapon: ", p.setWeapon())
print("Class Abilities: ", p.setAbility())
