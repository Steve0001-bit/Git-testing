import time
import random

#### 4D Random NUmber ( single entry )
numbers = []
while True:
    time.sleep(3)
    number = random.randint(0, 9)
    numbers.append(number)
    
    if len(numbers) == 4:
        break
print("-" * 80)        
print("Your 4D number :", numbers)
print("-" * 80) 