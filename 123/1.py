import random
import time
import string
letters = string.ascii_letters
length = 10000
array = [random.choice(letters) for _ in range(length)]

def bubble_sort(array): 
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

start_time = time.time() 
bubble_sort(array)        
end_time = time.time()  
vremya = end_time - start_time
vremya_format = f"{vremya:.6f} секунд"

print (array)
print (vremya_format)