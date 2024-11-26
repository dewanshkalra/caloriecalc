
def calculate_bmr(age, gender, weight, height):
    """Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation."""
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Gender must be 'male' or 'female'.")
    return bmr

def calculate_calories(bmr, activity_level):
    """Adjust BMR based on activity level."""
    activity_multipliers = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725,
        "super active": 1.9
    }
    return bmr * activity_multipliers.get(activity_level.lower(), 1.2)

def main():
    print("Calorie Calculator")
    try:
        age = int(input("Enter your age (in years): "))
        gender = input("Enter your gender (male/female): ").strip()
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in cm): "))
        
        print("\nActivity Levels:")
        print("1. Sedentary (little or no exercise)")
        print("2. Lightly active (light exercise/sports 1-3 days a week)")
        print("3. Moderately active (moderate exercise/sports 3-5 days a week)")
        print("4. Very active (hard exercise/sports 6-7 days a week)")
        print("5. Super active (very hard exercise, physical job or twice-a-day training)")
        
        activity_map = {
            "1": "sedentary",
            "2": "lightly active",
            "3": "moderately active",
            "4": "very active",
            "5": "super active"
        }
        
        activity_choice = input("Choose your activity level (1-5): ").strip()
        activity_level = activity_map.get(activity_choice, "sedentary")
        
        bmr = calculate_bmr(age, gender, weight, height)
        calories = calculate_calories(bmr, activity_level)
        
        print(f"\nYour BMR (Basal Metabolic Rate): {bmr:.2f} calories/day")
        print(f"Your daily calorie needs based on activity level: {calories:.2f} calories/day")
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
