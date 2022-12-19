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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    #window.after_cancel is used for stopping the timer
    window.after_cancel(timer)

    #reset the timer
    canvas.itemconfig(timer_count,text= "00:00")
    check_mark.config(text=" ")
    title.config(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    #get global variable to local variable by using global before a variable to access it as shown below
    global reps
    if reps == 8 or reps == 16 or reps == 24:
        count_down(LONG_BREAK_MIN * 60)
        reps += 1
        title.config(text = "Break", font=(FONT_NAME, 35, "bold"), bg= YELLOW, fg= RED)
        check_mark.config(text="✔", highlightthickness=0, bg=YELLOW, fg=GREEN)
    elif reps % 2 == 0 and (reps != 8 or reps != 16 or reps != 24):
        count_down(WORK_MIN * 60)
        reps += 1
        title.config(text="Work", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
        check_mark.config(text=" ")
    else:
        count_down(SHORT_BREAK_MIN * 60)
        reps += 1
        title.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)
        check_mark.config(text="✔", highlightthickness=0, bg=YELLOW, fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count /60)
    count_sec = count % 60

    # dynamic typing
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    #this function gets the time
    canvas.itemconfig(timer_count, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # window.after used to set timer for 1 second
        timer = window.after(1000, count_down, count-1)
    if count_sec == "00" and count_min == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro app")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text = "timer", font=(FONT_NAME, 35, "bold"), bg= YELLOW, fg= GREEN)
title.grid(column=1, row=0)


tomato_img = PhotoImage(file ="tomato.png")
canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness= 0)
canvas.create_image(100,112, image=tomato_img)
canvas.grid(column =1, row=1)
timer_count = canvas.create_text(103,130, text= "00:00", fill= "white", font=(FONT_NAME, 35, "bold"))

start_button = Button(text= "start", command=start_timer, highlightthickness = 0)
start_button.grid(column=0,row=2)

reset_button = Button(text= "Reset", command=reset_timer, highlightthickness = 0)
reset_button.grid(column=2, row=2)

check_mark = Label(text=" ",highlightthickness=0,bg=YELLOW, fg= GREEN)
check_mark.grid(column=1, row=3)

window.mainloop()