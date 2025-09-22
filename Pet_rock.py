print("In the 1700s, there was a time of poverty. Since your family is unable to afford a pet, your parents gave you a magical pet rock (don't ask where they got it).")
rock_name = input("What would you name your pet rock? ")

pet_rock = {
    "emotion": "happy",
    "health": 10,
    "hunger": 5
}

# --- 2. The Game Loop ---
while True:
    print(f"\n--- Your Pet Rock, {rock_name} ---")
    print(f"**Emotions:** {pet_rock['emotion'].capitalize()} ")
    print(f"**Health:** {pet_rock['health']}/10 ")
    print(f"**Hunger:** {pet_rock['hunger']}/10 🍽️")

    # --- 3. Game-Over Conditions ---
    negative_emotions = ["anxiety", "angry", "hurt"]
    if pet_rock['emotion'] in negative_emotions:
        print("\nIt's game over, and you will be doomed to be lonely forever.")
        break
    if pet_rock['hunger'] >= 10:
        print("\nGame over. The rock has disappeared because of your stupidity.")
        break
    if pet_rock['health'] <= 0:
        print("\nHealth is less than or equal to 0. Game over. The rock has lost all its energy and crumbled to dust. ")
        break

    # --- 4. Handle User Input and Consequences ---
    print(f"\nWhat do you want to do with your pet rock, {rock_name}?")
    print("1. Have fun and play with it")
    print("2. Feed it")
    print("3. Do nothing and just stare")
    print("4. Ignore it")
    print("5. Bully the pet")
    choice = input("Your choice: ")

    if choice == '1':
        print(f"\nYou and {rock_name} had a lot of fun, but it's hungry now. Would you feed it?")
        pet_rock['emotion'] = "happy"
        pet_rock['hunger'] = min(10, pet_rock['hunger'] + 1)
        
        feed_choice = input("Yes or no: ")
        if feed_choice.lower() == 'yes':
            pet_rock['hunger'] = max(0, pet_rock['hunger'] - 2)
            pet_rock['emotion'] = "fulfilled"
            print(f"You fed {rock_name} and it's fulfilled now. 😊")
        else:
            print(f"You didn't feed {rock_name}. The rock is still hungry.")
    elif choice == '2':
        print(f"\nYou feed {rock_name} a pebble. 😋")
        pet_rock['hunger'] = max(0, pet_rock['hunger'] - 2)
        # The document states "Same again with the question 'what do you want to do with your pet'",
        # which is handled by the loop restarting.
    elif choice == '3':
        print(f"\nYou just stare at {rock_name}. It's getting sad. 😶")
        pet_rock['health'] = max(0, pet_rock['health'] - 2)
        pet_rock['emotion'] = "sad"
    elif choice == '4':
        print(f"\nYou ignore {rock_name}. Its emotion is now hurt. 💔")
        pet_rock['emotion'] = "hurt"
        pet_rock['health'] = max(0, pet_rock['health'] - 4)
    elif choice == '5':
        print(f"\nYou bully {rock_name}. Its emotion is now anger. 😡")
        pet_rock['emotion'] = "angry"
        pet_rock['health'] = max(0, pet_rock['health'] - 4)
        pet_rock['hunger'] = max(0, pet_rock['hunger'] - 4)
    else:
        print(f"\n{rock_name} looks confused by your choice. It's just a rock, after all. 🤷")

    # A short, passive state change to simulate time passing.
    # Hunger increases, and health decreases slightly regardless of the action.
    pet_rock['hunger'] = min(10, pet_rock['hunger'] + 1)
    pet_rock['health'] = max(0, pet_rock['health'] - 1)
    
print("\nGame over!")
