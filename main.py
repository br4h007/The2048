from tkinter import NE, Grid
import pygame
import random
from copy import deepcopy
pygame.init() 
pygame.font.init()
#create screen/ global variables
screen = pygame.display.set_mode((372, 372))
pygame.display.set_caption("2048")

#colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
GREEN = (0,255,0)

surf = pygame.image.load("C:\\Users\\SUMAN1708\\Desktop\\Python Projects\\2048\\Block2.png")
surf4 = pygame.image.load("C:\\Users\\SUMAN1708\\Desktop\\Python Projects\\2048\\Block4.png")
surf8 = pygame.image.load("C:\\Users\\SUMAN1708\\Desktop\\Python Projects\\2048\\Block8.png")
surf16 = pygame.image.load("C:\\Users\\SUMAN1708\\Desktop\\Python Projects\\2048\\Block16.png")
surf32 = pygame.image.load("C:\\Users\\SUMAN1708\\Desktop\\Python Projects\\2048\\Block32.png")
surf64 = pygame.image.load("C:\\Users\\SUMAN1708\\Desktop\\Python Projects\\2048\\Block64.png")
surf128 = pygame.image.load("C:\\Users\\SUMAN1708\\Desktop\\Python Projects\\2048\\Block128.png")
surf256 = pygame.image.load("C:\\Users\\SUMAN1708\\Desktop\\Python Projects\\2048\\Block256.png")
surf512 = pygame.image.load("C:\\Users\\SUMAN1708\\Desktop\\Python Projects\\2048\\Block512.png")
surf1024 = pygame.image.load("C:\\Users\\SUMAN1708\\Desktop\\Python Projects\\2048\\Block1024.png")
surf2048 = pygame.image.load("C:\\Users\\SUMAN1708\\Desktop\\Python Projects\\2048\\Block2048.png")

#dictionary
blocks = {2:surf, 
          4:surf4,
          8:surf8,
          16:surf16,
          32:surf32,
          64:surf64,
          128:surf128,
          256:surf256,
          512:surf512,
          1024:surf1024,
          2048:surf2048
          }

blocks[2]

BACKGROUND_COLOUR = (205, 192, 180)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRID_COLOUR = (187, 173, 160)

WON=False
LOST=False
x = 0

#grid definition
#[  0 ,  0 ,  0 ,  0]
GRID = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
        ]

#screen draw definitions
def draw_screen():
  global BACKGROUND_COLOUR
  global screen
  screen.fill(BACKGROUND_COLOUR)

def draw_grid():
  global screen

  #vertical lines
  for i in range(93, 372, 93):
    pygame.draw.line(screen, GRID_COLOUR, (i,0), (i,496), 17)
  #horizontal lines
  for j in range(93, 372, 93):
    pygame.draw.line(screen, GRID_COLOUR, (0,j), (496,j), 17)

def spawn():
  try:
    #test
    empty_slots = [(i, j)for i in range(4)for j in range(4)if not GRID[i][j]]
    spawn_place = random.choice(empty_slots)
    GRID[spawn_place[0]][spawn_place[1]] = 2

  except:
    pass

def map_values():
  global screen
  for i in range(4):
    for j in range(4):
      if GRID[i][j] == 0:
        continue
      screen.blit(blocks[GRID[i][j]], (j*93, i*93))

#push functions

def push_right():
  #label grid global so we can change it
  global GRID
  #create copy to represent new turn
  NEW_GRID = deepcopy(GRID)
  #move stuff right
  #choose row we are in
  for i in range(4):
    zero_count = 0
    #choose column
    for j in range(4):
      #find all zeros in each row
      if GRID[i][j] == 0:
        zero_count += 1
    #remove all the zeros in each row
    for _ in range(zero_count):
      GRID[i].remove(0)
    for _ in range(zero_count):
      GRID[i].insert(0,0)

  #try combine numbers
  for y in range(4):
  #index right 3 spots, right to left
    for x in range(3,0,-1):
      #if there is a duplicate square to the right
      if GRID[y][x] == GRID[y][x-1]:
        #promote block by 2
        GRID[y][x] *= 2
        #remove right block
        GRID[y].pop(x-1)
        GRID[y].insert(0,0)
  #check that turn ended
  if NEW_GRID == GRID:
    current_zeros = 0
    for i in range(4):
      #choose column
      for j in range(4):
        #find all zeros in each row
        if NEW_GRID[i][j] == 0:
          current_zeros += 1
    if current_zeros == 0:
      for i in range(4):
      #choose column
        for j in range(4):
          #find all zeros in each row
          if NEW_GRID[i][j] > 0:
            y = NEW_GRID[i][j]
            x += y
      imsotirednow = x+1
      run = False
      pygame.quit()
      exit()
      print("Your score is " + str(imsotirednow))
    elif current_zeros > 0:
      spawn()
      #score
      for i in range(4):
        #choose column
        for j in range(4):
          #find all zeros in each row
          if NEW_GRID[i][j] > 0:
            y = NEW_GRID[i][j]
            x += y
            imsotirednow = x + 1
      print("Your score is " + str(imsotirednow))
  elif NEW_GRID != GRID:
    spawn()
    #score
    for i in range(4):
      #choose column
      for j in range(4):
        #find all zeros in each row
        if NEW_GRID[i][j] > 0:
          y = NEW_GRID[i][j]
          x += y
          imsotirednow = x + 1
    print("Your score is " + str(imsotirednow))

