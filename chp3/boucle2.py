import random
from random import randint


seuilmax = 35.0


for i in range(10) : 
    temperature = random.uniform(20, 40)
    if temperature > seuilmax:
        print(f"le seul de temperature a été dépasser : {temperature:.2f}°C")
    else :
        print(f"la tempétature est correct :{temperature :.1f}°C")