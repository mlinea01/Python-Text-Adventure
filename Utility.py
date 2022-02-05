from time import sleep


def get_player_choice(choices, prompt_msg, confirm_func=None):
    choice = None
    while choice is None:
        print(prompt_msg)
        print_numbered_list(choices)
        user_input = input("\nYour choice: ")
        choice = choose(user_input, choices)
        if choice is None:
            print("Invalid choice!\n")
            sleep(1)
        elif confirm_func is not None and not confirm_func(choice):
            choice = None
    return choice

def print_numbered_list(list):
    for i in range(len(list)):
        print(str(i+1) + ". " + str(list[i]))

def choose(user_input, choices):
    choice_index = int(user_input) - 1 if user_input.isnumeric() else None
    if choice_index is None or choice_index < 0 or choice_index >= len(choices):
        return None
    else:
        return choices[choice_index]
