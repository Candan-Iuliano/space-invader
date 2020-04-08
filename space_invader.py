
import turtle
import os
import math
import random
import time
import threading
from multiprocessing import Process
import sys
from threading import Timer


#Set up the Screen

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

#Register the Shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
turtle.register_shape("explosion.gif")
#Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set score to 0
score = 0

#draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


#Create Plater Turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Choose the number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies =[]

#Add enemies to list
for i in range(number_of_enemies):
    #Create the Enemy
    enemies.append(turtle.Turtle())

#Create the Enemy
for enemy in enemies:
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200) + 10
    y = random.randint(100, 250) + 40
    enemy.setposition(x, y)


enemyspeed = 2





#Creat Player Bullet
bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.1,1)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
# ready- ready to fire
# fire - bullet is firing
bulletstate = "ready"

#Move the player left and right

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


#Bullet States
def fire_bullet():
    #declare bulletsate as a global if it needs change
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"

    #move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor()- t2.ycor(),2))
    if distance < 50:
        return True
    else:
        return False




#def enemydeath():
    #enemy.shape("explosion.gif")

#t = Timer(1.0, enemydeath)



#Create Keyboard bidnings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")



#Main Game Loop

while True:

#    t.start()
    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor() > 280:
            #Move all enemies down
            for enemy in enemies:
                y = enemy.ycor()
                y -= 40
                enemy.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            # Move all enemies down
            for enemy in enemies:
                y = enemy.ycor()
                y -= 40
                enemy.sety(y)
            # Change enemy direction
            enemyspeed *= -1

         # Check for bullet collision with enemy
        if isCollision(bullet, enemy):
            # Reset Bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)


            #threading.Thread(target=enemydeath).start()


            # Reset the Enemy
            enemy.shape("invader.gif")
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)



            #Update Score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))



        if isCollision(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #Move the Bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if the bullet has hit top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"






delay = wn.mainloop()
