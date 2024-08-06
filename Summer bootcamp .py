import time


def invalid_input_handler(prompt, valid_options):
    """Prompt the user until they enter a valid option.

    Args:
        prompt (str): The input prompt to show the user.
        valid_options (list): A list of valid options.

    Returns:
        str: The valid user input.
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_options:
            return choice
        else:
            print(f"Invalid input. Please enter one of the following: "
                  f"{', '.join(valid_options)}")


def print_pause(message, pause=2):
    """Prints a message and then pauses for a given duration.

    Args:
        message (str): The message to print.
        pause (int): The duration to wait after printing the message.
    """
    print(message)
    time.sleep(pause)


def Fit_Fusion():
    acc = invalid_input_handler("Play again? (yes/no): ", ["yes", "no"])
    if acc == "yes" :
        user_name = invalid_input_handler("Please enter your user_name")
        password = invalid_input_handler("Please enter your password")
    print_pause("Please enter your profiles")   
    age = invalid_input_handler(int("Please enter your age"))
    height = invalid_input_handler(int("Please enter your height"))
    weight = invalid_input_handler(int("Please enter your weight"))
    BMI = weight/(height/100)^2
    allergies = invalid_input_handler("Do you have any allergies?(yes/no)")
    if allergies == "yes" :
        al = invalid_input_handler("What are they?")
        ae = al.split()
    goals = invalid_input_handler("Do you have any goals?(yes/no)")
    if goals == "yes":
        gol = invalid_input_handler("what are they?")
    if goals == "no" :
        if BMI >= 18.5:
            print_pause("You are under weight")
            print_pause(f"Your suggested weight goal is {22(height^2)}")
        if BMI <= 26: 
            print_pause("You are overweight")   
            print_pause(f"Your suggested weight goals is {22(height^2)}")
        if 19 < BMI > 26 :
            print_pause("You are at a healthy weight")
            print_pause(f"Your suggested weight goals is {22(height^2)}")
            
