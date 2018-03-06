import numpy as np

def danger_distance(x,y,badmask):

    ydim1, xdim1 = badmask.shape
    #padarray = np.pad(badmask, (1,1), mode='constant')
    ydim = ydim1-2
    xdim = xdim1-2
    padarray = badmask
    xedges = np.zeros((ydim+1,xdim))
    yedges = np.zeros((ydim,xdim+1))

    #Define horizontal edge array
    for i in range(xdim):
        for j in range(ydim):
            #top edge
            xedges[j,i]=padarray[(j+1)-1,(i+1)]-padarray[(j+1),(i+1)]
            #bottom edge
            xedges[j+1,i]=padarray[(j+1)+1,(i+1)]-padarray[(j+1),(i+1)]

    #Define vertical edge array
    for i in range(xdim):
        for j in range(ydim):
            #top edge
            yedges[j,i]=padarray[(j+1),(i+1)-1]-padarray[(j+1),(i+1)]
            #bottom edge
            yedges[j,i+1]=padarray[(j+1),(i+1)+1]-padarray[(j+1),(i+1)]

    danger_dist = distance(x,y,xedges,yedges)

    return danger_dist

def distance(xa,ya,xedge,yedge):

    totdist = 0
    for y1 in range(xedge.shape[0]):
        for x1 in range(xedge.shape[1]):
            if(xedge[y1,x1]!=0):
                xd = (x1)-(xa)
                yd = (y1-0.5)-(ya)
                #print(xd,yd)
                dist = (xd**2.0+yd**2.0)**0.5
                #print(dist)
                totdist +=dist
                #print(totdist)
    for y1 in range(yedge.shape[0]):
        for x1 in range(yedge.shape[1]):
            if(yedge[y1,x1]!=0):
                xd = (x1-0.5)-(xa)
                yd = (y1)-(ya)
                #print(xd,yd)
                dist = (xd**2.0+yd**2.0)**0.5
                #print(dist)
                totdist +=dist
                #print(totdist)
        
    return totdist