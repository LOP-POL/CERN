This is a simulation of an event in the MALTA pixel detector. The step file contains a class that defines a step with a position and a charge.
In the experiment class a random number is generated for the number of steps because there is no telling what number of steps the detector will get.
Step objects are then generated witha  randomly generated position and charge.
Depending on the depending on the charge that is also randomly generated, the step objects that are hits are added to an array of hits.
