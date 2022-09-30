from PIL import Image
import os

class Pixel():
    initflag = False
    def __init__(self):
        self.matrix_size = 1
        self.pixel_rgb_list = []
        self.matrix_rgb_dict = {}
        self.matrix_pixel_max = []
        
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
        for y in range(0 , img_height):
            for x in range(0 , img_width):
                pixel_rgb = img.getpixel((x,y))
                self.pixel_rgb_list.append(pixel_rgb)
        
        for matrix in range(0 , matrixnum):
            self.matrix_rgb_dict = {}   
            ast = int((matrix%(img_width/self.matrix_size))*self.matrix_size)
            aed = int((matrix%(img_width/self.matrix_size))*self.matrix_size + self.matrix_size)
            bst = int(matrix/(img_width/self.matrix_size))*self.matrix_size
            bed = int(matrix/(img_width/self.matrix_size))*self.matrix_size + self.matrix_size
            end0 = int((matrix%(img_width/self.matrix_size))*self.matrix_size + self.matrix_size)-1
            end1 = int(matrix/(img_width/self.matrix_size))*self.matrix_size + self.matrix_size - 1
            for a in range(ast, aed):
                for b in range(bst, bed):
                    if self.pixel_rgb_list[b * img_width + a] not in self.matrix_rgb_dict:
                        self.matrix_rgb_dict[self.pixel_rgb_list[b * img_width + a]] = 1
                    elif self.pixel_rgb_list[b * img_width + a] in self.matrix_rgb_dict:
                        self.matrix_rgb_dict[self.pixel_rgb_list[b * img_width + a]] += 1
                    if a == end0 and b == end1:
                        self.matrix_pixel_max.append(max(self.matrix_rgb_dict))

        for matrix_index , rect_rgb in enumerate(self.matrix_pixel_max):
            draw_xs = int((matrix_index%(img_width/self.matrix_size))*self.matrix_size)
            draw_xe = int((matrix_index%(img_width/self.matrix_size))*self.matrix_size + self.matrix_size)
            draw_ys = int(matrix_index/(img_width/self.matrix_size))*self.matrix_size
            draw_ye = int(matrix_index/(img_width/self.matrix_size))*self.matrix_size + self.matrix_size
            for draw_x in range(draw_xs, draw_xe):
                for draw_y in range(draw_ys, draw_ye):
                    img.putpixel((draw_x,draw_y),rect_rgb)
        name , fileback = os.path.splitext(self.im_address)
        img.save(name + "pixel" + fileback)
pixel = Pixel()
if __name__ == "__main__":
    while 1:
        pixel.user_input()
        pixel.impixel()

            
                
           
