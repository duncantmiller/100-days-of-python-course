import tkinter as tk
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def work_seconds():
    """calculate work seconds"""

    return WORK_MIN * 60

def short_break_seconds():
    """calculate short break seconds"""

    return SHORT_BREAK_MIN * 60

def long_break_min():
    """calculate long break seconds"""

    return LONG_BREAK_MIN * 60

def countdown_time(reps):
    """figures out time based on what stage we are in"""

    if reps % 8 == 0:
        return long_break_min()
    elif reps % 2 == 0:
        return short_break_seconds()
    else:
        return work_seconds()


def start_timer(reps=0):
    """starts the timer and keeps track of reps"""

    reps += 1
    count_down(countdown_time(reps), reps)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count, reps):
    """count down mechanism"""

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        count -= 1
        window.after(1000, count_down, count, reps)
    else:
        start_timer(reps)

# ---------------------------- UI SETUP ------------------------------- #

timer_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 60))
timer_label.grid(column=1, row=0)
timer_label.grid(column=1, row=0)
image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", bg=YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_label = tk.Label(text="✓", bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()
