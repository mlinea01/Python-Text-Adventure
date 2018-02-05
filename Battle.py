class Battle:

    def mainAttack(self,training_dummy=10):

        print("")
        print("It was a direct hit!")
        print("You attacked the training dummy for 10 damage!")
        training_dummy-=10
        print("training dummy:",training_dummy)
        print("")

    def secondaryAttack(self,training_dummy=7):
        print("")
        print("It was a direct hit!")
        print("You attack the training dummy for 7 damage!")
        training_dummy-=7
        print("training dummy:",training_dummy)
        print("")