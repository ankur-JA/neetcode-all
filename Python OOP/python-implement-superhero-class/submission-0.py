class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health



# TODO: Create Superhero instances

superHero_1 = SuperHero("Batman", "Intelligence", 100)
superHero_2 = SuperHero("Superman", "Strength", 150)


# TODO: Print out the attributes of each superhero

print(superHero_1.name)
print(superHero_1.power)
print(superHero_1.health)
print(superHero_2.name)
print(superHero_2.power)
print(superHero_2.health)
