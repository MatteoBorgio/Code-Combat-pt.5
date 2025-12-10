from player import Player
from view import ConsoleView
from setup import GameSetup
from random import randint

class GameController:
    def __init__(self, view: ConsoleView, player1: Player, player2: Player):
        self.__view = view
        self.__player1 = player1
        self.__player2 = player2

    @property
    def player1(self) -> Player:
        return self.__player1
    
    @property
    def player2(self) -> Player:
        return self.__player2

    def __handle_turn(self, player: Player, enemy: Player) -> None:
        potion = player.should_use_potion(enemy)
        if potion is not None:
            self.__view.show_potion_decision(player.name, potion.name) 
            result = player.use_potion(potion)
            if "error" not in result:
                self.__view.show_potion_success(player.name, potion.effect, player.health)
            else:   
                self.__view.show_action_failure(player.name, result['error'], result['reason'])
        damage = player.attack(enemy)
        self.__view.show_attack_result(player.name, enemy.name, damage)
    
    def start_game_loop(self):
        self.__view.show_welcome()
        turn = 0
        self.__view.show_default_weapon(self.__player1.name, self.__player1.weapon.name)
        self.__view.show_default_weapon(self.__player2.name, self.__player2.weapon.name)
        self.__view.show_initial_stats(self.__player1, self.__player2)
        while True:
            turn += 1
            self.__view.show_turn_header(turn)
            self.__handle_turn(self.__player1, self.__player2)
            if not self.__player2.is_alive():
                break
            self.__handle_turn(self.__player2, self.__player2)
            if not self.__player1.is_alive():
                break
            self.__player1.tick_buffs()
            self.__player2.tick_buffs()
        
        if self.__player1.is_alive():
            self.__view.show_winner(self.__player1.name)
        else:
            self.__view.show_winner(self.__player2.name)
            

if __name__ == "__main__":
    game_controller = GameController(ConsoleView(), Player(GameSetup.generate_name(), 50, 50, randint(10, 20), randint(10, 20)), Player(GameSetup.generate_name(), 50, 50, randint(10, 20), randint(10, 20)))
    GameSetup.setup(game_controller.player1)
    GameSetup.setup(game_controller.player2)
    game_controller.start_game_loop()                               