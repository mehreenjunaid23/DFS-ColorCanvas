
import pygame
import random
import time
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
#glood filling algorithm
def flood_fill(screen, surface, position, fill_color, delay):
    surf_array = pygame.surfarray.pixels2d(surface)  # Create an array from the surface.
    fill_color = surface.map_rgb(fill_color)  # Convert the color to mapped integer value.
    current_color = surf_array[position]  # Get the mapped integer color value.
    frontier = [position]
    while len(frontier) > 0:
        x, y = frontier.pop()
        try:  # Add a try-except block in case the position is outside the surface.
            if surf_array[x, y] != current_color:
                continue
        except IndexError:
            continue
        surf_array[x, y] = fill_color #update color of pixel
        screen.set_at((x, y), fill_color)
        # #simulation
        pygame.display.update()
        time.sleep(delay)  # Add a delay between each pixel update.
        # Then we append the neighbours of the pixel in the current position to our 'frontier' list.
        frontier.append((x + 1, y))  # Right.
        frontier.append((x - 1, y))  # Left.
        frontier.append((x, y + 1))  # Down.
        frontier.append((x, y - 1))  # Up.

    pygame.surfarray.blit_array(surface, surf_array)

#draw and color
def draw():
    Tk().wm_withdraw() #to hide the main window
    messagebox.showinfo('Alert','When done drawing quit to color')

    pygame.init()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #initialising window parameters
    screen = pygame.display.set_mode((700, 500), 0, 32)
    screen.fill(WHITE)
    pygame.display.set_caption('Coloring Algorithm')
    clock = pygame.time.Clock()

    # closing the window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_buttons = pygame.mouse.get_pressed()

        #drawing
        if event.type == pygame.MOUSEMOTION:
            if mouse_buttons[0]:  # Left mouse button down.
                last = (event.pos[0]-event.rel[0], event.pos[1]-event.rel[1])
                pygame.draw.line(screen, BLACK, last, event.pos, 5)

        pygame.display.update()
        clock.tick(30)  # Limit the frame rate to 30 FPS.
    pygame.image.save(screen, "image.png")

def main():
    Tk().wm_withdraw()  # to hide the main window
    answer = messagebox.askquestion('Choose Option', 'What would you like to do?\n\n'
                                                      '1. Draw (Yes)\n'
                                                      '2. Color (No) \n', icon = "question")
    if answer == "yes": #drawing
        draw()
        pygame.init()
        #initilise window
        screen = pygame.display.set_mode((1024, 640))
        clock = pygame.time.Clock()
        image = pygame.image.load('image.png').convert() #convert window to array
        while True:
            clock.tick(30)
             # closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    #coloring
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        fill_color = random.choice(tuple(pygame.color.THECOLORS.values())) #random color generation
                        flood_fill(screen, image, event.pos, fill_color, 0.001) #color
            
            screen.blit(image, (0, 0))
            pygame.display.update()
    elif answer == "no":
        #load image from computer
        Tk().wm_withdraw() #to hide the main window
        file_path = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png"), ("JPG Images", "*.jpg"), ("JPEG Images", "*.jpeg;*.jpg")])
        pygame.init()
        #initilise window
        screen = pygame.display.set_mode((1024, 640))
        clock = pygame.time.Clock()
        image = pygame.image.load(file_path).convert()
        while True:
            clock.tick(30)
            # closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        fill_color = random.choice(tuple(pygame.color.THECOLORS.values())) #random color generation
                        flood_fill(screen, image, event.pos, fill_color, 0.000000001) #color

            screen.blit(image, (0, 0))
            pygame.display.update()

        
if __name__ == "__main__":
    main()
