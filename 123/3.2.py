import random
import time 
length = 10000
array = [random.uniform(0,10000) for _ in range(length)]


def selection_sort(arr):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
start_time = time.time() 
selection_sort(array)        
end_time = time.time()  
vremya = end_time - start_time
vremya_format = f"{vremya:.6f} секунд"

print (array)
print (vremya_format)