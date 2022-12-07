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
                offset_canvas.SetPixel(offset_canvas.width - 1, y, 0, 255, 0)
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
"""
            for x in range(0 , self.matrix.width):
                for y in range(0, self.matrix.height ):
                    offset_canvas.SetPixel(x,y,48,55,55)
                
            ranx = random.sample(range(0,self.matrix.width),10)
            rany = random.sample(range(0,self.matrix.width),10)
            for x in range(0, 10):
                offset_canvas.SetPixel(ranx[x],rany[x],255,255,255)
                if(ranx[x] >=2 and ranx[x] <29 ):
                    offset_canvas.SetPixel(ranx[x]+1,rany[x]+1,255,255,255)
                    offset_canvas.SetPixel(ranx[x]-1,rany[x]+1,255,255,255)
                    
                    if(rany[x] >=2 and rany[x] <29 ):
                         offset_canvas.SetPixel(ranx[x]-1,rany[x]-1,255,255,255)
                         offset_canvas.SetPixel(ranx[x]+1,rany[x]-1,255,255,255)
            for x in range(0,5):
                self.matrix.brightness = random.randint(0,101)
                if(((ranx[1]+x >= 0 and ranx[1]+x < self.matrix.width) or (rany[1]+x >= 0 and rany[1]+x < self.matrix.width)) or
                   ((ranx[2]+x >= 0 and ranx[2]+x < self.matrix.width) or (rany[2]+x >= 0 and rany[2]+x < self.matrix.width))):
                    offset_canvas.SetPixel(ranx[1]+x,rany[1]+x,255,255,255)
                    offset_canvas.SetPixel(ranx[2]-x,rany[2]+x,255,255,255)
                    offset_canvas.SetPixel(ranx[1]+x,rany[1]-x,255,255,255)
                    offset_canvas.SetPixel(ranx[2]-x,rany[2]-x,255,255,255)
                    offset_canvas.SetPixel(ranx[3]+x,rany[1]+x,255,255,255)
                    offset_canvas.SetPixel(ranx[2]-x,rany[3]+x,255,255,255)
                    offset_canvas.SetPixel(ranx[3]+x,rany[1]-x,255,255,255)
                    offset_canvas.SetPixel(ranx[2]-x,rany[2]-x,255,255,255)
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                    time.sleep(.1)
                    
# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    if (not simple_square.process()):
        simple_square.print_help()
