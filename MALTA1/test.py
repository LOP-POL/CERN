from Experiment import Experiment

experiment = Experiment("firstTry")
for i in range(10):
	experiment.GenerateSteps()
	experiment.StartOfEvent()
	print("Number of hits: %n" % experiment.GetNumberOfHits())
	experiment.EndOfEvent()
	print("Number of digits: %n" % experiment.GetNumberOfDigits())
	pass

print("Have a nice day")