from tkinter import *
def yaz():
    abc = input1.get() + ' '+ input2.get() +' '+ input3.get() +'\n'
    

    with open('siyahi.txt','a') as file:
        print(file.write(abc))


window = Tk()

window.geometry('450x450')

input1 = Entry(width=20,font='Verdana 14')

input2 = Entry(width=20,font='Verdana 14')

input3 = Entry(width=20,font='Verdana 14')

input1.place(x=20, y=50)

input2.place(x=20, y=100)

input3.place(x=20, y=150)

yazil = Button(text='yazil',width=5,command=yaz)

yazil.place(x=20,y=200)


window.mainloop()