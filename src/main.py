import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.label import Widget
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.clock import Clock
from kivy.config import Config
import random

class Game(Widget):
    def __init__(self,**kwargs) -> None:
        super(Game,self).__init__(**kwargs)
        self.init()
        Clock.schedule_interval(self._tic,0.1)

    def _tic(self,dt):
        self.update(dt)
        self.draw(dt)

    def init(self):
        self.nx=40
        self.ny=40
        if Window.width >= Window.height:
            self.w = self.h = int(Window.height / self.ny)
            self.nx = int(Window.width / self.w)
        else:
            self.w = self.h = int(Window.width / self.nx)
            self.ny = int(Window.height / self.h)
        self.n = self.nx*self.ny
        self.a=[]
        self.b=[]
        for i in range(0,self.n):
            self.a.append(0)
            self.b.append(0)
        for i in range(0,self.n//10):
            self.a[random.randint(0,self.n-1)]=1
        self.draw(0)

    def update(self,dt):
        alive=0
        for i in range(0,self.n):
            (x,y) = self.pos(i)
            neighbors = self.neighbors(x,y)
            if self.a[i] == 0:
                if neighbors==3:
                    self.b[i] = 1
                    alive += 1
                else:
                    self.b[i] = 0
            else:
                if neighbors==2 or neighbors==3:
                    self.b[i] = 1
                    alive+=1
                else:
                    self.b[i] = 0
        c=self.a
        self.a=self.b
        self.b=c

    def pos(self, i):
        x =  i % self.nx
        y =  i // self.nx 
        return (x,y)

    def get(self,x,y):
        x = x % self.nx
        y = y % self.ny
        return self.a[y * self.nx + x]

    def neighbors(self,x,y):
        return self.get(x-1,y-1) + self.get(x,y-1) + self.get(x+1,y-1) \
             + self.get(x-1,y) + self.get(x+1,y) \
             + self.get(x-1,y+1) + self.get(x,y+1) + self.get(x+1,y+1)

    def pixel_pos(self, i):
        (x,y)=self.pos(i)
        x *= self.w
        y *= self.h
        return (x,y)

    def draw(self,dt):
        self.canvas.clear()
        with self.canvas:
            Color(1,0,0,1)
            for i in range(0,self.n):
                if self.a[i]!=0:
                    Rectangle(size=(self.w,self.h),pos=self.pixel_pos(i))

class MyApp(App):

    def build(self):
        #Config.fullscreen="auto"
        return Game()

if __name__ == "__main__":
    Window.fullscreen="auto"
    Window.maximize()
    MyApp().run()

