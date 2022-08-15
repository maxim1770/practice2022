from tkinter import *
from tkinter import ttk


def start():
    alist = enter.get().split()
    alist = [int(x) for x in alist]

    if len(lab_list) > 0:
        for i in range(len(lab_list)):
            lab_list[0].after(1, lab_list[0].destroy())
            lab_list.pop(0)

    for i in range(len(alist)):
        a = Label(mainframe, text=str(alist[i]))
        a.grid(column=1, row=3 + i, sticky=W)
        lab_list.append(a)
    buton.state(["disabled"])
    enter_entry.state(["disabled"])
    root.after(1, step(alist))


def step_(alist, i=1):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def step(alist, i=1):
    if i < len(alist):
        temp = alist[i]
        j = i - 1
        while j >= 0 and temp < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp
        for k in range(len(lab_list)):
            lab_list[k].configure(text=str(alist[k]))
        i += 1
        print(alist)
        root.update_idletasks()
        root.after(1000)
        root.after(1, lambda: step(alist, i))
    if i == len(alist):
        print(alist)
        buton.state(["!disabled"])
        enter_entry.state(["!disabled"])
        for k in range(len(alist)):
            lab_list[k].configure(background="#99ff99")
        return


root = Tk()
root.title("Графика")
root.geometry('400x400')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

Label(mainframe, text='ввод: ').grid(column=1, row=1, sticky=W)

enter = StringVar()
enter_entry = ttk.Entry(mainframe, width=7, textvariable=enter)
enter_entry.grid(column=2, row=1, sticky=(W, E))

buton = ttk.Button(mainframe, text="кнопка", command=start)
buton.grid(column=2, row=2, sticky=W)

#massiv = Label(mainframe, text='')
#massiv.grid(column=1, row=3, sticky=W)

lab_list = []

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()