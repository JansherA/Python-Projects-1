

import random



# times = 1000
# success = 0

# for x in range(times):


# 	chosen = random.randint(1,3)
# 	prize = random.randint(1,3)



# 	if chosen == prize:
# 		success += 1

times = 1000 #This is the number of times the code executes, just like the iterations in the Mandelbrot project
success = 0 #This is a counter of the times the player has won the prize



for x in range(times): #This loops through every iteration and goes through the randomness of picking doors
	chosen = random.randint(1,3) #These two lines are the random odds of each door
	prize = random.randint(1,3)

	

	if chosen != prize: #This is the code for switching doors. The commented code is for 1000 trials of not switching
		success += 1 #Increases the counter of successes each time there is a success

percent = success/times * 100 #This takes the iterations and successes and turns them into a percent


print(str(percent)+"%") #Printing out the percent
