class Battle:

    def mainAttack(self,spell):
        
        training_dummy = 10

        while training_dummy > 0:

            input("Press enter to attack")
            print("")
            print("You attacked with",spell.name)
            print("It was a direct hit!")
            print("You attacked the training dummy for",spell.damage,"damage!")
            training_dummy -= spell.damage

            if training_dummy < 0:
                training_dummy = 0

            print("training dummy:",training_dummy)
            print("")

        print("The training dummy was defeated!\n")