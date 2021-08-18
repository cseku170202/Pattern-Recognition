import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkcalendar import *
from PIL import ImageTk, Image


import Naive_bayes_testing
import Naive_bayes_NAND_testing
import Naive_bayes_NOR_testing

root = Tk()
root.title('Naive Bayes Model')
root.geometry("800x550")

ttk.Label(root, text="Select a Logic Gate!!",
          background='blue', foreground="white",
          font=("Times New Roman", 15)).pack()



############################# AND ###########################
def Cat_Prediction():
    new_root = Tk()
    new_root.title('AND GATE')
    new_root.geometry("650x500")

    ttk.Label(new_root, text="Enter AND Gate inputs!!",
              background='blue', foreground="white",
              font=("Times New Roman", 15)).pack()

    def clear_screen():
        my_text.delete(1.0, END)
        get_text_label.config(text='')

        my_text1.delete(1.0, END)
        get_text_label1.config(text='')
        pass

    def find_category():
        global news
        #get_text_label.config(text=my_text.get(1.0, END))
        news = my_text.get(1.0, END)
        news1 = my_text1.get(1.0, END)
        #print(news)
        #print(type(news))
        news = str(news)
        get_cat = Naive_bayes_testing.Classify(news, news1)
        get_text_label.config(text="Result :"+" "+get_cat)
        pass

    my_text = Text(new_root, width=10, height=2, background='yellow', foreground='blue', font=("Times New Roman", 14))
    my_text.pack(pady=20)

    my_text1 = Text(new_root, width=10, height=2, background='yellow', foreground='blue', font=("Times New Roman", 14))
    my_text1.pack(pady=40)

    text_frame = Frame(new_root)
    text_frame.pack()


    clear_button = Button(text_frame, text="Clear Input Screen", command=clear_screen)
    clear_button.grid(row=0, column=0)


    get_text_button = Button(text_frame, text="Observe Decision", command=find_category)
    get_text_button.grid(row=0, column=1, padx=20)

    get_text_label = Label(new_root, text='', font=("Times New Roman", 15))
    get_text_label.pack(pady=15)

    get_text_label1 = Label(new_root, text='')
    get_text_label1.pack(pady=50)

    pass

prediction_button = ttk.Button(root, text="AND", command=Cat_Prediction, width=10)
prediction_button.place(x=260, y=60)
############################# AND ###########################





############################# NAND Gate ###########################
def Cat_Prediction():
    new_root = Tk()
    new_root.title('NAND GATE')
    new_root.geometry("650x500")

    ttk.Label(new_root, text="Enter NAND Gate inputs!!",
              background='blue', foreground="white",
              font=("Times New Roman", 15)).pack()

    def clear_screen():
        my_text.delete(1.0, END)
        get_text_label.config(text='')

        my_text1.delete(1.0, END)
        get_text_label1.config(text='')
        pass

    def find_category():
        global news
        #get_text_label.config(text=my_text.get(1.0, END))
        news = my_text.get(1.0, END)
        news1 = my_text1.get(1.0, END)
        #print(news)
        #print(type(news))
        news = str(news)
        get_cat = Naive_bayes_NAND_testing.Classify(news, news1)
        get_text_label.config(text="Result :"+" "+get_cat)
        pass

    my_text = Text(new_root, width=10, height=2, background='yellow', foreground='blue', font=("Times New Roman", 14))
    my_text.pack(pady=20)

    my_text1 = Text(new_root, width=10, height=2, background='yellow', foreground='blue', font=("Times New Roman", 14))
    my_text1.pack(pady=40)

    text_frame = Frame(new_root)
    text_frame.pack()


    clear_button = Button(text_frame, text="Clear Input Screen", command=clear_screen)
    clear_button.grid(row=0, column=0)


    get_text_button = Button(text_frame, text="Observe Decision", command=find_category)
    get_text_button.grid(row=0, column=1, padx=20)

    get_text_label = Label(new_root, text='', font=("Times New Roman", 15))
    get_text_label.pack(pady=15)

    get_text_label1 = Label(new_root, text='')
    get_text_label1.pack(pady=50)

    pass

prediction_button = ttk.Button(root, text="NAND", command=Cat_Prediction, width=10)
prediction_button.place(x=370, y=60)
############################# NAND Gate ###########################





############################# NOR Gate ###########################
def Cat_Prediction():
    new_root = Tk()
    new_root.title('NOR GATE')
    new_root.geometry("650x500")

    ttk.Label(new_root, text="Enter NOR Gate inputs!!",
              background='blue', foreground="white",
              font=("Times New Roman", 15)).pack()

    def clear_screen():
        my_text.delete(1.0, END)
        get_text_label.config(text='')

        my_text1.delete(1.0, END)
        get_text_label1.config(text='')
        pass

    def find_category():
        global news
        #get_text_label.config(text=my_text.get(1.0, END))
        news = my_text.get(1.0, END)
        news1 = my_text1.get(1.0, END)
        #print(news)
        #print(type(news))
        news = str(news)
        get_cat = Naive_bayes_NOR_testing.Classify(news, news1)
        get_text_label.config(text="Result :"+" "+get_cat)
        pass

    my_text = Text(new_root, width=10, height=2, background='yellow', foreground='blue', font=("Times New Roman", 14))
    my_text.pack(pady=20)

    my_text1 = Text(new_root, width=10, height=2, background='yellow', foreground='blue', font=("Times New Roman", 14))
    my_text1.pack(pady=40)

    text_frame = Frame(new_root)
    text_frame.pack()


    clear_button = Button(text_frame, text="Clear Input Screen", command=clear_screen)
    clear_button.grid(row=0, column=0)


    get_text_button = Button(text_frame, text="Observe Decision", command=find_category)
    get_text_button.grid(row=0, column=1, padx=20)

    get_text_label = Label(new_root, text='', font=("Times New Roman", 15))
    get_text_label.pack(pady=15)

    get_text_label1 = Label(new_root, text='')
    get_text_label1.pack(pady=50)

    pass

prediction_button = ttk.Button(root, text="NOR", command=Cat_Prediction, width=10)
prediction_button.place(x=480, y=60)
############################# NOR Gate ###########################







root.mainloop()