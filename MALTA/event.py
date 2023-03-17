from Experiment import Event

def Start_Of_Event(name,thr,pixels=65536,steps=8000):
    Ev = Event(name,thr,steps)
    Ev.CreateSteps(pixels)
    
    return print(Ev.CreateGroups(pixels))


askName = input("What is the name of the experiment:\n")
askThreshold = input("What is the threshold:\n")
askSteps = input("How many steps would you like to use\n")
askPixels = input("How many pixels, should be a number with a square root\n")
Start_Of_Event(askName,int(askThreshold),int(askPixels),int(askSteps))