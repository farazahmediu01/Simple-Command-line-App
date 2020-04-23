from functionality import press_validation, input_loop, delete_names, sorted_names, make_file
from cmd_colors import text_color

def main():
    # global inp, storage, input_array, message
    # Initialzing main variables
    message = "\n[yellow]Enter name of your friends you want to invite in your party.[reset]"
    storage = []        # Main storage variable.
    input_array = []    # Partial storage variable.
    inp = None          # Defaul input variable.

    print(text_color(message))
    # Main loop.
    while True:

        # First block to be run.
        if inp == None:
            '''This block runs only first time where user enter names 
            till user_input =! an empty string.'''

            input_array = input_loop()
            storage.extend(input_array)
            print(f"You have entered {len(input_array)} names.")

        message = "\n[yellow]Press 'a' to Add names.\nPress 'd' to Delete names.\nPress 'r' to Read all names.\nPress 'e' to Exit."
        print(text_color(message))
        # print("Press 'd' to Delete names.")
        # print("Press 'r' to Read all names.")
        # print("Press 'e' to Exit.\n")

        # This is second conditonal block which handles the wrong input.
        inp = input(">").lower()
        if press_validation(inp):
            pass
        else:
            print("Error")
            print("You can only press the instructions blow.")
            continue

        # Add names
        if inp == 'a':
            input_array = input_loop()
            storage.extend(input_array)
            print(f"You have entered {len(input_array)} names.")

        # Delete names
        elif inp == 'd':
            input_array = input_loop()
            input_array = delete_names(input_array, storage)

            print(f"You hava successfully delete {len(input_array)} names.")
            for i in range(1, len(input_array) + 1):
                print(f"{i}) {input_array[i-1]}")

        # Sort names
        elif inp == 'r':
            print("Read name in a sorted way [y/n]?")
            inp = input(">").lower()
            sorted_names(inp, storage)
            print(f"Total {len(storage)} names")

        # Exit
        elif inp == 'e':
            make_file(storage)
            print("_" * 30)
            print("\nHave a nice day see you soon.")
            print("_" * 30)
            break


if __name__ == "__main__":
    main()
