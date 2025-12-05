from weapon import Weapon
from potion import Potion
from random import choice

class GameSetup:

    NAME_LIST = [
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
    
    SURNAME_LIST = [ "Dawnspear", "Ironforge", "Shadowvale", "Stormborn", "Brightshield",
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
    
    MELEE_WEAPONS = [
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
    
    RANGED_WEAPONS = [
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
    
    def assign_potions(player) -> None:
        potions = [
            Potion("Healing Draught", "heal", 10, 1),
            Potion("Healing Draught", "heal", 10, 1),
        ]
        if player.strength >= player.dexterity:
            potions.append(Potion("Ogre Tonic", "buff_str", 2, 3))
        else:
            potions.append(Potion("Cat’s Grace", "buff_dex", 2, 3))

        try:
            player.potions = potions
        except AttributeError:
            print("Player not valid")
    
    def generate_name() -> str:
        return choice(GameSetup.NAME_LIST) + choice(GameSetup.SURNAME_LIST)
    
    def assign_weapon(player) -> None:
        try:
            if player.strength > player.dexterity:
                player.weapon = choice(GameSetup.MELEE_WEAPONS)
            else:
                player.weapon = choice(GameSetup.RANGED_WEAPONS)
        except AttributeError:
            print("Player not valid")

    def setup(player) -> None:
        GameSetup.assign_potions(player)
        GameSetup.assign_weapon(player)
        

    


    
    
