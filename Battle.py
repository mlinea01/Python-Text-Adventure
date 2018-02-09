class Battle:

    @classmethod
    def fight(cls, player, enemy):

        fighters = []
        if player.speed > enemy.speed:
            fighters.append(player)
            fighters.append(enemy)
        else:
            fighters.append(enemy)
            fighters.append(player)

        while enemy.hp > 0 and player.hp > 0:
            i = 0
            while i < len(fighters):
                fighter = fighters[i]
                other_fighter = fighters[(i+1) % 2]
                chosen_attack = fighter.chooseAttack()
                print("\n" + fighter.name + " uses " + chosen_attack.name)
                other_fighter.hit_by(chosen_attack)
                i += 1
                print("")
