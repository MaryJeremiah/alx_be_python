#provide clothing recommendations based on the weather conditions
if 'weather' =="sunny": # type: ignore
        print( "Wear a t-shirt and sunglasses.")
elif 'weather' == "rainny":
        print("Don't forget your umbrella and a raincoat.")
elif 'weather' == "cold": # type: ignore
        print("Make sure to wear a warm coat and a scarf.")
else:
        print("Sorry, I don't have recommendations for this weather.")