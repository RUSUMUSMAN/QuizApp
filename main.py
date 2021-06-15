from tkinter import *
from tkinter import messagebox
app=Tk()

app.title('QUIZAPP')
app.geometry('800x550+400+200')
i=0
dct=dict()
qut=[["Is Python case sensitive when dealing with identifiers?","yes","no","machine dependent","none"],["What is the maximum possible length of an identifier?","31 characters","63 characters","79 characters","none"],["Which of the following is invalid?","_a=1","__a=1","__str__=1","none"],["Which of the following is an invalid variable?","my_string_1","1st_string","foo","_"]]
ans=["yes","none","none","1st_string"]
def submit():
    global i,dct
    dct[i]=var.get()
    correct=0
    for j in range(0,len(qut)):
        if j in dct.keys() and dct[j]==ans[j]:
            correct+=1
    check=messagebox.askquestion("Submit Test", "Do you want to submit the test?",icon="warning")
    if check=="yes":
        que.destroy()
        optionf.destroy()
        bframe.destroy()
        finalLabel = Label(app,text="Successfully completed!\n\nYour Score : {}/{}".format(correct,len(qut)),fg="green",width=700,pady=20,font="Times 20",height=300,anchor=CENTER)
        finalLabel.pack()


def next():
    global i,optionf,dct,btn1
    if var.get()!="":
        selection = var.get()
        dct[i] =selection
        # print(selection)

    i=i+1
    if i==1:
        btn1 = Button(bframe, text="Previous", fg="#fff", font="Times 16", bg="green", padx=10, pady=10, command=prev)
        btn1.grid(row=0,column=0)
        btn2.grid(padx=(550,0))
    if i<=len(qut)-1:
        que.config(text="Q.No"+str(i))
        qusl.config(text=qut[i][0])
        optionf.destroy()
        optionf = LabelFrame(app, text="options", bd=2, bg="#000", fg="#fff", padx=10, pady=10, highlightbackground="red",
                             highlightthickness=2)
        optionf.pack(padx=10, pady=10)
        for j in range(1, len(qut[i])):
            temp = "opt" + str(j)
            temp = Radiobutton(optionf, text=qut[i][j], width=600, anchor="w", value=qut[i][j], variable=var,
                               font="Times 16", fg="#222", bg="#fff", padx=20)
            temp.pack(pady=10)
    if i==len(qut)-1:
        btn2.config(text="SUBMIT",command=submit)


def prev():
    global i, optionf, dct,btn1
    i = i - 1
    if i<len(qut)-1:
        btn2.config(text="NEXT",command=next)

    if i==0:
        btn1.destroy()
        btn2.grid(padx=(650, 0))
    if i>=0:
        que.config(text="Q.No" + str(i))
        qusl.config(text=qut[i][0])
        optionf.destroy()
        optionf = LabelFrame(app, text="options", bd=2, bg="#000", fg="#fff", padx=10, pady=10,
                             highlightbackground="red",
                             highlightthickness=2)
        optionf.pack(padx=10, pady=10)
        for j in range(1, len(qut[i])):
            temp = "opt" + str(j)
            temp = Radiobutton(optionf, text=qut[i][j], width=600, anchor="w", value=qut[i][j], variable=var,
                               font="Times 16", fg="#222", bg="#fff", padx=20)
            temp.pack(pady=10)
    else:
        print(dct)
#This is a heading of the application
head=LabelFrame(app,highlightbackground="red",bd=2,highlightthickness=2)
head.pack(padx=10,pady=10)

logo = Label(head,text="QUIZ",width=600,font="Times 20",bg="green",padx=10,pady=10)
logo.pack()


#this is a frame setting for question
que=LabelFrame(app,text="Q.No"+str(i+1),highlightbackground="white",highlightthickness=2)
que.pack(padx=10,pady=10)

qusl=Label(que,text=qut[i][0],width=600,font="Times 16",wraplength=600,fg="#000")
qusl.pack()

#this is a frame for options for the questions.
optionf=LabelFrame(app,text="options",bd=2,bg="#000",fg="#fff",padx=10,pady=10,highlightbackground="red",highlightthickness=2)
optionf.pack(padx=10,pady=10)
var=StringVar()
for j in range(1,len(qut[0])):
    temp="opt"+str(j)
    temp = Radiobutton(optionf,text=qut[0][j],width=600,anchor="w",value=qut[0][j],variable=var,font="Times 16",fg="#222",bg="#fff",padx=20)
    temp.pack(pady=10)


#This is the frame to set move to the next or back to previous
bframe=LabelFrame(app,bd=2,bg="#fff",fg="#fff",padx=10,pady=10,highlightbackground="red",highlightthickness=2)
bframe.pack(side=BOTTOM)
btn2=Button(bframe,text="NEXT",fg="#fff",font="Times 16",bg="green",padx=10,pady=10,command=next)
btn2.grid(row=0,column=1,padx=(650,0))


app.mainloop()
