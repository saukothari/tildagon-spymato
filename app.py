import asyncio
import app
import math
from events.input import Buttons, BUTTON_TYPES
from app_components import clear_background


class SpymatoApp(app.App):
    def __init__(self):
        self.button_states = Buttons(self)
        self.start = 0
        self.tt_show = "SPYMATO"

        self.cateyerad = 8
        self.sign = -1
        self.eye_nimate = 300


        self.totalelapsed = 0

    def update(self, delta):
        self.totalelapsed+= delta
        if (self.totalelapsed>=self.eye_nimate):
            self.cateyerad +=self.sign
            if (self.cateyerad<=0):
                self.sign = 1
            if (self.cateyerad>=8):
                self.sign = -1
            self.totalelapsed=0
                
                
                
            
        print(delta)
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            # The button_states do not update while you are in the background.
            # Calling clear() ensures the next time you open the app, it stays open.
            # Without it the app would close again immediately.
            self.button_states.clear()
            self.minimise()

    def draw(self, ctx):

        clear_background(ctx)
        ctx.rgb(255,255,255)
        tw = ctx.text_width(self.tt_show)
        ctx.move_to(0-(tw/2), -60)
        ctx.text(self.tt_show)
        
        ctx.rgb(1, 0, 0).begin_path()
        

        ctx.move_to(0,0)
        ctx.quad_to(-30,-50, -50,0)
        ctx.fill()
        
        ctx.move_to(0,0)
        ctx.quad_to(30,-50, 50,0)
        ctx.fill()
        
        #ctx.move_to(0,20)
        ctx.arc(0,50, 59,0,2 * math.pi,True)
        ctx.fill()

        # left eye
        ctx.rgb(0,0,0).arc(-20,20, 15,0,2 * math.pi,True)
        ctx.fill()
        ctx.rgb(255,255,255).arc(-20,20, self.cateyerad,0,2 * math.pi,True)
        ctx.fill()

        # right eye
        ctx.rgb(0,0,0).arc(20,20, 15,0,2 * math.pi,True)
        ctx.fill()
        ctx.rgb(255,255,255).arc(20,20, self.cateyerad,0,2 * math.pi,True)
        ctx.fill()



        ctx.save()
        

       

        
        ctx.restore()

__app_export__ = SpymatoApp