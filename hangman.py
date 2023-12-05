import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.wordlist = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
        self.word_to_guess = random.choice(self.wordlist).lower()
        self.guesses_left = 6
        self.current_word = ["_"] * len(self.word_to_guess)
        self.incorrect_guesses = []

        self.word_label = tk.Label(root, text=" ".join(self.current_word), font=("Helvetica", 20))
        self.word_label.pack(pady=20)

        self.input_frame = tk.Frame(root)
        self.input_frame.pack()

        self.input_label = tk.Label(self.input_frame, text="Type your answer:")
        self.input_label.grid(row=0, column=0)

        self.guess_entry = tk.Entry(self.input_frame, font=("Helvetica", 20))
        self.guess_entry.grid(row=0, column=1, padx=10, pady=10)

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack()

        self.info_label = tk.Label(root, text=f"Guesses left: {self.guesses_left}", font=("Helvetica", 16))
        self.info_label.pack()

        self.hangman_label = tk.Label(root, text="", font=("Courier", 14))
        self.hangman_label.pack()

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if guess in self.word_to_guess:
            for i in range(len(self.word_to_guess)):
                if self.word_to_guess[i] == guess:
                    self.current_word[i] = guess
        else:
            self.guesses_left -= 1
            self.incorrect_guesses.append(guess)

        self.word_label.config(text=" ".join(self.current_word))
        self.info_label.config(text=f"Guesses left: {self.guesses_left}")
        self.update_hangman()

        if "".join(self.current_word) == self.word_to_guess:
            self.info_label.config(text="You win! The word was: " + self.word_to_guess)
            self.submit_button.config(state=tk.DISABLED)
        elif self.guesses_left == 0:
            self.info_label.config(text="You lose! The word was: " + self.word_to_guess)
            self.submit_button.config(state=tk.DISABLED)

    def update_hangman(self):
        hangman_parts = [
            "  _____  \n |     | \n |     O \n |    /|\\\n |    / \\",
            "  _____  \n |     | \n |     O \n |    /|\\\n |    /",
            "  _____  \n |     | \n |     O \n |    /|\\\n |",
            "  _____  \n |     | \n |     O \n |    /|",
            "  _____  \n |     | \n |     O \n |    /",
            "  _____  \n |     | \n |     O \n |",
            "  _____  \n |     | \n |     O",
            "  _____  \n |     |",
            "  _____",
        ]

        if self.guesses_left < len(hangman_parts):
            self.hangman_label.config(text=hangman_parts[self.guesses_left])
        else:
            self.hangman_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()


