# Taken from online course

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 4  # 25
SHORT_BREAK_MIN = 2  # 5
LONG_BREAK_MIN = 3  # 20
TICK = "✓"
WORKING_TEXT = "Working"
IDLE_TEXT = "Timer"
SHORT_BREAK_TEXT = "Short Rest"
LONG_BREAK_TEXT = "Long Rest"


def countdown_start():
    if not counting:
        timer_label.config(text=WORKING_TEXT)
        countdown(WORK_MIN)


def countdown(counter):
    global wait_to_count, counting, check_label
    counting = 1
    minutes = math.floor(math.modf(counter)[1])
    seconds = math.floor(math.modf(counter)[0] * 60)
    if counter <= 1 / 60:
        if timer_label.cget("text") == WORKING_TEXT:
            label_text = check_label.cget("text")
            label_text += TICK
            check_label.config(text=label_text)
            if len(label_text) < 4:
                counter = SHORT_BREAK_MIN
                timer_label.config(text=SHORT_BREAK_TEXT)
            else:
                counter = LONG_BREAK_MIN
                timer_label.config(text=LONG_BREAK_TEXT)
        elif timer_label.cget("text") == SHORT_BREAK_TEXT:
            counter = WORK_MIN
            timer_label.config(text=WORKING_TEXT)
        elif timer_label.cget("text") == LONG_BREAK_TEXT:
            counter = WORK_MIN
            timer_label.config(text=WORKING_TEXT)
            check_label.config(text="")

    if seconds < 10:  # counter < 5/60:
        new_time = f"{minutes}:0{seconds}"
    else:
        new_time = f"{minutes}:{seconds}"
    canvas.itemconfig(counter_text, text=new_time)
    wait_to_count = window.after(1000, countdown, counter - 1 / 60)


def reset_procedure():
    global counting
    if counting:
        window.after_cancel(wait_to_count)
        canvas.itemconfig(counter_text, text=f"{WORK_MIN}:00")
        counting = 0
        check_label.config(text="")
        timer_label.config(text=IDLE_TEXT)
    else:
        pass


# ---------------------------- UI SETUP ------------------------------- #
counting = 0  # Variable that tracks if it is counting or not
window = Tk()
window.title = "Pomodoro Technique Manager"
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=300, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 112, image=tomato_img)
counter_text = canvas.create_text(150, 130, text=f"{WORK_MIN}:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Timer label
timer_label = Label(text=IDLE_TEXT, font=(FONT_NAME, 40, "bold"))
timer_label.config(fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# Start button
start_but = Button(text="Start", bg=PINK, command=countdown_start)
start_but.grid(row=3, column=0)

# Reset button
reset_but = Button(text="Reset", bg=PINK, command=reset_procedure)
reset_but.grid(row=3, column=2)

# Check mark label
check_label = Label(text="", font=(FONT_NAME, 20, "bold"))
check_label.config(fg=GREEN, bg=YELLOW)
check_label.grid(row=4, column=1)

window.mainloop()
