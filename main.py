words = ['Mango','Apple','engineer','civil','gun','fan','tv','door','laptop','bottle','water','grapes','megastar','workshop','courage','honesty']

def labelSlider():
    global count, sliderwords
    text = 'Welcome to typing Speed Increaser Game'
    if(count >= len(text)):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    fontLabel.configure(text=sliderwords)
    fontLabel.after(150,labelSlider)

def time():
    global timeleft, score, miss
    if(timeleft >= 11):
        pass
    else:
        timeLableCount.configure(fg='red')

    if(timeleft>0):
        timeleft-= 1
        timeLableCount.configure(text=timeleft)
        timeLableCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='HIT ={} | MISS ={} | Total Score ={}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('notification','For play Again Hit Retry Button')
        if(rr==True):
            score = 0
            timeleft = 30
            miss = 0
            timeLableCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLableCount.configure(text=score)

def startGame(event):
    global score,miss
    if(timeleft == 30):
        time()
    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score +=1
        scoreLableCount.configure(text=score)
        print("Score :",score)
    else:
        miss +=1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)

from tkinter import *
import random
from tkinter import messagebox

####root method
root = Tk()
root.wm_geometry('800x600+200+100')
root.configure(bg='powder blue')
root.title('Typing Speed Increaser Game')
root.iconbitmap('typingspeed.ico')
#####VARIABLE SECTION
score = 0
timeleft = 30
count = 0
sliderwords = ''
miss = 0
####label method
fontLabel = Label(root,text='',font=('airal',25,'italic bold'),
                 bg='powderblue',fg='red',width=40)
fontLabel.place(x=10,y=10)
labelSlider()

random.shuffle(words)
wordLabel= Label(root,text=words[0],font=('airal',40,'italic bold'),bg='powder blue')
wordLabel.place(x=300,y=150)

scoreLable = Label(root,text='Your Score : ',font=('airal',25,'italic bold'),bg='powder blue',fg='black')
scoreLable.place(x=10,y=100)

scoreLableCount = Label(root,text=score,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
scoreLableCount.place(x=80,y=180)

timerLabel = Label(root,text='Time Left :',font=('airal',25,'italic bold'),bg='powder blue',fg='black')
timerLabel.place(x=600,y=100)

timeLableCount = Label(root,text=timeleft,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
timeLableCount.place(x=680,y=180)


gamePlayDetailLabel = Label(root,text='Type word And Hit Enter Button',font=('arial',30,'italic bold'),
                            bg='powder blue',fg='dark grey')
gamePlayDetailLabel.place(x=120,y=450)


####entry method
wordEntry = Entry(root,font=('airal',25,'italic bold'),bd=10,justify='center')
wordEntry.place(x=200,y=220)
wordEntry.focus_set()
#####'
root.bind('<Return>',startGame)
root.mainloop()