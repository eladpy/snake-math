import pygame
from logic.Fruit import Fruit
from logic.Snake import Snake
from Constants import *
from logic.math import *
from random import randint

# Text and fon
def display_on_screen(x_pos,y_pos, display_str, center):
    pos = (x_pos, y_pos)
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf',22)
    text = font.render(display_str, True, COLORS["GREEN"])
    textRect = text.get_rect()
    if center == "y":
        textRect.center = (x_pos, y_pos)
    return text,textRect

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()
    list = math()
    snake = Snake()
    fruits = []
    random = randint(list[3], list[4])
    ##create number of fruits
    for i in range(FRUIT_QUANTITY):
        fruits.append(Fruit())
    
    while True:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn(DIRECTIONS["UP"])
                elif event.key == pygame.K_DOWN:
                    snake.turn(DIRECTIONS["DOWN"])
                elif event.key == pygame.K_LEFT:
                    snake.turn(DIRECTIONS["LEFT"])
                elif event.key == pygame.K_RIGHT:
                    snake.turn(DIRECTIONS["RIGHT"])

        snake.move()
        # This is the case when the snake is eaten the fruite    
        if snake.get_head_position() == fruits[0].position:
            snake.length += 1
            list = math()
            for j  in range(len(fruits)):
                fruits[j].randomize_position()
        if snake.get_head_position() == fruits[1].position:
            pygame.QUIT()
        
    
        text,textRect = display_on_screen(350, 25 , to_string(list[0],list[1],list[-1]), "y")          
        screen.fill(COLORS["WHITE"])
        screen.blit(text,textRect)
        snake.draw(screen)
        for i in range(len(fruits)):
            fruits[i].draw(screen)
            if i == 0:
                t, tr = display_on_screen(fruits[i].position[0] - 1, fruits[i].position[1] - 20, str(list[2]), "y")
            else:
                t, tr = display_on_screen(fruits[i].position[0] - 1, fruits[i].position[1] - 20, str(random), "y")
            screen.blit(t, tr)  


        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()
    
