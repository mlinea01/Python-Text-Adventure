class Battle:

    def mainAttack(self,damage):

        training_dummy = damage
        print("")
        print("It was a direct hit!")
        print("You attacked the training dummy for",damage,"damage!")
        training_dummy -= damage
        print("training dummy:",training_dummy)
        print("")