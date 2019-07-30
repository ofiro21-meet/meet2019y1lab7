
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 7
TIME_STEP = 100

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
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

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



def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    elif x_pos <= LEFT_EDGE:
         print("You hit the left edge! Game over!")
         quit()
    elif y_pos >= UP_EDGE:
         print("You hit the up edge! Game over!")
         quit()
    elif y_pos <= DOWN_EDGE:
         print("You hit the down edge! Game over!")
         quit()
    turtle.ontimer(move_snake,TIME_STEP)


    
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

move_snake()

    
turtle.mainloop()
