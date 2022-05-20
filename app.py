import os
from pprint import pprint as pp
from tkinter import *
from tkinter.ttk import *

from threading import Thread


def verify_extension(s):
    list_ext = ['py', 'html', 'php', 'c', 'cpp', 'ui', '']
    for ex in list_ext:
        if s.endswith('.' + ex):
            return True
    return False


def count_line(path):
    result = {}
    total = 0
    er = []
    for root, sub, files in os.walk(path):

        for f in files:

            if verify_extension(f):
                current_file_path = os.path.join(root, f)
                print(f)
                try:
                    with open(current_file_path, 'r') as current_file:
                        lines = current_file.readlines()
                        total += len(lines)
                        result[current_file_path] = len(lines)
                except:
                    er.append(f)
                    pass
    result['total_line'] = total
    result['error'] = er
    return result


def format(name, n, long=80):
    s = long - len(str(n))
    for _ in range(len(name), s):
        name += '-'
    return name + str(n)


class Fen(Tk):
    def __init__(self):
        super(Fen, self).__init__()
        self.geometry('1000x500')
        self.path_var = StringVar()

        self.label_title = Label(self, text='Line Count', font=('Helvetica', 12))
        self.frame_form = Frame(self)
        self.path_input = Entry(self.frame_form, textvariable=self.path_var, width=50)
        self.btn_valid = Button(self, text='Valider', command=lambda: self.count_line_ui(self.path_var.get()))

        self.frame_result = Frame(self)
        self.text_result = Text(self, state=DISABLED)
        self.text_result['width'] = 100
        self.text_result['height'] = 30

        self.placing()

    def placing(self):
        self.label_title.pack()

        self.frame_form.pack()
        Label(self.frame_form, text='Directory : ').grid(row=0, column=0)
        self.path_input.grid(row=0, column=1)

        self.btn_valid.pack(pady=20)

        self.frame_result.pack(pady=10)
        self.text_result.pack()

    def count_line_ui(self, path):
        result = count_line(path)
        index = 1
        self.text_result.delete(1.0, END)

        for p, number in result.items():
            self.text_result['state'] = NORMAL
            self.text_result.insert(END, format(p, number, long=100) + '\n')
            self.text_result['state'] = DISABLED
            index += 1


f = Fen()
f.mainloop()
