import random
import time 
length = 10000
array = [random.randint(0,10000) for _ in range(length)]
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i

        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1

        array[j] = x

    return array
start_time = time.time() 
insertion_sort(array)        
end_time = time.time()  
vremya = end_time - start_time
vremya_format = f"{vremya:.6f} секунд"

print (array)
print (vremya_format)