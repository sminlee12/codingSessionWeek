import random
import tkinter as tk

choices = ["Rock", "Paper", "Scissors"]
your_score = 0
computer_score = 0
round_num = 0

def play(your_choice):
    global your_score, computer_score, round_num

    if round_num >= 5 or your_score == 3 or computer_score == 3:
        return

    round_num += 1
    computer_choice = random.choice(choices)
    result_text = f"Round {round_num}\nYou chose {your_choice}. Computer chose {computer_choice}.\n"

    if your_choice == computer_choice:
        result_text += "It's a tie!"
    elif (
        (your_choice == "Rock" and computer_choice == "Scissors")
        or (your_choice == "Paper" and computer_choice == "Rock")
        or (your_choice == "Scissors" and computer_choice == "Paper")
    ):
        your_score += 1
        result_text += "You win this round!"
    else:
        computer_score += 1
        result_text += "The computer wins this round!"

    result_label.config(text=result_text)
    score_label.config(text=f"You: {your_score}   Computer: {computer_score}")

    if your_score == 3:
        finish_game("You are the winner!")
    elif computer_score == 3:
        finish_game("The computer is the winner!")
    elif round_num == 5:
        if your_score > computer_score:
            finish_game("You are the winner!")
        elif computer_score > your_score:
            finish_game("The computer is the winner!")
        else:
            finish_game("The game is a tie!")

def finish_game(message):
    result_label.config(text=result_label.cget("text") + f"\n\n{message}")
    for button in choice_buttons:
        button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("380x300")

instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
instruction_label.pack(pady=15)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)
choice_buttons = []
for choice in choices:
    button = tk.Button(button_frame, text=choice, width=10, command=lambda c=choice: play(c))
    button.pack(side=tk.LEFT, padx=4)
    choice_buttons.append(button)

score_label = tk.Label(root, text="You: 0   Computer: 0", font=("Arial", 12))
score_label.pack(pady=12)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="center", wraplength=340)
result_label.pack(pady=8)

root.mainloop()
