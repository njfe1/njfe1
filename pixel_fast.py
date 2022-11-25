from PIL import Image
import os
import sys
class Pixel():
    initflag = False
    def __init__(self):
        self.matrix_size = 1
        self.pixel_rgb_list = []

        
    def user_input(self):
        if self.initflag:
            self.__init__()
        self.im_address = input('image address:')
        
        
        sizelist = []
        img = Image.open(self.im_address)
        img_width , img_height = img.size
        if img_width > img_height:
            forrange = img_height
        else:
            forrange = img_width
        for i in range(1 , forrange):
            if img_height % i == 0 and img_width % i == 0:
                sizelist.append(i)
            else:
                continue
        print("size:",sizelist)
        self.matrix_size = int(input("size:"))
        self.initflag = True
    def impixel(self):
        print(self.im_address)
        print(self.matrix_size)
        img = Image.open(self.im_address)
        img = img.convert("RGB")
        img_width , img_height = img.size
        for gety in range(0,img_height,self.matrix_size):
            for getx in range(0,img_width,self.matrix_size):
                pixel_rgb = img.getpixel((getx,gety))
                self.pixel_rgb_list.append(pixel_rgb)

        

        for matrix_index , rect_rgb in enumerate(self.pixel_rgb_list):
            draw_xs = int((matrix_index%(img_width/self.matrix_size))*self.matrix_size)
            draw_xe = int((matrix_index%(img_width/self.matrix_size))*self.matrix_size + self.matrix_size)
            draw_ys = int(matrix_index/(img_width/self.matrix_size))*self.matrix_size
            draw_ye = int(matrix_index/(img_width/self.matrix_size))*self.matrix_size + self.matrix_size
            for draw_x in range(draw_xs, draw_xe):
                for draw_y in range(draw_ys, draw_ye):
                    img.putpixel((draw_x,draw_y),rect_rgb)
        name , fileback = os.path.splitext(self.im_address)
        img.save(name + "pixel_fast" + fileback)
pixel = Pixel()
if __name__ == "__main__":
    while 1:
        pixel.user_input()
        pixel.impixel()

            
                
           