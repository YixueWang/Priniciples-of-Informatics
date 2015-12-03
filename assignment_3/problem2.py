# Functions for students to implement.

# Performs search in unsorted L.
# L might not be sorted. Can't use sorting to solve this.
def searchGreaterNotSorted(L, v):
	n = 0
	for i in L:
		if i > v:
			n = n + 1
	return n


# Performs search in sorted L (ascending order).
# L is sorted.
def searchGreaterSorted(L, v):
  n = 0
  for i in range(len(L)):
    if L[i] > v:
      n = len(L[i:])
      break
  return n


# Performs binary search in sorted L (ascending order).
def searchGreaterBinSearch(L, v):
  low = 0
  high = len(L)
  while low < high:
    mid = (low + high) // 2
    if L[mid] < v:
      mid = mid +1
      low = mid
    elif L[mid] > v:
      high = mid
    else:
      while mid != len(L)-1:
        mid +=1
        while L[mid] == v:
          if mid = len(L) -1:
            return 0
  return len(L[mid:])


  		

# Performs range search in sorted L (ascending order).
def searchInRange(L, v1, v2):
  n = searchGreaterBinSearch(L, v1) - searchGreaterBinSearch(L, v2)
  return n 
