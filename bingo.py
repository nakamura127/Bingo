import tkinter as tk
import random

def pick_number():
    if remaining_numbers:
        picked_number = random.choice(remaining_numbers)
        remaining_numbers.remove(picked_number)
        picked_numbers.append(picked_number)
        label.config(text=f"Picked Number: {picked_number}")
        # 10個ごとに改行
        formatted_history = '\n'.join([', '.join(map(str, picked_numbers[i:i+10])) for i in range(0, len(picked_numbers), 10)])
        history_label.config(text=formatted_history)

root = tk.Tk()
root.title("Bingo System")

remaining_numbers = list(range(1, 76))
picked_numbers = []

label = tk.Label(root, text="ボタンを押してください", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="番号を選択", command=pick_number, font=("Arial", 14))
button.pack(pady=10)

history_label = tk.Label(root, text="", font=("Arial", 12))
history_label.pack()

root.mainloop()
