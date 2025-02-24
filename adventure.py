import tkinter as tk
import random

def generate_question():
    global num1, num2, correct_answer
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 + num2
    update_text(f"Solve: {num1} + {num2} = ?")

def check_answer():
    global rabbit_position, score
    try:
        user_answer = int(answer_entry.get())
        if user_answer == correct_answer:
            rabbit_position += 2  # Move forward if correct
            score += 1
            update_text("✅ Correct! The rabbit moves forward.")
            show_success_message()
        else:
            update_text("❌ Wrong! The rabbit stays in place.")
        answer_entry.delete(0, tk.END)
        check_progress()
    except ValueError:
        update_text("⚠️ Please enter a valid number.")

def show_success_message():
    success_label.config(text="🎉 Great job! Keep going!", fg="green")
    root.after(1000, lambda: success_label.config(text=""))  # Remove message after 1 sec

def check_progress():
    if rabbit_position >= 20:
        update_text("🎊 Congratulations! The rabbit reached the destination.")
        update_buttons([("Play Again", restart_game), ("Exit", root.quit)])
    else:
        generate_question()

def restart_game():
    global rabbit_position, score
    rabbit_position = 0
    score = 0
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    text_area.config(state=tk.DISABLED)
    update_text("Solve math problems to help the rabbit reach its goal!")
    generate_question()
    update_buttons([("Submit Answer", check_answer)])
    success_label.config(text="")

def update_text(new_text):
    text_area.config(state=tk.NORMAL)
    text_area.insert(tk.END, new_text + "\n")
    text_area.config(state=tk.DISABLED)
    text_area.see(tk.END)

def update_buttons(options):
    for widget in button_frame.winfo_children():
        widget.destroy()
    for text, command in options:
        button = tk.Button(button_frame, text=text, command=command, width=20)
        button.pack(pady=5)

# Create UI
root = tk.Tk()
root.title("Math Rabbit Game")
root.geometry("500x300")

text_area = tk.Text(root, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED)
text_area.pack(pady=10)

answer_entry = tk.Entry(root, width=10)
answer_entry.pack()

success_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
success_label.pack()

button_frame = tk.Frame(root)
button_frame.pack()

restart_game()
root.mainloop()
