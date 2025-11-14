"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Lemanuel LEE Devane
Date: 11/10/2025

AI Usage: Filling in method implementations based on the assignment TODO comments,
guidance on method overriding and polymorphism, verifying that special abilities, Weapon class, and battle-system were correctly implemented, and helping format and organize the final code for readability
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"{self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"{self.char2.name} wins!")
        else:
            print("It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters
    """

    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic

    def attack(self, target):
        damage = self.strength
        print(f"{self.name} attacks for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def display_stats(self):
        print(f"--- {self.name} ---")
        print(f" Health:   {self.health}")
        print(f" Strength: {self.strength}")
        print(f" Magic:    {self.magic}")


class Player(Character):
    """
    Base class for player characters
    Derived from Character base class
    """

    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1 # starter level for all players
        self.experience = 0
        self.weapon = None  # Player could possibly have a weapon

    def display_stats(self):
        super().display_stats()
        print(f" Class:    {self.character_class}")
        print(f" Level:    {self.level}")
        print(f" EXP:      {self.experience}")


class Warrior(Player):
    """
    Warrior class - strong physical fighter
    """

    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 15, 5)

    def attack(self, target):
        damage = self.strength + 5  # warrior strength bonus
        if self.weapon:
            damage += self.weapon.damage_bonus  # add weapon bonus
        print(f"{self.name} slashes with a mighty strike for {damage} damage!")
        target.take_damage(damage)
# warrior special attack
    def power_strike(self, target):
        damage = self.strength + 12
        print(f"{self.name} performs POWER STRIKE for {damage} damage!")
        target.take_damage(damage)


class Mage(Player):
    """
    Mage class - magic spellcaster
    """

    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)

    def attack(self, target):
        damage = self.magic
        if self.weapon:
            damage += self.weapon.damage_bonus  # add weapon bonus
        print(f"{self.name} casts a magic bolt for {damage} damage!")
        target.take_damage(damage)
# mage special attack
    def fireball(self, target):
        damage = self.magic + 10
        print(f"{self.name} casts FIREBALL for {damage} damage!")
        target.take_damage(damage)


import random
class Rogue(Player):
    """
    Rogue class - sneaky fighter
    """

    def __init__(self, name):
        super().__init__(name, "Rogue", 90, 12, 10)

    def attack(self, target):
        
        damage = self.strength
        if self.weapon:
            damage += self.weapon.damage_bonus  # add weapon bonus
    #give rogues a 30% chance of critical hit which doubles the damag
        if random.randint(1, 10) <= 3:
            damage *= 2
            print(f"CRITICAL HIT! {self.name} deals {damage} damage!")
        else:
            print(f"{self.name} strikes swiftly for {damage} damage!")
        target.take_damage(damage)

    def sneak_attack(self, target):
        damage = self.strength * 2
        print(f"{self.name} performs SNEAK ATTACK for {damage} damage!")
        target.take_damage(damage)


class Weapon:
    """
    Allows for weapons to be taken by characters and incraments their damage based on the weapon damage num.
    """

    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        print(f"Weapon: {self.name} (Damage Bonus: +{self.damage_bonus})")


# ============================================================================
# MAIN PROGRAM FOR TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)

    # Create character instances
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")

    # Display stats
    print("\nCharacter Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    # Polymorphism test
    print("\nTesting Polymorphism:")
    dummy = Character("Training Dummy", 100, 0, 0)
    for c in [warrior, mage, rogue]:
        print(f"\n{c.name} attacks the dummy:")
        c.attack(dummy)
        dummy.health = 100  # reset dummy health

    # Special abilities
    print("\nTesting Special Abilities:")
    warrior.power_strike(Character("Enemy1", 50, 0, 0))
    mage.fireball(Character("Enemy2", 50, 0, 0))
    rogue.sneak_attack(Character("Enemy3", 50, 0, 0))

    # Weapon composition test
    print("\nTesting Weapons:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    sword.display_info()
    staff.display_info()
    dagger.display_info()

    # Battle system test
    print("\nBattle System Test:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()

    print("\n✅ Testing complete!")
