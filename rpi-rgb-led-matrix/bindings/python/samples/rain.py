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
            for x in range(0 , self.matrix.width):
                for y in range(0, self.matrix.height ):
                    offset_canvas.SetPixel(x,y,10,10,130)
            for z in range(0,15):
                    self.matrix.brightness = 65
                    ranx = random.sample(range(0,self.matrix.width),15)
                    rany = random.sample(range(0,self.matrix.width),15)
                    for y in range(0 ,random.randint(1,8)):
                        if(ranx[z]+y > 0 and ranx[z]+y < 32):
                            if(rany[z]+y > 0 and rany[z]+y < 32):
                                offset_canvas.SetPixel(ranx[z]+y,rany[z]+y,random.randint(200,255),random.randint(100,150),random.randint(200,255))
                    
                    if(random.randint(1,1000) % 153 == 0):
                        self.matrix.brightness = 100
                        for q in range(0, self.matrix.width):
                            offset_canvas.SetPixel(ranx[1]+1,q,255,255,255)
                            if(random.randint(1,1000)% 271 == 0):
                                for g in range(0, self.matrix.width - q):
                                    if(g % 4 > 0):
                                        offset_canvas.SetPixel(ranx[1]+q+g,q,255,255,255)
                                       
                                    else:
                                        offset_canvas.SetPixel(ranx[1]+q-g,q,255,255,255)
                                        
                             
                    offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                    #time.sleep(.1)
                        
    
                
                

# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    if (not simple_square.process()):
        simple_square.print_help()
