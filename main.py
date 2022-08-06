import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
operating = False

window = tk.Tk()
window.title("Pomodoro Clock")
window.config(padx=100, pady=50, bg=YELLOW)

def counter(count):
    count_minute = math.floor(count/60)
    count_second = count % 60

    if count_second < 10:
        count_second = f"0{count_second}"
    global timer
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        timer = window.after(1000, counter, count-1)
    else:
        start()
        checkmarks.config(text=reps//2 * "✔")

def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    checkmarks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global operating
    operating = False

def start():
    global operating
    if operating:
        reset()

    operating = True
        
    global reps
    reps += 1

    if reps == 8:
        seconds = 60 * LONG_BREAK_MIN
        label1.config(text="Break", fg=RED)
    elif reps % 2 == 1:
        seconds = 60 * WORK_MIN
        label1.config(text="Work", fg=GREEN)
    else:
        seconds = 60 * SHORT_BREAK_MIN
        label1.config(text="Break", fg=PINK)

    counter(seconds)

def add_check(label):
    print("✔")


canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_file = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_file)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

label1 = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW, highlightthickness=0)
label1.grid(column=1,row=0)

reset_button = tk.Button(text="Reset", command=reset, highlightthickness=0, bg=YELLOW)
reset_button.grid(column=2, row=2)

start_button = tk.Button(text='Start', command=start, highlightthickness=0, bg=YELLOW)
start_button.grid(column=0, row=2)
checkmarks = tk.Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=2)

window.mainloop()
