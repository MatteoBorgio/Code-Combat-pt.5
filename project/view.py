from colorama import init, Fore, Style

init(autoreset=True)


class ConsoleView:
    def show_welcome(self):
        print(Style.BRIGHT + Fore.CYAN + "=== COMBAT SIMULATION ===")

    def show_validation_error(self, component, message):
        print(Fore.RED + f"❌ Creation {component} failed. Error: {message}")
    
    def show_default_weapon(self, player_name, default_weapon_name):
        print(Fore.MAGENTA + f"{player_name} uses: {default_weapon_name}")
    
    def show_initial_stats(self, p1, p2):
        left = (Fore.GREEN + f"{p1.name} (HP: {p1.health} ❤️, STRENGTH: {p1.strength} 💪🏻, DEXTRITY: {p1.dextrity} ⚡)")
        right = (Fore.YELLOW + f"{p2.name} (HP: {p2.health} ❤️, STRENGTH: {p2.strength} 💪🏻, DEXTRITY: {p2.dextrity} ⚡)")
        print(left + " \n" + right)

    def show_turn_header(self, turn_number):
        print(Style.BRIGHT + Fore.BLUE + f"--- Turn {turn_number} 📢 ---")

    def show_potion_decision(self, player_name, potion_name):
        print(Fore.MAGENTA + f"{player_name} decides to use '{potion_name}' 🧪")
    
    def show_action_failure(self, player_name, action_name, reason):
        print(Fore.RED + f"❌ Action {action_name} failed: {player_name} {reason}")

    def show_potion_success(self, player_name, effect_desc, current_hp_msg):
        print(Fore.GREEN + f"✨ {player_name} used the potion: {effect_desc}. {player_name} (HP: {current_hp_msg}) ✨")
    
    def show_attack_result(self, attacker_name, defender_name, damage):
        print(Fore.YELLOW + f"⚔️ {attacker_name} attacks {defender_name} and deals {damage} damage ⚔️")

    def show_winner(self, winner_name):
        print(Style.BRIGHT + Fore.GREEN + f"The winner is: {winner_name} 🏆")

    def get_user_input(self, prompt):
        player_input = input(Fore.YELLOW + str(prompt))
        return player_input
