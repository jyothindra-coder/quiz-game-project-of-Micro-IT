import tkinter as tk
from tkinter import messagebox
import requests
import html
import random
import threading
from playsound import playsound

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Quiz Game")
        self.root.geometry("500x350")

        self.questions = []
        self.current_question = 0
        self.score = 0
        self.selected_option = tk.StringVar()

        self.create_widgets()
        self.fetch_questions()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=450, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.selected_option, value="", font=("Arial", 12))
            rb.pack(anchor='w', padx=50)
            self.options.append(rb)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=20)

        # Hover effect on Next button
        self.next_button.bind("<Enter>", lambda e: self.next_button.config(bg="lightblue"))
        self.next_button.bind("<Leave>", lambda e: self.next_button.config(bg="SystemButtonFace"))

    def fetch_questions(self):
        try:
            url = "https://opentdb.com/api.php?amount=5&type=multiple"
            response = requests.get(url)
            data = response.json()

            for item in data['results']:
                question = html.unescape(item['question'])
                correct = html.unescape(item['correct_answer'])
                incorrect = [html.unescape(ans) for ans in item['incorrect_answers']]
                options = incorrect + [correct]
                random.shuffle(options)

                self.questions.append({
                    "question": question,
                    "options": options,
                    "answer": correct
                })

            self.load_question()
            self.next_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch questions.\n{e}")
            self.root.destroy()

    def animate_label(self, label, text):
        label.config(text="")
        for i in range(len(text) + 1):
            self.root.after(i * 30, lambda i=i: label.config(text=text[:i]))

    def play_correct_sound(self):
        threading.Thread(target=lambda: playsound("correct.wav", block=False)).start()

    def play_wrong_sound(self):
        threading.Thread(target=lambda: playsound("wrong.wav", block=False)).start()

    def load_question(self):
        q = self.questions[self.current_question]
        self.animate_label(self.question_label, q["question"])
        self.selected_option.set(None)
        for i, option in enumerate(q["options"]):
            self.options[i].config(text=option, value=option)

    def next_question(self):
        if not self.selected_option.get():
            messagebox.showwarning("Select an option", "Please select an answer before continuing.")
            return

        if self.selected_option.get() == self.questions[self.current_question]["answer"]:
            self.score += 1
            self.play_correct_sound()
        else:
            self.play_wrong_sound()

        self.current_question += 1

        if self.current_question == len(self.questions):
            messagebox.showinfo("Quiz Completed", f"You scored {self.score} out of {len(self.questions)}!")
            self.root.destroy()
        else:
            self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
