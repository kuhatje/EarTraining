import tkinter
import random

# Create the display window, set title, set background colour, set size
root = tkinter.Tk()
root.title("Notes")
root.configure(bg="#2b2b2b")
root.geometry("250x200")

# List of possible notes, in order
notes = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]


# Function to generate the note given in the question label.
def generate_note_index():
    return random.randrange(0, 12)


# Generate the number of semitones given in the question label.
def generate_interval():
    return random.randrange(1, 12)


# Randomly select ascending or descending interval mode.
def generate_ascending_descending_mode():
    if random.randrange(0, 1) == 0:
        return "below"
    else:
        return "above"


# Generate the correct answer.
def generate_correct_note():
    correct_answer = str
    if current_above_below == "above":
        correct_answer_index = current_note_index + current_interval
        correct_answer = notes[correct_answer_index]
        while correct_answer_index > 11:
            correct_answer_index -= 12
            correct_answer = notes[correct_answer_index]
    elif current_above_below == "below":
        correct_answer_index = current_note_index - current_interval
        correct_answer = notes[correct_answer_index]
        while correct_answer_index < 0:
            correct_answer_index += 12
            correct_answer = notes[correct_answer_index]

    return correct_answer


# Cool Kids (variables that are generated with every question)
current_note_index = generate_note_index()
current_note = notes[current_note_index]
current_interval = generate_interval()
current_above_below = generate_ascending_descending_mode()
current_correct_note = generate_correct_note()


# Creates the initial question label and puts it on the window.
question_label = tkinter.Label

# Make the word 'semitone' plural if the current interval is greater than 1
if current_interval == 1:
    question_label = tkinter.Label(root, fg="white", bg="#2b2b2b", text="What note is " + str(current_interval) +
                                                                        " semitone " + current_above_below + " " +
                                                                        current_note + "?")
elif current_interval > 1:
    question_label = tkinter.Label(root, fg="white", bg="#2b2b2b",
                                   text="What note is " + str(current_interval) + " semitones "
                                        + current_above_below + " " + current_note + "?")

question_label.grid(row=0, column=1, columnspan=4, padx=5, pady=5)


# Create every new question after the initial one after 'Next>>' button is pressed.
def create_new_question():
    # The following variables will be changed within this function.
    global question_label
    global wrong_answer_label
    global correct_answer_label
    global current_note_index
    global current_note
    global current_interval
    global current_above_below
    global current_correct_note

    # Forgets the old question, old answer, and next button
    question_label.grid_forget()
    wrong_answer_label.grid_forget()
    correct_answer_label.grid_forget()
    next_question_button.grid_forget()

    # Regenerate the cool kids
    current_note_index = generate_note_index()
    current_note = notes[current_note_index]
    current_interval = generate_interval()
    current_above_below = generate_ascending_descending_mode()
    current_correct_note = generate_correct_note()

    # Make the word 'semitone' plural if the current interval is greater than 1
    if current_interval == 1:
        question_label = tkinter.Label(root, fg="white", bg="#2b2b2b",
                                       text="What note is " + str(current_interval) + " semitone "
                                            + current_above_below + " " + current_note + "?")
        question_label.grid(row=0, column=1, columnspan=4, padx=5, pady=5)
    elif current_interval > 1:
        question_label = tkinter.Label(root, fg="white", bg="#2b2b2b",
                                       text="What note is " + str(current_interval) + " semitones "
                                            + current_above_below + " " + current_note + "?")
        question_label.grid(row=0, column=1, columnspan=4, padx=5, pady=5)


# Button widget for the next question
next_question_button = tkinter.Button(root, width=5, text="Next >>", command=create_new_question)


# Check if the user's answer is correct
def check_answer(user_answer):
    if user_answer == current_correct_note:
        return True
    else:
        return False


