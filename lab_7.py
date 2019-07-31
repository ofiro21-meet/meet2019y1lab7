
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=800
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 7
TIME_STEP = 120

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("turtle")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

def new_stamp():
    snake_pos = snake.pos()
    pos_list.append(snake_pos)
    snake_stamp = snake.stamp()
    stamp_list.append(snake_stamp)
    

for i in range (START_LENGTH):
    x_pos,y_pos=snake.pos()
    x_pos+=SQUARE_SIZE
    snake.goto (x_pos,y_pos)
    new_stamp()
                

def remove_tail():
    old_stamp=stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)


snake.direction = None
UP_EDGE = 400
DOWN_EDGE = -400
RIGHT_EDGE = 600
LEFT_EDGE = -600

def up():
    snake.direction="Up"
    

def down():
    snake.direction="Down"
    

def right():
    snake.direction="Right"
    

def left():
    snake.direction="Left"
    
    

turtle.onkeypress(up, "Up")
turtle.onkeypress(left, "Left")
turtle.onkeypress(down, "Down")
turtle.onkeypress(right, "Right")
turtle.listen()

turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for n in range(len(food_pos)):
    food.goto(food_pos[n])
    food_stamp = food.stamp()
    food_stamps.append (food_stamp)
    
    food.hideturtle()

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1

    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1

    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    food_stamps.append (food.stamp())
    

def move_snake():
    global START_LENGTH
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
    elif snake.direction=="Right":
        snake.goto(x_pos+ SQUARE_SIZE, y_pos )
    elif snake.direction=="Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)

    new_stamp()
    remove_tail()
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    


    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    elif new_x_pos <= LEFT_EDGE:
         print("You hit the left edge! Game over!")
         quit()
    elif new_y_pos >= UP_EDGE:
         print("You hit the up edge! Game over!")
         quit()
    elif new_y_pos <= DOWN_EDGE:
         print("You hit the down edge! Game over!")
         quit()

    if snake.pos() in pos_list[0:-2] and len(pos_list)>8:
        quit()

    
         
    elif snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        new_stamp()
        
    if len(food_stamps) <= 6 :
        make_food()
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()
      

   
    
turtle.mainloop()
