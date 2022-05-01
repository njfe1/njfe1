from PIL import Image
import os
class Pixel():
    def __init__(self):
        self.im_address = 0
        self.matrix_size = 0
        self.pixel_rgb_list = []
        self.matrix_rgb_dict = {}
        self.matrix_pixel_max = []
    def user_input(self):
        
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
            for a in range(int((matrix%(img_width/self.matrix_size))*self.matrix_size) , int((matrix%(img_width/self.matrix_size))*self.matrix_size + self.matrix_size)):
                for b in range(int(matrix/(img_width/self.matrix_size))*self.matrix_size , int(matrix/(img_width/self.matrix_size))*self.matrix_size + self.matrix_size):
                    if self.pixel_rgb_list[b * img_width + a] not in self.matrix_rgb_dict:
                        self.matrix_rgb_dict[self.pixel_rgb_list[b * img_width + a]] = 1
                    elif self.pixel_rgb_list[b * img_width + a] in self.matrix_rgb_dict:
                        self.matrix_rgb_dict[self.pixel_rgb_list[b * img_width + a]] += 1
                    if a == int((matrix%(img_width/self.matrix_size))*self.matrix_size + self.matrix_size) - 1 and b == int(matrix/(img_width/self.matrix_size))*self.matrix_size + self.matrix_size - 1:
                        self.matrix_pixel_max.append(max(self.matrix_rgb_dict))

        for matrix_index , rect_rgb in enumerate(self.matrix_pixel_max):
            for draw_x in range(int((matrix_index%(img_width/self.matrix_size))*self.matrix_size) , int((matrix_index%(img_width/self.matrix_size))*self.matrix_size + self.matrix_size)):
                for draw_y in range(int(matrix_index/(img_width/self.matrix_size))*self.matrix_size , int(matrix_index/(img_width/self.matrix_size))*self.matrix_size + self.matrix_size):
                    img.putpixel((draw_x,draw_y),rect_rgb)
        name , fileback = os.path.splitext(self.im_address)
        img.save(name + "pixel3" + fileback)
pixel = Pixel()
if __name__ == "__main__":
    pixel.user_input()
    pixel.impixel()
