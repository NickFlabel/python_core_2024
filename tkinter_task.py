from tkinter import Tk, Label, Button

root = Tk()
root.title("Заголовок окна")
root.geometry("300x200")

label = Label(root, text="Нажми кнопку", font=("Arial", 14))
label.pack(padx=10, pady=10)


def on_click():
    label.config(text="Текст изменен!")


button = Button(root, text="Изменить текст", command=on_click)
button.pack()

root.mainloop()


