import emoji
import random

def story_genrator():
    # Define keywords for categories we care about
    character = [":black_cat:", ":dog_face:", ":mouse_face:", ":woman_red_hair:", ":man_curly_hair:"]
    vehicle = [":oncoming_taxi:", ":trolleybus:", "	:passenger_ship:", ":small_airplane:", "train"]
    place = ["	:hospital:", ":derelict_house:"]

    # Pick random emojis
    character_emoji = random.choice(character)
    vehicle_emoji = random.choice(vehicle)
    place_emoji = random.choice(place)

    # Filter emojis whose description contains our keywords
    story = f"A {emoji.emojize(character_emoji).strip()} going to {emoji.emojize(place_emoji).strip()} using {emoji.emojize(vehicle_emoji).strip()} ."

    ## generating story
    print(f"Story using Emoji:")
    print(story)

if __name__=='__main__':

    ## Asking user input
    user_input = input("Do you want to generate emoji story?:").lower()

    if user_input=="yes":
        story_genrator()
    else:
        print("Thanks for using Emoji story generator.")