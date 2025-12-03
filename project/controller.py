from player import Player
from weapon import Weapon
from random import choice
from random import randint
from view import View
from potion import Potion

class GameController:
    def __init__(self, view: View, player1: Player, player2: Player):
        self.__view = view
        self.__player1 = player1
        self.__player2 = player2

    def __assign_potions(self, player: Player) -> list[Potion]:
        potions = [
            Potion("Healing Draught", "heal", 10, 1),
            Potion("Healing Draught", "heal", 10, 1),
        ]
        if player.strength >= player.dexterity:
            potions.append(Potion("Ogre Tonic", "buff_str", 2, 3))
        else:   
            potions.append(Potion("Cat’s Grace", "buff_dex", 2, 3))
        return potions
    
    def __assign_name(self) -> str:
        name_list = [
        "Arvelin", "Kaelor", "Thandric", "Elowen", "Rhaegar",
        "Miralen", "Dareth", "Selindra", "Korvin", "Althira",
        "Aeryn", "Luthien", "Faelar", "Sylwen", "Thalorien",
        "Nimaera", "Elandor", "Seraphiel", "Vaelis", "Caelith",
        "Brokkar", "Thrain", "Durgan", "Hildaen", "Magni",
        "Torvra", "Bofrid", "Kaelda", "Dornik", "Gruntha",
        "Malreth", "Xyra", "Kharzul", "Velthir", "Nergash",
        "Sarynth", "Dravok", "Zephra", "Morwen", "Kalzur",
        "Althorius", "Mirelda", "Seradion", "Ysara", "Velamir",
        "Kaenra", "Thalvion", "Nareth", "Elyndra", "Orveth",
        "Aerion", "Lysara", "Thaless", "Corvian", "Naela",
        "Myrren", "Sireth", "Calandra", "Varyn", "Oryssa"
        ]
        surname_list = [
        "Dawnspear", "Ironforge", "Shadowvale", "Stormborn", "Brightshield",
        "Nightwhisper", "Windrider", "Flameheart", "Moonglade", "Frostbane",
        "Oakenshield", "Dragonsong", "Silverleaf", "Stormbreaker", "Ravencrest",
        "Firebrand", "Emberfall", "Grimstone", "Whisperwind", "Starcrest",
        "Darkbane", "Stronghammer", "Winterfall", "Sunstrider", "Ironheart",
        "Lightbringer", "Mistwalker", "Stonehelm", "Skydancer", "Thornblade",
        "Wildborn", "Brightforge", "Blackthorn", "Ashenvale", "Frostforge",
        "Shadowbane", "Starweaver", "Bloodcrest", "Windwatcher", "Goldmantle",
        "Ironbeard", "Moonbrook", "Silverflame", "Stormwatch", "Fireweaver",
        "Runeborn", "Shadowbrook", "Thornbreaker", "Wolfsong", "Skywarden"
        ]   
        name = choice(name_list)
        surname = choice(surname_list)
        return name + " " + surname

    def __assign_weapon(self, player: Player) -> None:
        melee_weapons = [
        Weapon("Longsword", 5, 9, "melee"),
        Weapon("Battle Axe", 6, 10, "melee"),
        Weapon("Mace", 4, 8, "melee"),
        Weapon("Dagger", 2, 5, "melee"),
        Weapon("Warhammer", 7, 11, "melee"),
        Weapon("Greatsword", 8, 12, "melee"),
        Weapon("Sabre", 4, 7, "melee"),
        Weapon("Spear", 5, 8, "melee"),
        Weapon("War Scythe", 6, 9, "melee"),
        Weapon("Halberd", 7, 10, "melee")
        ]
        ranged_weapons = [
        Weapon("Longbow", 5, 9, "ranged"),
        Weapon("Shortbow", 3, 7, "ranged"),
        Weapon("Light Crossbow", 4, 8, "ranged"),
        Weapon("Heavy Crossbow", 6, 10, "ranged"),
        Weapon("Reinforced Sling", 2, 5, "ranged"),
        Weapon("Throwing Spear", 5, 9, "ranged"),
        Weapon("Chakram", 4, 8, "ranged"),
        Weapon("Elven Bow", 6, 10, "ranged"),
        Weapon("Gem-Tipped Darts", 3, 6, "ranged"),
        Weapon("Runic Staff", 4, 9, "ranged")
        ]
        if player.strength > player.dexterity:
            player.weapon = choice(melee_weapons)
        else:
            player.weapon = choice(ranged_weapons)

    def __handle_turn(self, player: Player, enemy: Player) -> None:
        potion = player.should_use_potion(enemy)
        if potion is not None:
            self.__view.show_potions_decision(player.name, potion.name) 
            result = player.use_potion(potion)
            if "error" not in result:
                self.__view.show_potion_success(player.name, potion.effect, player.health)
            else:   
                self.__view.show_action_failure(player.name, result['error'], result['reason'])
        damage = player.attack(enemy)
        self.__view.show_attack_result(player.name, enemy.name, damage, player.weapon)
    
    def start_game_loop(self):
        self.__view.show_welcome()
        turn = 0
        self.__player1.name = self.__assign_name()
        self.__assign_weapon(self.__player1)
        self.__assign_potions(self.__player1)
        self.__view.show_default_weapon(self.__player1.name, self.__player1.weapon.name)
        self.__player2.name = self.__assign_name()
        self.__assign_weapon(self.__player2)
        self.__assign_potions(self.__player1)
        self.__view.show_default_weapon(self.__player2.name, self.__player2.weapon.name)
        self.__view.show_initial_stats(self.__player1, self.__player2)
        while True:
            turn += 1
            self.__view.show_turn_header(turn)
            self.__handle_turn(self.__player1, self.__player2)
            if not self.__player2.is_alive():
                break
            self.__handle_turn(self.__player1, self.__player2)
            if not self.__player1.is_alive():
                break
            self.__player1.tick_buffs()
            self.__player2.tick_buffs()
        
        if self.__player1.is_alive():
            self.__view.show_winner(self.__player1.name)
        else:
            self.__view.show_winner(self.__player2.name)
            

if __name__ == "__main__":
    game_controller = GameController(View(), Player("", 50, 50, randint(10, 20), randint(10, 20), []), Player("", 50, 50, randint(10, 20), randint(10, 20), []))
    game_controller.start_game_loop()                               