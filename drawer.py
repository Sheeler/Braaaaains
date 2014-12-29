# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 21:32:17 2014

editors: Andrew Sheeler // Jenny Nitishinskaya // Maxwell Nye

This code will initiate a drawing window using the python module
Tkinter and save your drawing in temp.jpg in you current folder.
If temp.jpg already exists, it will be overwritten.

The majority of this code was created by Chris Aung. We found it
on github here: http://stackoverflow.com/questions/17915440/python-
                tkinter-save-canvas-as-image-using-pil
Our edits changed the window/pen size, and closes the window once
the drawing has been saved.
"""

import Tkinter as tk
import Image,ImageDraw


class ImageGenerator:
    def __init__(self,parent,posx,posy,*kwargs):
        self.root = root
        self.parent = parent
        self.posx = posx
        self.posy = posy
        self.sizex = 32
        self.sizey = 32
        self.b1 = "up"
        self.xold = None
        self.yold = None 
        self.drawing_area=tk.Canvas(self.parent,
                                    width=self.sizex,height=self.sizey)
        self.drawing_area.place(x=self.posx,y=self.posy)
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.b1down)
        self.drawing_area.bind("<ButtonRelease-1>", self.b1up)
        self.button=tk.Button(self.parent,text="Done!",
                              width=10,bg='white',command=self.save)
        self.button.place(x=self.sizex/7,y=self.sizey+20)
        self.button1=tk.Button(self.parent,text="Clear!",
                               width=10,bg='white',command=self.clear)
        self.button1.place(x=(self.sizex/7)+80,y=self.sizey+20)

        self.image=Image.new("RGB",(32,32),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)


    #Modify such that it saves and loads. 
    def save(self):
        filename = "temp.jpg"
        self.image.save(filename)
        root.destroy()

    def clear(self):
        self.drawing_area.delete("all")
        self.image=Image.new("RGB",(32,32),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)

    def b1down(self,event):
        self.b1 = "down"

    def b1up(self,event):
        self.b1 = "up"
        self.xold = None
        self.yold = None

    def motion(self,event):
        if self.b1 == "down":
            if self.xold is not None and self.yold is not None:
                event.widget.create_line(self.xold,
                                         self.yold,
                                         event.x,event.y,
                                         smooth='true',width=4,fill='blue')
                self.draw.line(((self.xold,self.yold),
                                (event.x,event.y)),(0,0,0),width=4)

        self.xold = event.x
        self.yold = event.y

if __name__ == "__main__":
    root=tk.Tk()
    root.wm_geometry("%dx%d+%d+%d" % (200, 200, 10, 10))
    root.config(bg='green')
    ImageGenerator(root,10,10)
    root.mainloop()
    
    