from copy import copy

class Battle:

    players = []
    enemy = None

    @classmethod
    def fight(cls, players, enemy):
        cls.players = players
        cls.enemy = enemy
        from Multiplayer import GameSession
        server = GameSession.get_server()

        while enemy.hp > 0 and Battle.playersAlive():

            fighters = copy(cls.players)
            fighters.append(enemy)
            i = 0
            while i < len(fighters):
                fighter = fighters[i]
                fighter.turn_start()

                if i == len(fighters)-1:
                    other_fighter = players[0]
                else:
                    other_fighter = enemy

                if fighter.cannot_attack > 0:
                    server.print_text(fighter.name + " cannot attack!")
                else:
                    chosen_attack = fighter.choose_attack()
                    if chosen_attack is not None:
                        server.print_text(fighter.name + " uses " + chosen_attack.name)
                        if chosen_attack.name == "Block":
                            fighter.hit_by(chosen_attack)
                        else:
                            other_fighter.hit_by(chosen_attack)
                i += 1
                fighter.turn_end()
                server.print_text("")

    @classmethod
    def playersAlive(cls):
        for player in cls.players:
            if player.hp > 0:
                return True

        return False
