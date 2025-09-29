# weather_advice.py
# Objective: Utilize conditional statements to guide program execution 
# based on user input regarding weather conditions.

# Prompt user for input
user_question = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide clothing recommendations
if user_question == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user_question == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif user_question == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
