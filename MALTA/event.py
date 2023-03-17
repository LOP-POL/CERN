from Experiment import Event

def Start_Of_Event(name,thr,steps=8000):
    Ev = Event(name,thr,steps)
    Ev.CreateSteps()
    
    return print(Ev.CreateGroups())

Start_Of_Event("Sigma",400)