# Check which button the user clicked, and run the check_answer function
def button_click(button_type):
    # Note button clicks handled here.
    # For each button, check if clicked note button matches the correct answer.
    if button_type == "C":
        user_answer_index = 0
        user_answer = notes[user_answer_index]
        answer_is_correct = check_answer(user_answer)
        if answer_is_correct:
            wrong_answer_label.grid_forget()
            correct_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
            next_question_button.grid(row=4, column=4, columnspan=4)
        if not answer_is_correct:
            correct_answer_label.grid_forget()
            wrong_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

    elif button_type == "C#/Db":
        user_answer_index = 1
        user_answer = notes[user_answer_index]
        answer_is_correct = check_answer(user_answer)
        if answer_is_correct:
            wrong_answer_label.grid_forget()
            correct_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
            next_question_button.grid(row=4, column=4, columnspan=4)
        if not answer_is_correct:
            correct_answer_label.grid_forget()
            wrong_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

    elif button_type == "D":
        user_answer_index = 2
        user_answer = notes[user_answer_index]
        answer_is_correct = check_answer(user_answer)
        if answer_is_correct:
            wrong_answer_label.grid_forget()
            correct_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
            next_question_button.grid(row=4, column=4, columnspan=4)
        if not answer_is_correct:
            correct_answer_label.grid_forget()
            wrong_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

    elif button_type == "D#/Eb":
        user_answer_index = 3
        user_answer = notes[user_answer_index]
        answer_is_correct = check_answer(user_answer)
        if answer_is_correct:
            wrong_answer_label.grid_forget()
            correct_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
            next_question_button.grid(row=4, column=4, columnspan=4)
        if not answer_is_correct:
            correct_answer_label.grid_forget()
            wrong_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

    elif button_type == "E":
        user_answer_index = 4
        user_answer = notes[user_answer_index]
        answer_is_correct = check_answer(user_answer)
        if answer_is_correct:
            wrong_answer_label.grid_forget()
            correct_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
            next_question_button.grid(row=4, column=4, columnspan=4)
        if not answer_is_correct:
            correct_answer_label.grid_forget()
            wrong_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

    elif button_type == "F":
        user_answer_index = 5
        user_answer = notes[user_answer_index]
        answer_is_correct = check_answer(user_answer)
        if answer_is_correct:
            wrong_answer_label.grid_forget()
            correct_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
            next_question_button.grid(row=4, column=4, columnspan=4)
        if not answer_is_correct:
            correct_answer_label.grid_forget()
            wrong_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

    elif button_type == "F#/Gb":
        user_answer_index = 6
        user_answer = notes[user_answer_index]
        answer_is_correct = check_answer(user_answer)
        if answer_is_correct:
            wrong_answer_label.grid_forget()
            correct_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
            next_question_button.grid(row=4, column=4, columnspan=4)
        if not answer_is_correct:
            correct_answer_label.grid_forget()
            wrong_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

    elif button_type == "G":
        user_answer_index = 7
        user_answer = notes[user_answer_index]
        answer_is_correct = check_answer(user_answer)
        if answer_is_correct:
            wrong_answer_label.grid_forget()
            correct_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
            next_question_button.grid(row=4, column=4, columnspan=4)
        if not answer_is_correct:
            correct_answer_label.grid_forget()
            wrong_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

    elif button_type == "G#/Ab":
        user_answer_index = 8
        user_answer = notes[user_answer_index]
        answer_is_correct = check_answer(user_answer)
        if answer_is_correct:
            wrong_answer_label.grid_forget()
            correct_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
            next_question_button.grid(row=4, column=4, columnspan=4)
        if not answer_is_correct:
            correct_answer_label.grid_forget()
            wrong_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

    elif button_type == "A":
        user_answer_index = 9
        user_answer = notes[user_answer_index]
        answer_is_correct = check_answer(user_answer)
        if answer_is_correct:
            wrong_answer_label.grid_forget()
            correct_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
            next_question_button.grid(row=4, column=4, columnspan=4)
        if not answer_is_correct:
            correct_answer_label.grid_forget()
            wrong_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

    elif button_type == "A#/Bb":
        user_answer_index = 10
        user_answer = notes[user_answer_index]
        answer_is_correct = check_answer(user_answer)
        if answer_is_correct:
            wrong_answer_label.grid_forget()
            correct_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
            next_question_button.grid(row=4, column=4, columnspan=4)
        if not answer_is_correct:
            correct_answer_label.grid_forget()
            wrong_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)

    elif button_type == "B":
        user_answer_index = 11
        user_answer = notes[user_answer_index]
        answer_is_correct = check_answer(user_answer)
        if answer_is_correct:
            wrong_answer_label.grid_forget()
            correct_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
            next_question_button.grid(row=4, column=4, columnspan=4)
        if not answer_is_correct:
            correct_answer_label.grid_forget()
            wrong_answer_label.grid(row=4, column=1, columnspan=4, padx=5, pady=5)


