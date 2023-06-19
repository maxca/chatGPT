import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")

        self.target_number = random.randint(1, 100)
        self.num_guesses = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Guess", command=self.check_guess)
        self.button.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.num_guesses += 1

        if guess < self.target_number:
            messagebox.showinfo("Result", "Too low! Try again.")
        elif guess > self.target_number:
            messagebox.showinfo("Result", "Too high! Try again.")
        else:
            messagebox.showinfo("Result", f"Correct! You guessed the number in {self.num_guesses} attempts.")
            self.master.destroy()

# Create the tkinter window
window = tk.Tk()

# Create an instance of the GuessingGame class
game = GuessingGame(window)

# Run the tkinter event loop
window.mainloop()
