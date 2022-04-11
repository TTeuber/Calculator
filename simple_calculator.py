from tkinter import *

root = Tk()
root.title("simple calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


function = ''
a = 0
b = 0
state = ''
equal_state = False


def addition():
    return float(a) + float(b)


def subtraction():
    return float(a) - float(b)


def multiplication():
    return float(a) * float(b)


def division():
    return float(a) / float(b)


def button_click(number):
    global a, b, function, state, equal_state
    if equal_state:
        e.delete(0, END)
        function = ''
        state = ''
        a = 0
        b = 0
        equal_state = False
    if number == '.' and e.get() == '':
        e.insert(0, '0')
    if state == '':
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))
    elif state == 'fill':
        e.delete(0, END)
        e.insert(0, str(number))
        state = ''


def button_clear():
    global a, b, function, state, equal_state
    e.delete(0, END)
    function = ''
    state = ''
    a = 0
    b = 0
    equal_state = False


def button_back():
    e.delete(0, END)


def button_addition():
    global function, a, b, state, equal_state
    if equal_state:
        b = 0
        equal_state = False
        function = ''
    if function == '':
        a = e.get()
        function = 'addition'
        state = 'fill'
    else:
        b = e.get()
        do_functions()
        a = e.get()
        state = 'fill'
        function = 'addition'
    format_entry()


def button_subtraction():
    global function, a, b, state, equal_state
    if equal_state:
        b = 0
        equal_state = False
        function = ''
    if e.get() == '':
        e.insert(0, '-')
    else:
        if function == '':
            a = e.get()
            function = 'subtraction'
            state = 'fill'
        else:
            b = e.get()
            do_functions()
            a = e.get()
            state = 'fill'
            function = 'subtraction'
        format_entry()


def button_multiplication():
    global function, a, b, state, equal_state
    if equal_state:
        b = 0
        equal_state = False
        function = ''
    if function == '':
        a = e.get()
        function = 'multiplication'
        state = 'fill'
    else:
        b = e.get()
        do_functions()
        a = e.get()
        state = 'fill'
        function = 'multiplication'
    format_entry()


def button_division():
    global function, a, b, state, equal_state
    if equal_state:
        b = 0
        equal_state = False
        function = ''
    if function == '':
        a = e.get()
        function = 'division'
        state = 'fill'
    else:
        b = e.get()
        do_functions()
        a = e.get()
        state = 'fill'
        function = 'division'
    format_entry()


def do_functions():
    global a, b
    if function == 'addition':
        e.delete(0, END)
        a = addition()
        e.insert(0, str(a))
    elif function == 'subtraction':
        e.delete(0, END)
        a = subtraction()
        e.insert(0, str(a))
    elif function == 'multiplication':
        e.delete(0, END)
        a = multiplication()
        e.insert(0, str(a))
    elif function == 'division':
        e.delete(0, END)
        a = division()
        e.insert(0, str(a))
    format_entry()


def button_equivalence():
    global a, b, equal_state
    if not equal_state:
        b = e.get()
        do_functions()
        equal_state = True
    elif equal_state:
        do_functions()


def format_entry():
    if float(e.get()) % 1 == 0:
        current = int(float(e.get()))
        e.delete(0, END)
        e.insert(0, str(current))
    else:
        current = float(e.get())
        e.delete(0, END)
        e.insert(0, str(round(current, 6)))


button_1 = Button(root, text="1", width=5, height=3, command=lambda: button_click(1))
button_2 = Button(root, text="2", width=5, height=3, command=lambda: button_click(2))
button_3 = Button(root, text="3", width=5, height=3, command=lambda: button_click(3))
button_4 = Button(root, text="4", width=5, height=3, command=lambda: button_click(4))
button_5 = Button(root, text="5", width=5, height=3, command=lambda: button_click(5))
button_6 = Button(root, text="6", width=5, height=3, command=lambda: button_click(6))
button_7 = Button(root, text="7", width=5, height=3, command=lambda: button_click(7))
button_8 = Button(root, text="8", width=5, height=3, command=lambda: button_click(8))
button_9 = Button(root, text="9", width=5, height=3, command=lambda: button_click(9))
button_0 = Button(root, text="0", width=5, height=3, command=lambda: button_click(0))
button_decimal = Button(root, text=".", width=5, height=3, command=lambda: button_click("."))

button_add = Button(root, text="+", width=5, height=3, command=button_addition)
button_subtract = Button(root, text="-", width=5, height=3, command=button_subtraction)
button_multiply = Button(root, text="x", width=5, height=3, command=button_multiplication)
button_divide = Button(root, text="/", width=5, height=3, command=button_division)
button_equal = Button(root, text="=", width=10, height=3, command=button_equivalence)
button_clear = Button(root, text="clear", width=10, height=3, command=button_clear)
button_back = Button(root, text="back", width=5, height=3, command=button_back)

button_1.grid(row=3, column=0)
button_3.grid(row=3, column=2)
button_2.grid(row=3, column=1)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_decimal.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equal.grid(row=5, column=0, columnspan=2)
button_clear.grid(row=5, column=2, columnspan=2)
button_back.grid(row=4, column=2)

root.mainloop()
