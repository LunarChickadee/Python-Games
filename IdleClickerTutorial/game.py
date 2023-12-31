import pygame

pygame.init()

website = 'https://www.youtube.com/watch?v=qCA7FBwKOgI&ab_channel=LeMasterTech part 2'

#color library 
red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
purple = (127,0,255)
orange = (255,165,0)


screen = pygame.display.set_mode([300, 450])
pygame.display.set_caption('Not Adventure Capitalist')
background = black
framerate = 60
font = pygame.font.SysFont(None, 25)
#font = pygame.font.Font('freesansbold.tff', 16)
timer = pygame.time.Clock()
sysfont = pygame.font.get_default_font()




# game variables

green_value = 1
red_value = 2
orange_value = 3
white_value = 4
purple_value = 5

def draw_task(color,y_coord, value, draw, length, speed):
    pygame.draw.circle(screen, color,(30,y_coord),20,5)
    pygame.draw.rect(screen, color,[70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, black, [75, y_coord - 10, 190, 20])
    value_text = font.render(str(value), True, white)
    screen.blit(value_text, (16,y_coord - 10))



running = True
while running:

    timer.tick(framerate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background)
    draw_task(green, 50, green_value)
    draw_task(red, 110, red_value)
    draw_task(orange, 170, orange_value)
    draw_task(white, 230, white_value)
    draw_task(purple, 290, purple_value)

    pygame.display.flip()


pygame.quit()