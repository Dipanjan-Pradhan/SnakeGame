import pygame
import random
import os

# initialize the pygame functions
pygame.init()

pygame.mixer.init()

# set the size of the display. it is given as a f orm of tuple
display_length = 700
display_width = 400

gameWindow = pygame.display.set_mode((display_length, display_width))
   
# changing the qbackground image
bgimg = pygame.image.load("green background wallpaper.png").convert_alpha()
bgimg = pygame.transform.scale(bgimg, (display_length, display_width))

welcome_image = pygame.image.load("welcome.png")
welcome_image = pygame.transform.scale(welcome_image, (display_length, display_width)).convert_alpha()

gameover_image = pygame.image.load("game_over.png")
gameover_image = pygame.transform.scale(gameover_image, (display_length, display_width)).convert_alpha()

food_image = pygame.image.load("apple_image1.png")
food_image = pygame.transform.scale(food_image, (20, 20)).convert_alpha()


# define colors using r-g-b ratio
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
indigo = (122, 243, 245)    

display_color = white
food_color = red
score_color = green

# define the clock to move the point                                                                           
clock = pygame.time.Clock()                                                                           
fps = 200

# print score in the gaming display
def text_screen(text, color, x, y):
    font = pygame.font.SysFont(None, 55)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
    

def plot_snake(gameWindow, black,snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])
 

def welcome():
    pygame.mixer.music.load("welcome.mp3")
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        gameWindow.blit(welcome_image, (0, 0))       
        # text_screen("Welcome to Snake Game", black, 120, 130)
        # text_screen("Press SpaceBar to play", black, 120, 170)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()        
                    
        pygame.display.update()
        clock.tick(fps)                                                                                                
        

def game_loop(): 
    
    pygame.mixer.music.load("snake_play.mp3")
    pygame.mixer.music.play()
    
    # initialize the score
    score = 0
    
    # change the game title
    pygame.display.set_caption("My First Game")
    pygame.display.update()               # this update line is often used to modify the game

        
    # define the incriment of snake after taking the food
    snk_list = []
    snk_length = 1
    
    # define the position of the food        
    food_x = random.randint(50, display_length - 50)                                                                           
    food_y = random.randint(50, display_width - 50)
    
    # define the size and the position of the snake
    snake_x = random.randint(50, display_length)
    snake_y = random.randint(50, display_width)
    snake_size = 20

    # define the velocity of the point(head of snake)
    velocity_x = 0
    velocity_y = 0

    ## change the velocity
    init_velocity = 1
       
    exit_game = False  
    game_over = False                                         
    
    if(not os.path.exists("high_score.txt")):
        with open("high_score.txt", "w") as f:
            f.write("0")
    
    with open("high_score.txt", "r") as f:
        hiscore = f.read()
                                                                                      
    # the game always runs in an infinite while loop with some functions     
    while not exit_game: 
        if game_over:
            with open("high_score.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(display_color)
            gameWindow.blit(gameover_image, (0, 0))
            # text_screen("Game Over! Press Enter to continue", food_color, 20, 100)
            
            for event in pygame.event.get():                                                                                                          
                # this is the activation of the close button                                                                           
                if event.type == pygame.QUIT:                                                                           
                    exit_game = True 
                    exit()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()                                                                        
                                                                                                
        else:
            # this for loop is used to identify the pressed keys                                                                           
            for event in pygame.event.get():    
                                                                                                                       
                # this is the activation of the close button                                                                           
                if event.type == pygame.QUIT:                                                                           
                    exit_game = True         
                    exit()                                                                
                    
                # identify another keys
                elif event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_RIGHT:
                        if velocity_x == init_velocity:
                            velocity_x = init_velocity
                            velocity_y = 0
                            
                        elif velocity_x == -init_velocity:
                            velocity_x = -init_velocity
                            velocity_y = 0
                            
                        else:    
                            velocity_x = velocity_x + init_velocity
                            velocity_y = 0
                        
                    elif event.key == pygame.K_LEFT:
                        if velocity_x == -init_velocity:
                            velocity_x = -init_velocity
                            velocity_y = 0
                            
                        elif velocity_x == init_velocity:
                            velocity_x = init_velocity
                            velocity_y = 0
                            
                        else:
                            velocity_x = velocity_x - init_velocity
                            velocity_y = 0

                    elif event.key == pygame.K_UP:
                        
                        if velocity_y == -init_velocity:
                            velocity_y = -init_velocity
                            velocity_x = 0
                            
                        elif velocity_y == init_velocity:
                            velocity_y = init_velocity
                            velocity_x = 0
                        
                        else:
                            velocity_y = velocity_y - init_velocity
                            velocity_x = 0
                        
                        
                    elif event.key == pygame.K_DOWN:
                        
                        if velocity_y == init_velocity:
                            velocity_y = init_velocity
                            velocity_x = 0
                            
                        elif velocity_y == -init_velocity:
                            velocity_y = -init_velocity
                            velocity_x = 0
                            
                        else:
                            velocity_y = velocity_y + init_velocity
                            velocity_x = 0
                            
                    elif event.key == pygame.K_q:
                        score += 10

                        
            snake_x += velocity_x
            snake_y += velocity_y
            
            # the game will be over if the snake touch the display wall    
            if (snake_x >= display_length) or (snake_x <= 0) or (snake_y >= display_width) or (snake_y <= 0):
                pygame.mixer.music.load("big-boom-202678.mp3")
                pygame.mixer.music.play()
                game_over = True
            
            
            # use to replace the food to another position after taking it
            if abs(snake_x - food_x) < (snake_size - 5) and abs(snake_y - food_y) < (snake_size - 5):
                score += 10       # increment the score                         
                food_x = random.randint(0, display_length - 50)
                food_y = random.randint(0, display_width - 50)    
                snk_length += snake_size
                pygame.display.update()            
                                        
            # use to fill the display window with color (default : black)
            gameWindow.fill(display_color)
            gameWindow.blit(bgimg, (0, 0))
            # pygame.draw.rect(gameWindow, food_color, [food_x, food_y, snake_size, snake_size])
            gameWindow.blit(food_image, (food_x, food_y))
            
            
            # print the score on the gaming display
            
            text_screen("Score: " + str(score) + "  High Score: " + str(hiscore), score_color, 10, 10)
                
            if score > int(hiscore):
                hiscore = score
            
            # define the head of the snake
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
                
            # control the length of snake after moving
            if len(snk_list) > snk_length:
                del snk_list[0]
                
            # if the snake touch his own body the game will be over
            if head in snk_list[:-1]:
                pygame.mixer.music.load("big-boom-202678.mp3")
                pygame.mixer.music.play()
                game_over = True
            
            # use to draw a specific point on the display using the x and y co-ordinates and the size of that point
            # the positions and the length and width of the point must be given in a listed form 
            
            plot_snake(gameWindow, black,snk_list, snake_size)
    
            
        pygame.display.update()
        clock.tick(fps)
        
        
welcome()     

# use to quit the game
pygame.quit()
quit()
