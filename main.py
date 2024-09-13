from tkinter import*
from textblob  import TextBlob

main =  Tk()
main.title("Spelling checker")
main.geometry("700x400")
spell_text=StringVar()

def check_spelling():
    word=text_field.get()
    check=TextBlob(word)
    correct_word = str(check.correct())
    spell_text.set("correct Word: "+correct_word)
title_label=Label(main,text="Spelling checker", font=("poppins",30,"bold"))
title_label.pack(pady=50)

text_field = Entry(main,font=("poppins",25))
text_field.pack()

check_button = Button(main,text="check",font=("poppins",20),command=check_spelling)
check_button.pack(pady=20)

spell_label=Label(main,font=("poppins",20),textvariable=spell_text)
spell_label.pack()
main.mainloop()