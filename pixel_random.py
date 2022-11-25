from PIL import Image
import os
import random
class Pixel():
    initflag = False
    def __init__(self):
        self.matrix_size = 1

        self.matrix_pixel_random = []
        self.pixel_random_list = []
        
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
        matrixnum = int((img_height * img_width) / self.matrix_size**2)
        for i in range(0,matrixnum):
            self.pixel_random_list.append(random.randint(0,self.matrix_size**2-1))
        mwn = img_width/self.matrix_size 
        for mn, mi in enumerate(self.pixel_random_list):
            self.matrix_pixel_random.append(img.getpixel(((mn%mwn)*self.matrix_size+mi%self.matrix_size,int(mn/mwn)*self.matrix_size+int(mi/self.matrix_size))))
                
        


        for matrix_index , rect_rgb in enumerate(self.matrix_pixel_random):
            draw_xs = int((matrix_index%(img_width/self.matrix_size))*self.matrix_size)
            draw_xe = int((matrix_index%(img_width/self.matrix_size))*self.matrix_size + self.matrix_size)
            draw_ys = int(matrix_index/(img_width/self.matrix_size))*self.matrix_size
            draw_ye = int(matrix_index/(img_width/self.matrix_size))*self.matrix_size + self.matrix_size
            for draw_x in range(draw_xs, draw_xe):
                for draw_y in range(draw_ys, draw_ye):
                    img.putpixel((draw_x,draw_y),rect_rgb)
        name , fileback = os.path.splitext(self.im_address)
        img.save(name + "pixel_random" + fileback)
pixel = Pixel()
if __name__ == "__main__":
    while 1:
        pixel.user_input()
        pixel.impixel()

            
                
           