def push_left():
  #label grid global so we can change it
  global GRID
  #create copy to represent new turn
  NEW_GRID = deepcopy(GRID)
  #move stuff right
  #choose row we are in
  for i in range(4):
    zero_count = 0
    #choose column
    for j in range(4):
      #find all zeros in each row
      if GRID[i][j] == 0:
        zero_count += 1
    #remove all the zeros in each row
    for _ in range(zero_count):
      GRID[i].remove(0)
    for _ in range(zero_count):
      GRID[i].append(0)

  #try combine numbers
  for y in range(4):
    #index right 3 spots, right to left
    for x in range(3):
      #if there is a duplicate square to the right
      if GRID[y][x] == GRID[y][x+1]:
        #promote block by 2
        GRID[y][x] *= 2
        #remove right block
        GRID[y].pop(x+1)
        GRID[y].append(0)
  #check that turn ended
  if NEW_GRID == GRID:
    current_zeros = 0
    for i in range(4):
      #choose column
      for j in range(4):
        #find all zeros in each row
        if NEW_GRID[i][j] == 0:
          current_zeros += 1
    if current_zeros == 0:
      for i in range(4):
      #choose column
        for j in range(4):
          #find all zeros in each row
          if NEW_GRID[i][j] > 0:
            y = NEW_GRID[i][j]
            x += y
      imsotirednow = x
      run = False
      pygame.quit()
      exit()
      print("Your score is " + str(imsotirednow))
    elif current_zeros > 0:
      spawn()
      #score
      for i in range(4):
        #choose column
        for j in range(4):
          #find all zeros in each row
          if NEW_GRID[i][j] > 0:
            y = NEW_GRID[i][j]
            x += y
            imsotirednow = x
      print("Your score is " + str(imsotirednow))
  elif NEW_GRID != GRID:
    spawn()
    #score
    for i in range(4):
      #choose column
      for j in range(4):
        #find all zeros in each row
        if NEW_GRID[i][j] > 0:
          y = NEW_GRID[i][j]
          x += y
          imsotirednow = x
    print("Your score is " + str(imsotirednow))

def push_down():
  #label grid global so we can change it
  global GRID
  #rotating the grid
  GRID_VERT = list(map(list, zip(*GRID)))
  #create copy to represent new turn
  NEW_GRID = deepcopy(GRID)
  #move stuff right
  #choose row we are in
  for i in range(4):
    zero_count = 0
    #choose column
    for j in range(4):
      #find all zeros in each row
      if GRID_VERT[i][j] == 0:
        zero_count += 1
    #remove all the zeros in each row
    for _ in range(zero_count):
      GRID_VERT[i].remove(0)
    for _ in range(zero_count):
      GRID_VERT[i].insert(0,0)

  #try combine numbers
  for y in range(4):
    #index right 3 spots, right to left
    for x in range(3,0,-1):
      #if there is a duplicate square to the right
      if GRID_VERT[y][x] == GRID_VERT[y][x-1]:
        #promote block by 2
        GRID_VERT[y][x] *= 2
        #remove right block
        GRID_VERT[y].pop(x-1)
        GRID_VERT[y].insert(0,0)
  #apply changes back to grid
  GRID = list(map(list, zip(*GRID_VERT)))  

