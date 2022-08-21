import math
from tkinter import *
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
timer_lable = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_lable)
    canvas.itemconfig(timmer_text, text = "00:00")
    timer.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)  # floor(x) return the largest integer <= x.
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timmer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_lable
        timer_lable = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps / 2)
        for i in range(work_session):
            mark += "✔"
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="Pomodoro/tomato.png")
canvas.create_image(100, 112, image= img)
timmer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer.grid(column=1, row=0)

start = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

checkmark = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark.grid(column=1, row=3)


window.mainloop()