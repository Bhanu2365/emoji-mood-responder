mood_responses = {
    "happy": ("😊", "That's great to hear! Keep smiling!"),
    "sad": ("😢", "It's okay to feel sad. Better days are coming."),
    "angry": ("😠", "Take a deep breath. You're stronger than you think."),
    "excited": ("😄", "Woohoo! Enjoy the moment!"),
    "tired": ("😴", "Make sure to get some rest, you deserve it!"),
    "anxious": ("😰", "You're not alone. Take it one step at a time."),
}

user_mood = input("How are you feeling today? ").strip().lower()

if user_mood in mood_responses:
    emoji, message = mood_responses[user_mood]
    print(f"{emoji} {message}")
else:
    print("🤔 I'm not sure how that feels, but I'm here for you!")
    
    