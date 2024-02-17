from tkinter import *
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
checks = ''
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, checks, reps
    timer_label.config(text="Pomodoro Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=(f"00:00"))
    checks = ''
    check_label.config(text=checks)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, checks
    reps += 1
    # WHY DOESN'T A FRIGIN WHILE LOOP WORK HERE???
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(fg=RED, text='better work BITCH')

        count_down(60 * WORK_MIN)

    elif reps == 2 or reps == 4 or reps == 6:
        checks += "✔"
        check_label.config(text=checks)

        timer_label.config(fg=PINK, text='Quick Rest')
        count_down(60 * SHORT_BREAK_MIN)

    elif reps == 8:
        checks += "✔"
        check_label.config(text=checks)
        timer_label.config(fg=GREEN, text='Long Recharge')

        count_down(60 * LONG_BREAK_MIN)
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=(f"{count_min}:{count_sec}"))

    if count > 0:
        timer = window.after(1, count_down, count - 1)

    else:

        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")

timer_label = Label(text="Pomodoro Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2, )

check_label = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
check_label.grid(row=3, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # Highlight thickness gets rid of border
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