def push_up():
  #label grid global so we can change it
  global GRID
  #rotating the grid
  GRID_VERT = list(map(list, zip(*GRID)))
  #create copy to represent new turn
  NEW_GRID = deepcopy(GRID)
  #move stuff right
  #choose row we are in
  for i in range(4):
    zero_count = 0
    #choose column
    for j in range(4):
      #find all zeros in each row
      if GRID_VERT[i][j] == 0:
        zero_count += 1
    #remove all the zeros in each row
    for _ in range(zero_count):
      GRID_VERT[i].remove(0)
    for _ in range(zero_count):
      GRID_VERT[i].append(0)

  #try combine numbers
  for y in range(4):
    #index right 3 spots, right to left
    for x in range(3):
      #if there is a duplicate square to the right
      if GRID_VERT[y][x] == GRID_VERT[y][x+1]:
        #promote block by 2
        GRID_VERT[y][x] *= 2
        #remove right block
        GRID_VERT[y].pop(x+1)
        GRID_VERT[y].append(0)
  #apply changes back to grid
  GRID = list(map(list, zip(*GRID_VERT)))  
  #check that turn ended
  if NEW_GRID == GRID:
    current_zeros = 0
    for i in range(4):
      #choose column
      for j in range(4):
        #find all zeros in each row
        if GRID_VERT[i][j] == 0:
          current_zeros += 1
    if current_zeros == 0:
      for i in range(4):
      #choose column
        for j in range(4):
          #find all zeros in each row
          if GRID_VERT[i][j] > 0:
            y = GRID_VERT[i][j]
            x += y
      imsotirednow = x
      run = False
      pygame.quit()
      exit()
      print("Your score is " + str(imsotirednow))
    elif current_zeros > 0:
      spawn()
      #score
      for i in range(4):
        #choose column
        for j in range(4):
          #find all zeros in each row
          if GRID_VERT[i][j] > 0:
            y = GRID_VERT[i][j]
            x += y
            imsotirednow = x
      print("Your score is " + str(imsotirednow))
  elif NEW_GRID != GRID:
    spawn()
    #score
    for i in range(4):
      #choose column
      for j in range(4):
        #find all zeros in each row
        if GRID_VERT[i][j] > 0:
          y = GRID_VERT[i][j]
          x += y
          imsotirednow = x
    print("Your score is " + str(imsotirednow))

def push_down():
  #label grid global so we can change it
  global GRID
  #rotating the grid
  GRID_VERT = list(map(list, zip(*GRID)))
  #create copy to represent new turn
  NEW_GRID = deepcopy(GRID)
  #move stuff right
  #choose row we are in
  for i in range(4):
    zero_count = 0
    #choose column
    for j in range(4):
      #find all zeros in each row
      if GRID_VERT[i][j] == 0:
        zero_count += 1
    #remove all the zeros in each row
    for _ in range(zero_count):
      GRID_VERT[i].remove(0)
    for _ in range(zero_count):
      GRID_VERT[i].insert(0,0)

  #try combine numbers
  for y in range(4):
    #index right 3 spots, right to left
    for x in range(3,0,-1):
      #if there is a duplicate square to the right
      if GRID_VERT[y][x] == GRID_VERT[y][x-1]:
        #promote block by 2
        GRID_VERT[y][x] *= 2
        #remove right block
        GRID_VERT[y].pop(x-1)
        GRID_VERT[y].insert(0,0)
  #apply changes back to grid
  GRID = list(map(list, zip(*GRID_VERT))) 

  #check that turn ended
  if NEW_GRID == GRID:
    current_zeros = 0
    for i in range(4):
      #choose column
      for j in range(4):
        #find all zeros in each row
        if GRID_VERT[i][j] == 0:
          current_zeros += 1
    if current_zeros == 0:
      for i in range(4):
      #choose column
        for j in range(4):
          #find all zeros in each row
          if GRID_VERT[i][j] > 0:
            y = GRID_VERT[i][j]
            x += y
      imsotirednow = x+1
      run = False
      pygame.quit()
      exit()
      print("Your score is " + str(imsotirednow))
    elif current_zeros > 0:
      spawn()
      #score
      for i in range(4):
        #choose column
        for j in range(4):
          #find all zeros in each row
          if GRID_VERT[i][j] > 0:
            y = GRID_VERT[i][j]
            x += y
            imsotirednow = x + 1
      print("Your score is " + str(imsotirednow))
  elif NEW_GRID != GRID:
    spawn()
    #score
    for i in range(4):
      #choose column
      for j in range(4):
        #find all zeros in each row
        if GRID_VERT[i][j] > 0:
          y = GRID_VERT[i][j]
          x += y
          imsotirednow = x + 1
    print("Your score is " + str(imsotirednow))


#gameloop
RUN = True

#Loading Screen
pygame.display.update()

#spawn starting numbers
spawn()
spawn()

while RUN:
  draw_screen()
  draw_grid()
  map_values()

  
  #event handler

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      pygame.quit()
      exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        push_right()
      if event.key == pygame.K_LEFT:
        push_left()
      if event.key == pygame.K_UP:
        push_up()
      if event.key == pygame.K_DOWN:
        push_down()
  #final update
  pygame.display.update()
#outside loop
pygame.display.quit()