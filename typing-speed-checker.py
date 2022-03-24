from tkinter import *
from tkinter import ttk

DURATION = 30
text1 = "If you don't like a test prompt, you can get a different (random) prompt with the 'change test' button - or select a specific paragraph to type from the list below. To find out how fast you type, just start typing in the blank textbox on the right of the test prompt. You will see your progress, including errors on the left side as you type. In order to complete the test and save your score, you need to get 100% accuracy. You can fix errors as you go, or correct them at the end with the help of the spell checker. Stimulate your mind as you test your typing speed with this standard English paragraph typing test. Watch your typing speed and accuracy increase as you learn about a variety of new topics! Over 40 typing test selections are available. To find out how fast you type, just start typing in the blank textbox on the right of the test prompt. You will see your progress, including errors on the left side as you type. In order to complete the test and share your results, you need to get 100% accuracy. You can review your progress for this session with the feedback chart below. Just hover over a dot to see what your average speed and accuracy are for that key. Because of the laboriousness of the translation process, since the 1940s efforts have been made, with varying degrees of success, to automate translation or to mechanically aid the human translator. More recently, the rise of the Internet has fostered a worldwide market for translation services and has facilitated 'language localization'. Ideally, the translator must know both languages, as well as the subject that is to be translated."
text2 = 'A quick brown fox jumps over the lazy dog'
text3 = 'Type to search about something you want to search  about'
sample_list = [text1, text2, text3]
text = sample_list[0]


def check():
    type_box.config(state='disabled')
    user_text = type_box.get('1.0', 'end')
    user_words = user_text.split(' ')
    test_words = text.split(' ')
    correct_words = 0
    for n in range(len(user_words)):
        if user_words[n] == test_words[n]:
            correct_words += 1
    speed = correct_words * 60/DURATION
    Label(window, text=f'Your typing speed is {speed} WPM', font=("Arial", 25)).pack(pady=20)


def start_typing(event):
    type_box.unbind("<KeyPress>")
    type_box.after(1000 * DURATION, check)


def change_sample(event):
    global text
    for n in range(len(values)):
        if samples.get() == values[n]:
            text = sample_list[n]
            print(text)
            textbox.config(state='normal')
            textbox.delete('1.0', 'end')
            textbox.insert('end', text)
            type_box.focus()


def restart_test():
    global restart, window, text
    window.destroy()
    restart = True
    text = sample_list[0]


restart = True
while restart:
    restart = False
    window = Tk()
    window.title('Typing Meter')
    window.minsize(width=400, height=400)
    window.config(padx=20, pady=20, bg='light blue')

    frame = Frame(window, pady=10, padx=10)
    frame.pack()

    sample_label = Label(frame, text='Pick a Sample: ')
    sample_label.pack(side='left')

    values = ['Sample 1', 'Sample 2', 'Sample 3']
    samples = ttk.Combobox(frame, values=values)
    samples.current(0)
    samples.pack(side='right')
    samples.bind('<<ComboboxSelected>>', change_sample)

    textbox = Text(window, width=180, height=10,)
    textbox.pack(expand=True)
    textbox.insert('end', text)
    textbox.config(state='disabled', padx=10)

    type_label = Label(window, text='This is 1 minute Typing Test. Time will start when you start typing')
    type_label.pack(pady=10)

    type_box = Text(window, width=180, height=10, padx=10, pady=10)
    type_box.pack()
    type_box.focus()
    type_box.bind("<KeyPress>", start_typing)

    restart_btn = Button(window, text='Restart', command=restart_test)
    restart_btn.pack(side='right', pady=10)

    window.mainloop()
