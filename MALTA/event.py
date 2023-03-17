from Experiment import Event

def Start_Of_Event(name,thr,steps=8000):
    Ev = Event(name,thr,steps)
    Ev.CreateSteps()
    
    return print(Ev.CreateGroups())


askName = input("What is the name of the experiment:\n")
askThreshold = input("What is the threshold:\n")
askSteps = input("How many steps would you like to use\n")
Start_Of_Event(askName,int(askThreshold),askSteps)