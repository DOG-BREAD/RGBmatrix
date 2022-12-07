#!/usr/bin/env python
from samplebase import SampleBase
from PIL import Image
import itertools
import time
class SimpleSquare(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        
        im = Image.open('pop.gif')
        self.matrix.brightness =75
        
        #print(pix)
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
            
            
            for z in range(0, im.n_frames ): #needs to go back to frame , check reading sequences
                im.seek(z)
                counter =0
                imrgb = im.convert("RGB")
                pixels = list(imrgb.getdata())
                #print(im.n_frames)
                pix = list(itertools.chain.from_iterable(pixels))
                for y in range(0,32):
                    for x in range(0,32):
                        offset_canvas.SetPixel(x, y, pix[counter],pix[counter + 1],pix[counter + 2])
                        counter +=3
                offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
                
                time.sleep(.14)
        

# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    if (not simple_square.process()):
        simple_square.print_help()