# Button widgets for each note, set text, colour, size, and command
C_button = tkinter.Button(root, text='C', activeforeground="white", fg="white", activebackground="#444441",
                          bg="#444441", width=5, command=lambda: button_click("C"))
C_sharp_button = tkinter.Button(root, text='C#/Db', activeforeground="white", fg="white", activebackground="#444441",
                                bg="#444441", width=5, command=lambda: button_click("C#/Db"))
D_button = tkinter.Button(root, text='D', activeforeground="white", fg="white", activebackground="#444441",
                          bg="#444441", width=5, command=lambda: button_click("D"))
D_sharp_button = tkinter.Button(root, text='D#/Eb', activeforeground="white", fg="white", activebackground="#444441",
                                bg="#444441", width=5, command=lambda: button_click("D#/Eb"))
E_button = tkinter.Button(root, text='E', activeforeground="white", fg="white", activebackground="#444441",
                          bg="#444441", width=5, command=lambda: button_click("E"))
F_button = tkinter.Button(root, text='F', activeforeground="white", fg="white", activebackground="#444441",
                          bg="#444441", width=5, command=lambda: button_click("F"))
F_sharp_button = tkinter.Button(root, text='F#/Gb', activeforeground="white", fg="white", activebackground="#444441",
                                bg="#444441", width=5, command=lambda: button_click("F#/Gb"))
G_button = tkinter.Button(root, text='G', activeforeground="white", fg="white", activebackground="#444441",
                          bg="#444441", width=5, command=lambda: button_click("G"))
G_sharp_button = tkinter.Button(root, text='G#/Ab', activeforeground="white", fg="white", activebackground="#444441",
                                bg="#444441", width=5, command=lambda: button_click("G#/Ab"))
A_button = tkinter.Button(root, text='A', activeforeground="white", fg="white", activebackground="#444441",
                          bg="#444441", width=5, command=lambda: button_click("A"))
A_sharp_button = tkinter.Button(root, text='A#/Bb', activeforeground="white", fg="white", activebackground="#444441",
                                bg="#444441", width=5, command=lambda: button_click("A#/Bb"))
B_button = tkinter.Button(root, text='B', activeforeground="white", fg="white", activebackground="#444441",
                          bg="#444441", width=5, command=lambda: button_click("B"))

# Create correct/wrong answer labels
correct_answer_label = tkinter.Label(root, fg="white", bg="#2b2b2b", text='Correct!')
wrong_answer_label = tkinter.Label(root, fg="white", bg="#2b2b2b", text='You is wrong!')

# Button widget that quits the program
quit_button = tkinter.Button(root, text='Quit', width=5, command=root.quit)
quit_button.grid(row=4, column=1)

# Put the note button widgets on the screen.
C_button.grid(row=1, column=1)
C_sharp_button.grid(row=1, column=2)
D_button.grid(row=1, column=3)
D_sharp_button.grid(row=1, column=4)
E_button.grid(row=2, column=1)
F_button.grid(row=2, column=2)
F_sharp_button.grid(row=2, column=3)
G_button.grid(row=2, column=4)
G_sharp_button.grid(row=3, column=1)
A_button.grid(row=3, column=2)
A_sharp_button.grid(row=3, column=3)
B_button.grid(row=3, column=4)

# Run the main loop.
root.mainloop()
