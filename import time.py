import time


def invalid_input_handler(prompt, valid_options=None):
    """Prompt the user until they enter a valid option.

    Args:
        prompt (str): The input prompt to show the user.
        valid_options (list, optional): A list of valid options. Defaults to None.

    Returns:
        str: The valid user input.
    """
    while True:
        choice = input(prompt).strip().lower()
        if valid_options:
            if choice in valid_options:
                return choice
            else:
                print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")
        else:
            try:
                return int(choice)
            except ValueError:
                print("Invalid input. Please enter a number.")


def print_pause(message, pause=2):
    """Prints a message and then pauses for a given duration.

    Args:
        message (str): The message to print.
        pause (int): The duration to wait after printing the message.
    """
    print(message)
    time.sleep(pause)


def display_diet_plan(age, BMI, has_allergies):
    if age < 18:
        print_pause("Your diet plan (for under 18):")
        print("Breakfast:")
        print_pause("Whole Grain Cereal with Milk: A bowl of whole-grain cereal with milk and a piece of fruit.")
        print_pause("Smoothie: Blend milk or a milk alternative with a banana, berries, and spinach.")
        print("Lunch:")
        print_pause("Grilled Chicken Sandwich: Whole-grain bread with grilled chicken, lettuce, and tomato.")
        print_pause("Veggie Sticks: Carrot and cucumber sticks with hummus.")
        print("Dinner:")
        print_pause("Spaghetti with Meat Sauce: Whole-grain spaghetti with a homemade meat sauce and a side of steamed broccoli.")
        print("Snacks:")
        print_pause("Yogurt with Fruit: A serving of yogurt with fresh fruit.")
        print_pause("Whole Grain Crackers with Cheese: A few whole-grain crackers with slices of cheese.")
    elif has_allergies:
        print_pause("Your diet plan (for those with allergies):")
        print("Breakfast:")
        print_pause("Gluten-Free Oatmeal: Cook 1 cup of gluten-free oats with a milk alternative. Add fruit and nuts.")
        print("Lunch:")
        print_pause("Quinoa Salad: Mix cooked quinoa with vegetables like bell peppers, cucumbers, and cherry tomatoes. Dress with olive oil and lemon.")
        print("Dinner:")
        print_pause("Baked Chicken with Sweet Potatoes: Baked chicken breast with roasted sweet potatoes and a side of green beans.")
        print("Snacks:")
        print_pause("Fruit Smoothie: Blend a milk alternative with fruits like bananas, berries, and a spoonful of nut butter.")
        print_pause("Vegetable Sticks: Carrot, cucumber, and bell pepper sticks with hummus.")
    elif BMI < 18.5:
        print_pause("Your diet plan (for underweight):")
        print("Breakfast:")
        print_pause("Oatmeal with Nuts and Fruit: Cook 1 cup of oats with milk or a milk alternative. Top with a handful of almonds or walnuts and fresh fruit.")
        print("Lunch:")
        print_pause("Chicken or Turkey Wrap: Whole-grain tortilla with grilled chicken or turkey, mixed greens, and avocado.")
        print("Dinner:")
        print_pause("Salmon or Chicken Breast: Baked or grilled salmon or chicken breast with sweet potato and steamed vegetables.")
        print("Snacks:")
        print_pause("Greek Yogurt with Honey and Granola: Greek yogurt topped with honey and granola.")
        print_pause("Trail Mix: A small handful of mixed nuts, dried fruit, and dark chocolate chips.")
    elif 18.5 <= BMI <= 24.9:
        print_pause("Your diet plan (for healthy weight):")
        print("Breakfast:")
        print_pause("Whole-Grain Toast with Avocado: Whole-grain toast topped with mashed avocado and a poached egg.")
        print("Lunch:")
        print_pause("Grilled Chicken Salad: Mixed greens with grilled chicken, cherry tomatoes, cucumber, and a light vinaigrette.")
        print("Dinner:")
        print_pause("Baked Fish with Quinoa: Baked fish fillet with a side of quinoa and steamed broccoli.")
        print("Snacks:")
        print_pause("Fruit and Nut Butter: Apple slices with almond or peanut butter.")
        print_pause("Vegetable Sticks: Carrot and celery sticks with hummus.")
    else:
        print_pause("Your diet plan (for overweight):")
        print("Breakfast:")
        print_pause("Green Smoothie: Blend spinach, kale, green apple, banana, and a milk alternative.")
        print("Lunch:")
        print_pause("Vegetable Soup: A bowl of vegetable soup with a side of whole-grain bread.")
        print("Dinner:")
        print_pause("Grilled Chicken with Vegetables: Grilled chicken breast with a side of steamed vegetables and a small portion of brown rice.")
        print("Snacks:")
        print_pause("Greek Yogurt with Berries: Greek yogurt topped with fresh berries.")
        print_pause("Mixed Nuts: A small handful of mixed nuts.")


