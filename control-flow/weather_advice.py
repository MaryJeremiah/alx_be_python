

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()


#provide clothing recommendations based on the weather conditions

if 'weather' =="sunny": # type: ignore
        print( "Wear a t-shirt and sunglasses.")
elif 'weather' == "rainny":
        print("Don't forget your umbrella and a raincoat.")
elif 'weather' == "cold": # type: ignore
        print("Make sure to wear a warm coat and a scarf.")
else:
        print("Sorry, I don't have recommendations for this weather.")