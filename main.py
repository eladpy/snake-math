import pygame
from logic.Fruit import Fruit
from logic.Snake import Snake
from Constants import *
from logic.math import *

# Text and fon
def display_on_screen(x_pos,y_pos, display_str):
    pos = (x_pos, y_pos)
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf',22)
    text = font.render(display_str, True, COLORS["GREEN"])
    textRect = text.get_rect()
    textRect.center = (x_pos // 2 +250, y_pos// 2-40 )
    return text,textRect

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()
    list = math()
    snake = Snake()
    fruits = []

    ##create number of fruits
    for i in range(FRUIT_QUANTITY):
        fruits.append(Fruit())
    fruits[0]
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
        for i in range(len(fruits)):    
            if snake.get_head_position() == fruits[i].position:
                snake.length += 1
                list = math()
                for j  in range(len(fruits)):
                    fruits[j].randomize_position()
        
    
        text,textRect = display_on_screen(200,200, to_string(list[0],list[1],list[-1]))          
        screen.fill(COLORS["WHITE"])
        screen.blit(text,textRect)
        snake.draw(screen)
        for i in range(len(fruits)):
            fruits[i].draw(screen)
        

        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()
