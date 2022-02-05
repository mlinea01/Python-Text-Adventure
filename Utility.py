def get_player_choice(choices, prompt_msg, confirm_func=None):
    choice = None
    while choice is None:
        print(prompt_msg)
        for i in range(len(choices)):
            print(str(i+1) + ". " + str(choices[i]))
        choice_index = int(input("\nYour choice: ")) - 1
        choice = choices[choice_index]
        if confirm_func is not None:
            confirmed = confirm_func(choice)
            if not confirmed:
                choice = None
    return choice
