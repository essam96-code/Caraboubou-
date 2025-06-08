# This is the main entry point for the calorie calculator application.
# It will contain the application's logic.

def calculate_bmi(weight_kg, height_m):
    """Calculates Body Mass Index (BMI)."""
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    return weight_kg / (height_m ** 2)

def calculate_bmr(weight_kg, height_cm, age_years, gender):
    """
    Calculates Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation.
    Gender should be 'male' or 'female'.
    """
    if gender.lower() == 'male':
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years) + 5
    elif gender.lower() == 'female':
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years) - 161
    else:
        raise ValueError("Gender must be 'male' or 'female'.")
    return bmr

def calculate_tdee(bmr, activity_level_str):
    """
    Calculates Total Daily Energy Expenditure (TDEE).
    activity_level_str should be one of: 'sedentary', 'lightly active',
    'moderately active', 'very active', 'super active'.
    """
    activity_multipliers = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'super active': 1.9
    }
    activity_level_str = activity_level_str.lower().strip()
    if activity_level_str not in activity_multipliers:
        raise ValueError(
            "Invalid activity level. Choose from: 'sedentary', 'lightly active', "
            "'moderately active', 'very active', 'super active'."
        )
    return bmr * activity_multipliers[activity_level_str]

def add_food_item(log, name, calories):
    """Adds a food item to the log."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Food name must be a non-empty string.")
    if not isinstance(calories, (int, float)) or calories < 0:
        raise ValueError("Calories must be a non-negative number.")
    log.append({'name': name.strip(), 'calories': calories})
    print(f"Added {name.strip()}: {calories} calories.")

def calculate_total_consumed_calories(log):
    """Calculates the total consumed calories from the log."""
    total_calories = 0
    for item in log:
        total_calories += item['calories']
    return total_calories

def main():
    print("Welcome to the Calorie Calculator!")
    food_log = []

    try:
        weight_kg = float(input("Enter your weight in kilograms: "))
        height_cm = float(input("Enter your height in centimeters: "))
        age_years = int(input("Enter your age in years: "))
        gender = input("Enter your gender ('male' or 'female'): ").strip()

        if weight_kg <= 0 or height_cm <= 0 or age_years <= 0:
            print("Weight, height, and age must be positive values.")
            return

        height_m = height_cm / 100
        bmi = calculate_bmi(weight_kg, height_m)
        bmr = calculate_bmr(weight_kg, height_cm, age_years, gender)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Your BMR is: {bmr:.2f} calories/day")

        print("\nSelect your activity level:")
        print("1. Sedentary (little or no exercise)")
        print("2. Lightly active (light exercise/sports 1-3 days/week)")
        print("3. Moderately active (moderate exercise/sports 3-5 days/week)")
        print("4. Very active (hard exercise/sports 6-7 days a week)")
        print("5. Super active (very hard exercise/physical job & exercise 2x/day)")

        activity_level_input = input("Enter your activity level (e.g., 'sedentary' or '1'): ").strip()

        activity_level_map = {
            "1": "sedentary", "sedentary": "sedentary",
            "2": "lightly active", "lightly active": "lightly active",
            "3": "moderately active", "moderately active": "moderately active",
            "4": "very active", "very active": "very active",
            "5": "super active", "super active": "super active"
        }

        activity_level_str = activity_level_map.get(activity_level_input.lower())

        if not activity_level_str:
            print("Invalid activity level selection.")
            return

        tdee = calculate_tdee(bmr, activity_level_str)
        print(f"Your estimated TDEE is: {tdee:.2f} calories/day")

        # Food logging loop
        while True:
            print("\nFood Log Menu:")
            print("1. Add food item")
            print("2. View total consumed calories")
            print("3. View remaining calories")
            print("4. Exit food logging")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == '1':
                try:
                    food_name = input("Enter food item name: ")
                    food_calories = float(input(f"Enter calories for {food_name}: "))
                    add_food_item(food_log, food_name, food_calories)
                except ValueError as e:
                    print(f"Error adding food item: {e}")
            elif choice == '2':
                total_consumed = calculate_total_consumed_calories(food_log)
                print(f"Total consumed calories: {total_consumed:.2f}")
            elif choice == '3':
                total_consumed = calculate_total_consumed_calories(food_log)
                remaining_calories = tdee - total_consumed
                print(f"Remaining calories for the day: {remaining_calories:.2f}")
            elif choice == '4':
                print("Exiting food logging. Final summary:")
                total_consumed = calculate_total_consumed_calories(food_log)
                remaining_calories = tdee - total_consumed
                print(f"Total TDEE: {tdee:.2f} calories/day")
                print(f"Total Consumed Calories: {total_consumed:.2f}")
                print(f"Net Remaining Calories: {remaining_calories:.2f}")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
