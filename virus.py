from tkinter import *
import math
import random

canvas_width = 1600
canvas_height = 800

Graph = []
N = 12800
K = 100
Texts = []
blobs = []
Day = 0

DaysILL = 9
thanatos = 100
arrostia = 7

class node():
    def __init__(self,ver,days,h):
        self.vertex = ver
        self.days_ill = days
        self.health_condition = h 
        self.neighbours = []
        

def setGraph():
    global Graph
    global blobs
    for i in range (N):
        person = node(i,0,'healthy')
        Graph.append(person)

    with open("produced_graph.txt") as file:
        for line in file:
            x = line.split()
            node1 = int(x[0])
            node2 = int(x[1])
            Graph[node1].neighbours.append(node2)
            Graph[node2].neighbours.append(node1)
    
    Graph[0].health_condition = "ill"

def draw():
    root = Tk()
    global Texts

    w = Canvas(root, 
           width=canvas_width, 
           height=canvas_height)
    w.pack()
    Valx = 200
    Valy = 100
    sizey = canvas_height/Valy
    sizex = canvas_width/Valx

    for i in range(Valy):
        for j in range(Valx):
            if(i*Valx+j > N):
                break
            blobs.append(w.create_oval(sizex*j,sizey*i,sizex*(j+1),sizey*(i+1)) )
    print("valx",Valx,"valy",Valy)

    def Day():
        
        global Day 
        Day += 1
        print("Day ",Day)

        for i in range(len(Graph)):
            if(Graph[i].health_condition == 'ill'):
                Graph[i].days_ill += 1

                if(Graph[i].days_ill > DaysILL):
                    Graph[i].health_condition = 'curred'

                if(random.randint(0,thanatos) < 1):
                    Graph[i].health_condition = 'dead'

                for j in range(len(Graph[i].neighbours)):
                    if(random.randint(0,DaysILL) < 1 and Graph[Graph[i].neighbours[j]].health_condition == 'healthy' ):
                        #arrostise ton tin epomeni mera
                        Graph[Graph[i].neighbours[j]].health_condition = 'Nill'

            if(Graph[i].health_condition == 'Nill'):
                Graph[i].health_condition = 'ill'

        for i in range(N):

            if (Graph[i].health_condition == 'ill'):

                try:
                    # :(
                    w.itemconfigure(blobs[i], fill  = 'yellow')
                except StopIteration:
                    pass

            if (Graph[i].health_condition == 'curred'):

                try:
                    # :) 
                    w.itemconfigure(blobs[i], fill  = 'blue')
                except StopIteration:
                    pass
            
            if (Graph[i].health_condition == 'dead'):

                try:
                    #psofos 
                    w.itemconfigure(blobs[i], fill  = 'black')
                except StopIteration:
                    pass

    my_button = Button(root,
                   text = "New Day",
                   command = Day)

    my_button.pack()
    mainloop()


def produce():
    f = open("produced_graph.txt", "w") 

    for i in range( N - K):
        for j in range (random.randint(0,K)):
            f.write(str(i)+"  "+str(i+j+1)+"\n")

        
    f.close()



def popup():
    global K
    global N
    global thanatos
    global arrostia
    global DaysILL

    root = Tk()
    root.geometry("600x400")

    w = Canvas(root, width = 500, height = 350)

    w.create_text(100, 100, text = "Connections: " )
    connections = Entry( w, width = 10)
    connections.place(relx = 0.3,rely = 0.26)

    w.create_text(100, 130, text = "Number of victims (max 20000): " )
    victims = Entry( w, width = 10)
    victims.place(relx = 0.38,rely = 0.34)

    w.create_text(300, 100, text = "Days until victim is curred: " )
    cur = Entry( w, width = 10)
    cur.place(relx = 0.77,rely = 0.26)

    w.create_text(350, 130, text = "Chance of getting the virus, 1 in: " )
    II= Entry( w, width = 10)
    II.place(relx = 0.9,rely = 0.34)

    w.create_text(300, 160, text = "Chance of 💀☠️, 1 in: " )
    LOL = Entry( w, width = 10)
    LOL.place(relx = 0.77,rely = 0.42)

    w.pack()

    def enter():

        global K
        global N
        global thanatos
        global arrostia
        global DaysILL

        N = int(victims.get())
        K = int(connections.get())
        DaysILL = int(cur.get())
        arrostia = int(II.get())
        thanatos = int(LOL.get())

        root.destroy()
        

    my_button = Button(root,
                   text = "Start",
                   command = enter)
    
    my_button.pack()
    mainloop()

def main():
    
    popup()

    produce()

    setGraph()

    draw()
    
    
if __name__ == "__main__":
    main()