import pygame as pg

class Figura:
    def __init__(self,pos_x,pos_y,color=(255,255,255),w=20,h=20,radio=10,vx=1,vy=1):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.color=color
        self.w=w
        self.h=h
        self.radio=radio
        self.vx=vx 
        self.vy=vy

    
    def moverCirculo(self,xmax,ymax):
        self.pos_x += self.vx
        self.pos_y += self.vy
        if self.pos_x >= xmax or self.pos_x <= 0:#los limites en x
            self.vx *= -1
        if self.pos_y >= ymax or self.pos_y <=0:#los limites en y
            self.vy *= -1

    def dibujarCirculo(self,pantalla):        
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y),self.radio)      

    def moverRectangulo(self,xmax,ymax):
        self.pos_x += self.vx
        self.pos_y += self.vy
        if self.pos_x >= xmax or self.pos_x <= 0:#los limites en x
            self.vx *= -1
        if self.pos_y >= ymax or self.pos_y <=0:#los limites en y
            self.vy *= -1

    def dibujarRectangulo(self,pantalla):
        pg.draw.rect(pantalla,self.color,(self.pos_x,self.pos_y,self.w,self.h )) 
