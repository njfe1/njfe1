import pygame
import time
import math
pygame.init()
bg_width = 800
bg_height = 600
sc = pygame.display.set_mode((bg_width,bg_height))
sc.fill((255,255,255))
pygame.display.set_caption("lifegame")
pygame.display.update()
class Game():
    def __init__(self):
        self.matrix_l = 10
        self.list0 = []
        self.list1 = []
        self.userinputflag=False
        self.i = 0
        self.list01 = [self.list0,self.list1]
    def listinit(self):
        self.i = 0
        self.list0.clear()
        self.list1.clear()
        for a in range(0,int((bg_width/self.matrix_l)*(bg_height/self.matrix_l))):
            self.list0.append(0)
            self.list1.append(0)
    def user_input(self):
        mouse_x,mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                matrix_index = int((math.ceil((mouse_y+1)/self.matrix_l-1))*bg_width/self.matrix_l+math.ceil((mouse_x+1)/self.matrix_l)-1)
                matrix_key = self.list0[matrix_index]
                self.list0[matrix_index]=abs(matrix_key-1)
                rect_rgb = 255 - self.list0[matrix_index]*255
                pygame.draw.rect(sc,(rect_rgb,rect_rgb,rect_rgb),((matrix_index%(bg_width/self.matrix_l))*self.matrix_l,int(matrix_index/(bg_width/self.matrix_l))*self.matrix_l,self.matrix_l,self.matrix_l))
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.userinputflag = True   

    def gaming(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
        for m_index,m_key in enumerate(self.list01[self.i]):
            n = 0
            mathlist = [m_index-1,m_index+1,m_index-(bg_width/self.matrix_l),m_index-(bg_width/self.matrix_l)-1,
            m_index-(bg_width/self.matrix_l)+1,m_index+(bg_width/self.matrix_l),m_index+(bg_width/self.matrix_l)-1,
            m_index+(bg_width/self.matrix_l)+1]
            for b in range(0,8):
                c=int(mathlist[b])
                if c < 0:
                    continue
                else:
                    try:
                        if self.list01[self.i][c] == 1:
                            n+=1
                    except:
                        continue
            if n < 2:
                self.list01[abs(self.i-1)][m_index] = 0
            elif n == 2:
                self.list01[abs(self.i-1)][m_index] = m_key
            elif n == 3:
                self.list01[abs(self.i-1)][m_index] = 1
            elif n > 3:
                self.list01[abs(self.i-1)][m_index] = 0

        for draw_index , draw_key in enumerate(self.list01[abs(self.i - 1)]):
            if draw_key == 1:
                pygame.draw.rect(sc,(0,0,0),((draw_index%(bg_width/self.matrix_l))*self.matrix_l,int(draw_index/(bg_width/self.matrix_l))*self.matrix_l,self.matrix_l,self.matrix_l))
            elif draw_key == 0:
                pygame.draw.rect(sc,(255,255,255),((draw_index%(bg_width/self.matrix_l))*self.matrix_l,int(draw_index/(bg_width/self.matrix_l))*self.matrix_l,self.matrix_l,self.matrix_l))
        pygame.display.update()
        self.i = abs(self.i - 1)
        if self.list0 == self.list1:
            Game.listinit(self)
            sc.fill((255,255,255))
            pygame.display.update()
            game.userinputflag = False
        time.sleep(1)

game = Game()
game.listinit()
while True:
    
    if game.userinputflag == False:
        game.user_input()
    elif game.userinputflag == True:
        game.gaming()
