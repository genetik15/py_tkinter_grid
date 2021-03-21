from tkinter import *

root = Tk()

l_user = Label(root, text='Логин: ').grid(row=0, column=0, padx=10, pady=10, sticky=W)
e_user = Entry(root).grid(row=0, column=1, columnspan=2, padx=10, sticky=W+E)

l_pass = Label(root, text='Пароль: ').grid(row=1, column=0, padx=10, sticky=W)
e_pass = Entry(root, show='*').grid(row=1, column=1, columnspan=2, padx=10, sticky=W+E)

btn_login = Button(root, text='Вход', padx=10).grid(row=2, column=0, padx=10, pady=10, sticky=W)
btn_registration = Button(root, text='Регистрация', padx=10).grid(row=2, column=1, padx=10, sticky=W)
btn_forgot = Button(root, text='Забыли пароль?', padx=10).grid(row=2, column=2, padx=10, sticky=W)

root.mainloop()
