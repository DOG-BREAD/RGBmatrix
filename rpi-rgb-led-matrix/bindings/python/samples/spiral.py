#!/usr/bin/env python
from samplebase import SampleBase
import random
import time

class SimpleSquare(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        while True:
            """for x in range(0, self.matrix.width):
                offset_canvas.SetPixel(x, x, 255, 255, 255)
                offset_canvas.SetPixel(offset_canvas.height - 1 - x, x, 255, 0, 255)

            for x in range(0, offset_canvas.width):
                offset_canvas.SetPixel(x, 0, 255, 0, 0)
                offset_canvas.SetPixel(x, offset_canvas.height - 1, 255, 255, 0)

            for y in range(0, offset_canvas.height):
                offset_canvas.SetPixel(0, y, 0, 0, 255)
                 offset_canvas.SetPixel(offset_canvas.width - 1, y, 0, 255, 0)"""
            x=0
            y=0
            z=0
            startx =0
            starty =0
            endx = self.matrix.height
            endy =self.matrix.height
            
            while(True):
                for x in range(startx, endx ):
                    offset_canvas.SetPixel(x,y,0,255,255)
                    time.sleep(.005)     
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                for y in range(starty, endy ):
                    offset_canvas.SetPixel(x,y,255,0,255)
                    time.sleep(.005)     
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                for x in range( endx, startx-1 , -1 ):
                    offset_canvas.SetPixel(x,y,255,255,0)
                    time.sleep(.005)     
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                for y in range( endy, starty, -1 ):
                    offset_canvas.SetPixel(x,y,255,0,0)
                    time.sleep(.005)     
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                startx += 1
                starty +=1
                endx -=1
                endy -=1
            """for y in range(0 , self.matrix.width,1):
                #offset_canvas.SetPixel(x,y,random.randint(0,255),random.randint(0,255),random.randint(0,255))
                
                    #time.sleep(.1)
                    if(x == self.matrix.height -1):
                        for z in range(y, self.matrix.width):
                            offset_canvas.SetPixel(x,z,random.randint(0,255),random.randint(0,255),random.randint(0,255))
                            time.sleep(.05)     
                            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                        
                for x in range( self.matrix.height,0,-1 ):
                    offset_canvas.SetPixel(x,z,random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    time.sleep(.05)     
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)        
                    
                    if(x == 0):
                        for z in range(y, 0,-1):
                            offset_canvas.SetPixel(x,z,random.randint(0,255),random.randint(0,255),random.randint(0,255))
                            time.sleep(.05)     
                            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                """
                

# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    if (not simple_square.process()):
        simple_square.print_help()
