from Experiment import Event

def Start_Of_Event(name,thr,pixels=262144,steps=8000):
    Ev = Event(name,thr,steps)
    Ev.CreateSteps()
   
    myFile = open("./logs/experiments %s.txt"%name,"a")
    for each in Ev.splitting():
        myFile.write(str(each))
    myFile.close()
    Ev.splitting()

askName = input("What is the name of the experiment:\n")

Start_Of_Event(askName,300)
