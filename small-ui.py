#!/usr/bin/env python3
#

import sys
import tkinter as tk
from tkinter import ttk

appname = "scaling-test"
applongname = "Scaling Test UI"

class AppWindow:

    def __init__(self, master, scale=100):
        self.w = master

        self.w.title(f'{applongname}-{scale}')
        self.w.rowconfigure(0, weight=1)
        self.w.columnconfigure(0, weight=1)

        frame = tk.Frame(self.w, name=appname.lower())
        frame.grid(sticky=tk.NSEW)
        frame.columnconfigure(1, weight=1)

        self.thing_label = tk.Label(frame)
        self.thing_label.grid(row=1, column=0, sticky=tk.W)
        self.thing_label['text'] = 'Scale:'
        self.thing = tk.Label(frame, compound=tk.RIGHT, anchor=tk.W, name='thing')
        self.thing['text'] = str(scale)
        self.thing.grid(row=1, column=2, sticky=tk.EW)

        self.menubar = tk.Menu(self.w)

        self.file_menu = tk.Menu(self.menubar, tearoff=tk.FALSE, title='File')
        self.file_menu.add_command(label='Exit', command=self.onexit)
        self.menubar.add_cascade(label='File', menu=self.file_menu)

        self.w.protocol("WM_DELETE_WINDOW", self.onexit)

        self.w.config(menu=self.menubar)

    def onexit(self, event=None):
        self.w.destroy()

    def _destroy(self):
        self.destroy()


def main():
    if len(sys.argv) != 2:
        print('Please supply a percentage scale to apply, i.e. 200 for 2x rendering scale')
        sys.exit(-1)

    root = tk.Tk(className=f'{appname.lower()}-{sys.argv[1]}')

    print(f'Initial tk scaling: {root.tk.call("tk", "scaling")}')
    print(f'Scale percentage is {sys.argv[1]}')
    root.tk.call('tk', 'scaling', root.tk.call("tk", "scaling") * float(int(sys.argv[1]) / 100.0))
    print(f'tk scaling now: {root.tk.call("tk", "scaling")}')

    app = AppWindow(root, scale=sys.argv[1])

    root.mainloop()


if __name__ == '__main__':
    main()
