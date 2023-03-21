from Experiment import Experiment

myFirstTry = Experiment("firstTry")
myFirstTry.StartEvent()
myFirstTry.CreateHits(10000)
myFirstTry.EndOfEvent()