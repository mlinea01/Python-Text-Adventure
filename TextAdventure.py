from time import sleep
from Battle import Battle
from CharacterCreator import CharacterCreator
from adventures.Forest.ForestAdventure import ForestAdventure
from characters.Enemies import TrainingDummy

class Main:

    # Character creation
    player = CharacterCreator.make_character()
    sleep(2)

    # Tutorial fight
    print("")
    print("\nYou'll need to learn how to fight out there. Let's see what ya got!")
    print("Attack this training dummy to practice.\n")
    print("")
    sleep(5)
    Battle().start(player, [TrainingDummy()])

    # Forest level
    ForestAdventure([player])
