import time
import random

# This dictionary will store user data including progress tracking
user_data = {
    "user_name": "",
    "password": "",
    "age": 0,
    "height": 0,
    "weights": [],  # List to store weights over time
    "BMIs": [],     # List to store BMIs over time
    "allergies": [],
    "goals": "",
    "custom_workout": [],
}

def invalid_input_handler(prompt, valid_options=None):
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
    print(message)
    time.sleep(pause)

def display_diet_plan(age, BMI, has_allergies):
    if age >= 18:
        if BMI < 18.5:
            print("You are underweight. Here is a diet plan to help you gain weight:")
        elif BMI > 25:
            print("You are overweight. Here is a diet plan to help you lose weight:")
        else:
            print("You are at a healthy weight. Here is a diet plan to maintain your weight:")
        
        if has_allergies:
            print("Diet plan considering your allergies:")
            # Customize diet plan based on allergies
        else:
            # Regular diet plan
            print("Your diet plan without considering allergies.")

    else:
        if BMI < 18.5:
            print("You are underweight. Here is a diet plan to help you gain weight:")
        elif BMI > 25:
            print("You are overweight. Here is a diet plan to help you lose weight:")
        else:
            print("You are at a healthy weight. Here is a diet plan to maintain your weight:")
        
        if has_allergies:
            print("Diet plan considering your allergies:")
            # Customize diet plan based on allergies
        else:
            # Regular diet plan
            print("Your diet plan without considering allergies.")

def display_workout_plan(age, BMI):
    if age >= 18:
        if BMI < 18.5:
            print("Workout plan for underweight adults:")
        elif BMI > 25:
            print("Workout plan for overweight adults:")
        else:
            print("Workout plan for healthy weight adults:")
    else:
        if BMI < 18.5:
            print("Workout plan for underweight minors:")
        elif BMI > 25:
            print("Workout plan for overweight minors:")
        else:
            print("Workout plan for healthy weight minors:")

def display_progress(user_data):
    print("\nProgress Tracking:")
    if user_data["weights"]:
        for i, (weight, bmi) in enumerate(zip(user_data["weights"], user_data["BMIs"])):
            print(f"Entry {i+1}: Weight = {weight} kg, BMI = {bmi:.2f}")
    else:
        print("No progress data available.")

def create_custom_workout():
    w = invalid_input_handler("Do you want to create a custom work out plan?",[valid_options=])
    if w == "yes" :
        print_pause("Let's create your custom workout plan!")
        workout_plan = []
        while True:
            exercise = input("Enter an exercise (or 'done' to finish): ").strip()
            if exercise.lower() == 'done':
                break
        sets = invalid_input_handler("How many sets of this exercise? ")
        reps = invalid_input_handler("How many reps per set? ")
        workout_plan.append({"exercise": exercise, "sets": sets, "reps": reps})  
        print_pause("Your custom workout plan:")
        for i, workout in enumerate(workout_plan):
            print(f"{i + 1}. {workout['exercise']}: {workout['sets']} sets of {workout['reps']} reps")
        return workout_plan
    elif w == "no":
            if user_data["age"] < 18:
                print_pause("Your workout plan (for under 18):")
                print("1. Cardiovascular Exercise: 30 minutes of running, cycling, or swimming, 3-5 times a week.")
                print("2. Strength Training: Bodyweight exercises like push-ups, squats, and planks, 2-3 times a week.")
                print("3. Flexibility: Stretching exercises or yoga, 2-3 times a week.")
            elif user_data["BMIs"] < 18.5:
                print_pause("Your workout plan (for underweight):")
                print("1. Strength Training: Focus on weightlifting exercises such as squats, deadlifts, bench presses, and rows, 3-4 times a week.")
                print("2. Cardiovascular Exercise: Light cardio like walking or swimming, 2-3 times a week.")
                print("3. Flexibility: Stretching exercises or yoga, 2-3 times a week.")
            elif 18.5 <= user_data["BMIs"] <= 24.9:
                print_pause("Your workout plan (for healthy weight):")
                print("1. Cardiovascular Exercise: 30 minutes of moderate to intense cardio, such as running, cycling, or swimming, 3-5 times a week.")
                print("2. Strength Training: A mix of weightlifting and bodyweight exercises, 2-3 times a week.")
                print("3. Flexibility: Stretching exercises or yoga, 2-3 times a week.")
            else:
                print_pause("Your workout plan (for overweight):")
                print("1. Cardiovascular Exercise: 45 minutes of low-impact cardio, such as brisk walking, cycling, or swimming, 5 times a week.")
                print("2. Strength Training: Light to moderate weightlifting exercises, 2-3 times a week.")
                print("3. Flexibility: Stretching exercises or yoga, 3-4 times a week.")


def daily_health_tip():
    tips = [
        "Drink plenty of water throughout the day to stay hydrated.",
        "Incorporate a variety of vegetables into your diet for optimal nutrition.",
        "Take short breaks and stretch regularly if you sit for long periods.",
        "Aim for at least 7-8 hours of sleep each night.",
        "Practice mindfulness or meditation to reduce stress and improve mental health.",
        "Include healthy fats like avocados, nuts, and olive oil in your diet.",
        "Engage in regular physical activity to maintain overall health."
    ]
    tip = random.choice(tips)
    print_pause(f"Daily Health Tip: {tip}")

def Fit_Fusion():
    acc = invalid_input_handler("Want to sign up? (yes/no): ", ["yes", "no"])
    if acc == "yes":
        user_data["user_name"] = input("Please enter your user name: ").strip()
        user_data["password"] = input("Please enter your password: ").strip()

    print_pause("Please enter your profile information.")
    user_data["age"] = invalid_input_handler("Please enter your age: ")
    user_data["height"] = invalid_input_handler("Please enter your height (cm): ")
    weight = invalid_input_handler("Please enter your weight (kg): ")
    user_data["weights"].append(weight)
    BMI = weight / ((user_data["height"] / 100) ** 2)
    user_data["BMIs"].append(BMI)

    allergies = invalid_input_handler("Do you have any allergies? (yes/no): ", ["yes", "no"])
    if allergies == "yes":
        al = input("What are they? ").strip()
        user_data["allergies"] = al.split()

    goals = invalid_input_handler("Do you have any goals? (yes/no): ", ["yes", "no"])
    if goals == "yes":
        user_data["goals"] = input("What are they? ").strip()
    elif goals == "no":
        if BMI < 18.5:
            print_pause("You are underweight")
            print_pause(f"Your suggested weight goal is {22 * (user_data['height'] / 100) ** 2:.2f} kg")
        elif BMI > 25:
            print_pause("You are overweight")
            print_pause(f"Your suggested weight goal is {22 * (user_data['height'] / 100) ** 2:.2f} kg")
        else:
            print_pause("You are at a healthy weight")
            print_pause(f"Your suggested weight goal is {22 * (user_data['height'] / 100) ** 2:.2f} kg")

    display_diet_plan(user_data["age"], BMI, allergies == "yes")
    display_workout_plan(user_data["age"], BMI)
    display_progress(user_data)
    
    user_data["custom_workout"] = create_custom_workout()
    print_pause("Your custom workout plan has been saved.")
    daily_health_tip()


# To start the program
Fit_Fusion()