def display_workout_plan(age, BMI):
    if age < 18:
        print_pause("Your workout plan (for under 18):")
        print("1. Cardiovascular Exercise: 30 minutes of running, cycling, or swimming, 3-5 times a week.")
        print("2. Strength Training: Bodyweight exercises like push-ups, squats, and planks, 2-3 times a week.")
        print("3. Flexibility: Stretching exercises or yoga, 2-3 times a week.")
    elif BMI < 18.5:
        print_pause("Your workout plan (for underweight):")
        print("1. Strength Training: Focus on weightlifting exercises such as squats, deadlifts, bench presses, and rows, 3-4 times a week.")
        print("2. Cardiovascular Exercise: Light cardio like walking or swimming, 2-3 times a week.")
        print("3. Flexibility: Stretching exercises or yoga, 2-3 times a week.")
    elif 18.5 <= BMI <= 24.9:
        print_pause("Your workout plan (for healthy weight):")
        print("1. Cardiovascular Exercise: 30 minutes of moderate to intense cardio, such as running, cycling, or swimming, 3-5 times a week.")
        print("2. Strength Training: A mix of weightlifting and bodyweight exercises, 2-3 times a week.")
        print("3. Flexibility: Stretching exercises or yoga, 2-3 times a week.")
    else:
        print_pause("Your workout plan (for overweight):")
        print("1. Cardiovascular Exercise: 45 minutes of low-impact cardio, such as brisk walking, cycling, or swimming, 5 times a week.")
        print("2. Strength Training: Light to moderate weightlifting exercises, 2-3 times a week.")
        print("3. Flexibility: Stretching exercises or yoga, 3-4 times a week.")


def Fit_Fusion():
    print("Welcome to Fit fusion")
    print_pause("Please enter your profile information.")
    age = invalid_input_handler("Please enter your age: ")
    height = invalid_input_handler("Please enter your height (cm): ")
    weight = invalid_input_handler("Please enter your weight (kg): ")
    BMI = weight / ((height / 100) ** 2)

    allergies = invalid_input_handler("Do you have any allergies? (yes/no): ", ["yes", "no"])
    if allergies == "yes":
        al = input("What are they? ").strip()
        ae = al.split()
    
    goals = invalid_input_handler("Do you have any goals? (yes/no): ", ["yes", "no"])
    if goals == "yes":
        gol = input("What are they? ").strip()
    elif goals == "no":
        if BMI < 18.5:
            print_pause("You are underweight")
            print_pause(f"Your suggested weight goal is {22 * (height / 100) ** 2:.2f} kg")
        elif BMI > 25:
            print_pause("You are overweight")
            print_pause(f"Your suggested weight goal is {22 * (height / 100) ** 2:.2f} kg")
        else:
            print_pause("You are at a healthy weight")
            print_pause(f"Your suggested weight goal is {22 * (height / 100) ** 2:.2f} kg")

    display_diet_plan(age, BMI, allergies == "yes")
    display_workout_plan(age, BMI)


# To start the program
Fit_Fusion()
