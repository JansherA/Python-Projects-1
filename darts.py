#Jansher Azmat
#Healey



#Monte carlo walk question: 
#I think that the longest you could walk while still returning home at least 50%
#of the time is 5. It can't possibly be 4 or less, because regardless of how you walk, it would always be in walkable
#range 100% of the time. With a walking distance of 5, there is a possibility that you walk in a straight line, or any 
#shape that would make the return distance unachievable by walking. However, there is also a 50% possibility that you walk 
#back and forth or any other pattern that would be within 4 blocks of the starting location, allowing you to avoid the bus.


#Monte carlo research:

# Through my research, I found out that Monte Carlo simulations are used in the real word as a technique to find the impact of
# risk and uncertaintly in financial or similar forecasting models, according to riskamp.com

#Palisade.com states that Monte Carlo simulations preform risk analysis by building models of possible results by substituting a 
#range of balues (probability distribution) for any factor that has inherent uncertainty, repeating with different random values. In my own words, 
#the simulation calculates risks by creating different scenarios with randomly generated relevant numbers to the data. This gives you an idea of what 
#your possible outcomes could be, and allows you to make better financial decisions. 

#Dart Game: 
#What I've noticed as I increased the "times" value in my code (how many trials) is that the output becomes closer to pi, 3.141529 etc.., on average.
#According to the calculations used, this makes a lot of sense considering the circle incscribed has a radius of 1 and how pi relates to circles, obviously. 


import random #importing random module to generate the test values


times = 100000 #This is the number of times the code will go through the calculation, the more that this number is increased, the closer the output is to pi.
it = 0 #The number of successful iterations.
r = 1 #The radius of the inscribed circle, this was given in the directions.
darts = 0 #This is to track the number of total trials completed at a given time. Different than the variable "it".

for x in range(times): #This loops through whatever number "times" is, essentially doing the operation that many times.

	x = random.uniform(-1,1) #These two lines are the random number generated that goes through the calculations.
	y = random.uniform(-1,1)
	
	if True: #This keeps track of the total number of trials completed at any time.
		darts += 1 

	if x**2 + y**2 <= r**2: #This is the calculation itself to see if a point is in or on the inscribed circle.
		it += 1 #If it is inside, than the successful iterations is increased by one, of course.
		

final = it*4/darts #This was the given calculation in the directions. This is why the variable "darts" was created.
print(str(final)) #And finally, converting the float values to a string in order to print them out successfully. 
