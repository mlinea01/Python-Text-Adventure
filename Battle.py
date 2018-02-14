class Battle:

    player = None
    enemy = None

    @classmethod
    def fight(cls, player, enemy):
        cls.player = player
        cls.enemy = enemy

        while enemy.hp > 0 and player.hp > 0:
            if cls.player.speed > cls.enemy.speed:
                fighters = [player, enemy]
            else:
                fighters = [enemy, player]

            i = 0
            while i < len(fighters):
                fighter = fighters[i]
                fighter.turn_start()
                other_fighter = fighters[(i+1) % 2]
                if fighter.cannot_attack > 0:
                    print(fighter.name + " cannot attack!")
                else:
                    chosen_attack = fighter.choose_attack()
                    if chosen_attack is not None:
                        print(fighter.name + " uses " + chosen_attack.name)
                        if chosen_attack.name == "Block":
                            fighter.hit_by(chosen_attack)
                        else:
                            other_fighter.hit_by(chosen_attack)
                i += 1
                fighter.turn_end()
                print("")
