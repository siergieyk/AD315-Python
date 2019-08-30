# Task 1

binarray = [1, 3, 7, 10, 33, 44, 88, 99, 101, 134, 155, 187, 204, 233, 256,
301, 333, 350, 401, 420, 450, 467, 477, 499, 500, 501, 503, 522, 555, 577, 
601, 603, 630, 640, 660, 799, 831, 931, 1043, 1099, 1134, 1281, 1421, 1500]
num = 1421
times = []

def binarySearchIt(binarray, l, r, num): 
  
  while l <= r: 
      mid = l + (r - l)/2; 
      if binarray[int(mid)] == num: 
          return mid 
      elif binarray[int(mid)] < num: 
          l = mid + 1
      else: 
          r = mid - 1

def binarySearchRec (binarray, l, r, num): 
  
  if r >= l: 
      mid = l + (r - l)/2
      if binarray[int(mid)] == num: 
          return mid 
      elif binarray[int(mid)] > num: 
          return binarySearchRec(binarray, l, mid-1, num) 
      else: 
          return binarySearchRec(binarray, mid + 1, r, num)




# Task 2

import random

bublist = [i for i in range(10000)] 
random.shuffle(bublist)
randlist = bublist

def BubSortIt(num):

  
  
  sorted = []


  for i in range(len(randlist) - 1, 0, -1):
        for j in range(i):
            if randlist[j] > randlist[j + 1]:
                randlist[j], randlist[j + 1] = randlist[j + 1], randlist[j]
  print(randlist)


def bubSortRec(bublist): 
  for i, num in enumerate(bublist): 
        try: 
            if bublist[i+1] < num: 
                bublist[i] = bublist[i+1] 
                bublist[i+1] = num 
                bubSortRec(bublist) 
        except IndexError: 
            pass
  return bublist
  



# Task 3
print("\nTask 1a")
import time 
start_time = time.time()

result = binarySearchIt(binarray, 0, len(binarray)-1, num)

endtime_bin_iter = time.time() - start_time

print("For number:",str(num)+", Index: ", int(result)) 

print("\nTask 1b")
import time 
start_time = time.time()

result = binarySearchRec(binarray, 0, len(binarray)-1, num) 

endtime_bin_rec = time.time() - start_time
print("For number:",str(num)+", Index: ", int(result)) 

print("\nTask 2a")

import time 
start_time = time.time()

BubSortIt(bublist)

endtime_bub_iter = time.time() - start_time



print("\nTask 2b")
import time 
start_time = time.time()
print(bubSortRec(bublist))

endtime_bub_rec = time.time() - start_time

print("\nTask3")
print("\n                   Iterative                Recursive")
print("Binary Search        ",endtime_bin_iter, "   ",endtime_bub_rec)
print("Bubble Sort          ",endtime_bub_iter,"     ",endtime_bin_rec)
