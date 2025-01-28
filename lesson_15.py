import tkinter

window = tkinter.Tk() # Инициализация пустого класса
# Задаем название окна
window.title("Добро пожаловать в приложение")
lbl = tkinter.Label(window, text="Добро пожаловать") # Создаем надпись
lbl.grid(column=0, row=0) # Задаем начальное положение
window.geometry("400x250") # Задаем начальный размер

def clicked():
    lbl.configure(text="Кнопка была нажата")

btn = tkinter.Button(window, text="Нажми меня", command=clicked)
btn.grid(column=0, row=1)
# Запускаем наше приложение
# window.mainloop()

class Main(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self._init_main()

    def _init_main(self):
        toolbar = tkinter.Frame()
        toolbar.pack(side=tkinter.TOP)

        btnOpenDialog = tkinter.Button(
            toolbar,
            text="Добавить позицию",
            command=self.open_dialog
        )
        btnOpenDialog.pack(side=tkinter.LEFT)

    def open_dialog(self):
        Child()


class Child(tkinter.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Добавить расходы/доходы")
        self.geometry("440x220")
        self.resizable(False, False)

