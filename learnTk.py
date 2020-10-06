from tkinter import *
import numpy as np
import time        
window=Tk()
window.title("Game of life ")
my_canvas=Canvas(window,width=10000,height=10000)
my_canvas.grid(row=0,column=0)
j,m,n=0,0,0
emplacement={}
tab_place = [[0 for i in range(148)] for j in range(148)]
while(j<1480):
    i=0
    n=0 
    while(i<1480):
        """coord contient respectivement les valeurs x1,y1,x2,y2 
        color=0 =>white """
        emplacement={"coord":[i,j,i+10,j+10],"state":0,"alive":False}
        tab_place[m][n]=emplacement
        my_canvas.create_rectangle(i,j,i+10,j+10)
        i+=10
        n+=1
    j+=10
    m+=1
def isAlive(m,n,mat):
    if mat[m][n]["state"]==1:
        return True
    else:
        return False
def getAliveCells(mat):
    nbr=0
    for m in range(len(mat)):
        for n in range(len(mat[0])):
             if isAlive(m,n,mat):
                 nbr+=1
    return nbr
    
def color_rectangle(m,n,color,mat):
    
    x1,y1,x2,y2=mat[m][n]['coord'][0],mat[m][n]['coord'][1],mat[m][n]['coord'][2],mat[m][n]['coord'][3]
    my_canvas.create_rectangle(x1,y1,x2,y2,fill=color)
    if color=="black":
        mat[m][n]["state"]=1
    else:
        mat[m][n]["state"]=0
def getNeighbours(m,n,mat):
     return [(i,j) for i in range(m-1,m+2)
             for j in range(n-1,n+2)
             if (i!=m or j!=n) and (i>=0 and i<len(mat) and j>=0 and j<len(mat[0]))
             ]
def number_neighbours_alive(m,n,mat):
    nbrCellsAlive=0
    for neighbour in getNeighbours(m,n,mat):
        if mat[neighbour[0]][neighbour[1]]["state"]==1:
            nbrCellsAlive+=1
    return nbrCellsAlive
    
def nextState(m,n,mat,alive_cells,death_cells):
    nbrCellsAlive= number_neighbours_alive(m,n,mat)   
    if nbrCellsAlive==3 and mat[m][n]["state"]==0:
        mat[m][n]["alive"]=True
        alive_cells.append((m,n))
    if mat[m][n]["state"]==1:
        if (nbrCellsAlive==2 or nbrCellsAlive==3):
            mat[m][n]["alive"]=True
            alive_cells.append((m,n))
        else:
            mat[m][n]["alive"]=False
            death_cells.append((m,n))
#structure complexe
# color_rectangle(39,74,"#00ff00",tab_place)
# color_rectangle(40,74,"#00ff00",tab_place)
# color_rectangle(39,75,"#00ff00",tab_place)
# color_rectangle(40,73,"#00ff00",tab_place)
# color_rectangle(41,72,"#00ff00",tab_place)
# color_rectangle(41,73,"#00ff00",tab_place)
            
#structure tres complexe
color_rectangle(42,75,"black",tab_place)
color_rectangle(41,74,"black",tab_place)
color_rectangle(41,75,"black",tab_place)
color_rectangle(41,76,"black",tab_place)
color_rectangle(39,73,"black",tab_place)
color_rectangle(39,74,"black",tab_place)
color_rectangle(39,75,"black",tab_place)
color_rectangle(37,71,"black",tab_place)
color_rectangle(37,72,"black",tab_place)
color_rectangle(35,71,"black",tab_place)
            
""" structure stable legerement modifier
color_rectangle(20,36,"black",tab_place)
color_rectangle(19,37,"black",tab_place)
color_rectangle(21,36,"black",tab_place)
color_rectangle(22,37,"black",tab_place)
color_rectangle(21,38,"black",tab_place)
color_rectangle(20,38,"black",tab_place)
color_rectangle(19,38,"black",tab_place) """
counter = IntVar()
counter.set(0)
my_canvas.pack()
counterObj = my_canvas.create_text((670,20), text=counter.get(),fill="red",font=("Helvetica", 35))
    
for i in range(2000):
    alive_cells=[]
    death_cells=[]
    [nextState(m,n,tab_place,alive_cells,death_cells) for m in range(len(tab_place))
                             for n in range(len(tab_place[0]))]
    for position in alive_cells:
        color_rectangle(*(position),"black",tab_place)
    for position in death_cells:
        color_rectangle(*(position),"white",tab_place)
    counter.set(i)
    my_canvas.itemconfig(counterObj,text=counter.get())
    window.update()                            
window.mainloop()
