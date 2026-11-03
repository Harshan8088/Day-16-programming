import numpy as np

marks=np.array([90,80,70,60,50,40])

total=np.sum(marks)
average=np.mean(marks)
percentage=(total/600)*100

print("Total Marks:",total)
print("Average Marks:",average) 
print("Percentage:",percentage)