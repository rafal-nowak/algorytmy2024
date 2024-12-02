import pygame, random # type: ignore
from settings import *
from graph import draw_graph

# algorithms functions you can choose from
from bubble_sort import bubbleSort
from insertion_sort import insertionSort
from merge_sort import mergeSort
from quick_sort import quickSort


# pygame setup
# do not touch
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
animating = True
dt = 0
current_frame = 1

# to adjust the speed of the animation just change this value
# greater speed = lower delay
animation_delay = 1


# datasets - just comment all you don't want to use and choose the size of an array
arr_size = 100

# random
arr = list(range(arr_size))
random.shuffle(arr)

# ascending
# arr = list(range(arr_size))

# descending
# arr = (list(range(arr_size)))
# arr.reverse()

# this is used to visualise array accesses
# do not touch
highlites = [0] * arr_size

# algorithm config
# to change algorithm just use another imported function
sorting_process = quickSort(arr, highlites, 0, len(arr)-1) 

# algorithm performance data
# do not touch
array_accesses = 0
comparisons = 0

# display data
# do not touch
width = screen.get_width()
height = screen.get_height()
bar_w = width // len(arr)
bar_unit_h = height * 0.9 // max(arr)


# main loop
while running:

    # events and keys input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    # reset previous frame
    screen.fill(BG_COLOUR)

    # animation core
    if animating and current_frame % animation_delay == 0:
        next_step = next(sorting_process, None)
        if next_step is None:
            animating = False
        else:
            array_accesses += next_step[0]
            comparisons += next_step[1]
        current_frame = 1
    if animating:
        current_frame += 1
        

    # display update
    draw_graph(screen, arr, highlites, width, height, bar_w, bar_unit_h)

    pygame.display.flip()

    # FPS regulation
    dt = clock.tick(200) / 1000

print('Array accesses: ', array_accesses)
print('Performed comparisons: ', comparisons)

pygame.quit()