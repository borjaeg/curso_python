import random

def bubble_sort(items):
	""" Implementation of bubble sort
		More Info: http://en.wikipedia.org/wiki/Bubble_sort
	"""
	for i in range(len(items)):
		for j in range(len(items)-1-i):
			if items[j] > items[j+1]:
				items[j], items[j+1] = items[j+1], items[j]

def insertion_sort(items):
	""" Implementation of insertion sort
		More Info: http://en.wikipedia.org/wiki/Insertion_sort
	"""
	for i in range(1, len(items)):
		j = i
		while j > 0 and items[j] < items[j-1]:
			items[j], items[j-1] = items[j-1], items[j]
			j -= 1

random_items = [random.randint(-50,100) for c in range(5000)]

import time

start_time = time.time()

bubble_sort(random_items)

end_time = time.time()
secs = end_time - start_time * 1.0

random_items = [random.randint(-50,100) for c in range(5000)]
start_time_b = time.time()

insertion_sort(random_items)

end_time_b = time.time()
secs_b = end_time_b - start_time_b * 1.0

random_items = [random.randint(-50,100) for c in range(5000)] #1000000
start_time_c = time.time()

random_items.sort()

end_time_c = time.time()
secs_c = end_time_c - start_time_c * 1.0

print "Bubble sort ha tartado %.2f segundos" % secs
print "Insertion sort ha tardado %.2f segundos" % secs_b
print "Python sort ha tardado %.2f segundos" % secs_c