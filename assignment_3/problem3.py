# Functions for students to implement.

naive = []
def buildNaive(points,n):
    del naive[:] #erasing previous data
    #your code here
    for i in points:
        naive.append(i)
    return naive

onedim = []
def buildOneDim(points,n):
    del onedim[:] #erasing previous data
    #your code here
    for i in range(0,n):
        onedim.append([])
    for m in points:
        i = int(m[0]*n)
        onedim[i].append(m)

    return onedim

twodim = []
def buildTwoDim(points,n):
    del twodim[:] #erasing previous data
    #your code here    
    for i in range(0,n):
        twodim.append([])
        for a in range(0,n):
            twodim[i].append([])

    for m in points:
        col = int(m[0]*n)
        row = int(m[1]*n)
        twodim[col][row].append(m)

    return twodim




def queryNaive(x0, y0, x1, y1):
    count = 0
    #your code here
    for n in naive:
        if n[0]>=x0 and n[0] <= x1 and n[1] >= y0 and n[1] <=y1:
            count =+1
    return count

def queryOneDim(x0, y0, x1, y1):
    count = 0
    n = len(onedim)
    index0 = int(x0*n)
    index1 = int(x1*n)
    #your code here
    for tokens in onedim[index0:index1+1]:
        for i in tokens:
            x = i[0]
            y = i[1]
            if x >= x0 and y >= y0 and x<= x1 and y <= y1:
                count +=1
    return count

def queryTwoDim(x0, y0, x1, y1):
    count = 0
    n = len(twodim)
    index_x0 = int(x0*n)
    index_x1 = int(x1*n)
    index_y0 = int(y0*n)
    index_y1 = int(y1*n)
    for tokens in twodim[index_x0:index_x1+1]:
        for lines in tokens[index_y0:index_y1+1]:
            for i in lines:
                x = i[0]
                y = i[1]
                if x >= x0 and y>= y0 and x <= x1 and y <= y1:
                    count +=1
    return count
