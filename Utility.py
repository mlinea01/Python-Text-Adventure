from time import sleep


def get_player_choice(choices, prompt_msg, confirm_func=None):
    choice = None
    while choice is None:
        print(prompt_msg)
        for i in range(len(choices)):
            print(str(i+1) + ". " + str(choices[i]))
        user_input = input("\nYour choice: ")
        choice_index = int(user_input) - 1 if user_input.isnumeric() else None
        if choice_index is None or choice_index < 0 or choice_index >= len(choices):
            print("Invalid choice!\n")
            sleep(1)
        else:
            choice = choices[choice_index]
            if confirm_func is not None:
                confirmed = confirm_func(choice)
                if not confirmed:
                    choice = None
    return choice
