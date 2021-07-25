import random
from math import sqrt
import pygame
from math import ceil, floor
pygame.init()
pygame.font.init()
class Board:
    def __init__(self, screen, quan):
        self.quan = int(sqrt(quan))
        self.width = screen
        self.height = screen
        self.board = [[0] * int(sqrt(quan)) for _ in range(int(sqrt(quan)))]
        self.cell_size = screen / int(sqrt(quan))
    def render(self, screen):
        cnt = 0
        for i in range(self.quan):
            for j in range(self.quan):
                x = random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                if x[0] == 4:
                    pygame.draw.rect(screen, 'red', (self.cell_size * i, self.cell_size * j, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(screen, 'white',(self.cell_size * i, self.cell_size * j, self.cell_size, self.cell_size),1)
    def get_coord(self, mouse_pos):
        ans = ()
        ans = x, y = floor(mouse_pos[0]/self.cell_size), floor(mouse_pos[1]/self.cell_size)
        return ans
    def get_click(self, mouse_pos):
        cell = self.get_coord(mouse_pos)
        self.on_click(cell, mouse_pos)
    def on_click(self, cell, mouse_pos):
        cnt = 0
        color = screen.get_at(pygame.mouse.get_pos())
        if color != (255, 0, 0, 255):
            if cell[0] - 1 >= 0:
                color_cell_l = screen.get_at((mouse_pos[0] - int(self.cell_size), mouse_pos[1]))
                if color_cell_l == (255, 0, 0, 255):
                    cnt+=1
            if cell[0] - 1 >= 0 and cell[1] - 1 >= 0:
                color_cell_lu = screen.get_at((mouse_pos[0] - int(self.cell_size), mouse_pos[1] - int(self.cell_size)))
                if color_cell_lu == (255, 0, 0, 255):
                    cnt+=1
            if cell[1] - 1 >= 0:
                color_cell_u = screen.get_at((mouse_pos[0], mouse_pos[1] - int(self.cell_size)))
                if color_cell_u == (255,0,0,255):
                    cnt+=1
            if cell[0] + 1 <= self.quan-1 and cell[1] - 1 >= 0:
                color_cell_ru = screen.get_at((mouse_pos[0] + int(self.cell_size), mouse_pos[1] - int(self.cell_size)))
                if color_cell_ru == (255,0,0,255):
                    cnt+=1
            if cell[0] + 1 <= self.quan-1:
                color_cell_r = screen.get_at((mouse_pos[0] + int(self.cell_size), mouse_pos[1]))
                if color_cell_r == (255, 0, 0, 255):
                    cnt+=1
            if cell[0] + 1 <= self.quan-1 and cell[1] + 1 <= self.quan-1:
                color_ceil_rd = screen.get_at((mouse_pos[0] + int(self.cell_size), mouse_pos[1] + int(self.cell_size)))
                if color_ceil_rd == (255,0,0,255):
                    cnt+=1
            if cell[1] + 1 <= self.quan - 1:
                color_ceil_d = screen.get_at((mouse_pos[0] , mouse_pos[1] + int(self.cell_size)))
                if color_ceil_d == (255, 0,0, 255):
                    cnt +=1
            if cell[0] - 1 >= 0 and cell[1] + 1 <= self.quan - 1:
                color_ceil_ld = screen.get_at((mouse_pos[0] - int(self.cell_size), mouse_pos[1] + int(self.cell_size)))
                if color_ceil_ld == (255, 0, 0, 255):
                    cnt+=1
            f1 = pygame.font.Font(None, 16)
            text1 = f1.render(f'{cnt}', 1, (255, 255, 255)) 
            screen.blit(text1, (mouse_pos[0], mouse_pos[1]))
board = Board(200, 100)
size = w, h = 200, 200
mines = 8
screen = pygame.display.set_mode(size)
running = True
screen.fill((0, 0, 0))
board.render(screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    pygame.display.flip()
