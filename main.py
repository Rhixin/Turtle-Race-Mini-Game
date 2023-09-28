from turtle import Turtle,Screen,addshape
import random
import art


colors = ["red", "orange","yellow","green","blue","indigo","violet"]

for i in colors:
    addshape(shape=None,name=f"{i}.gif")



def random_speed(turt):
    speed = [2, 2.25, 2.5, 2.75, 3, 3.25, 3.50, 3.75, 4]
    choice = random.choice(speed)
    
    turt.forward(choice)
    
def check_winner(turt):
    if turt.xcor() >= 179:
        return True
    
    return False     
        
Screen().setup(width=500,height=400)
Screen().bgpic("finish_bg.png")



racers = []
y = 150
for i in colors:
    tim = Turtle(shape=f"{i}.gif")
    tim.penup()
    tim.color(i)
    tim.goto(x=-220,y=y)
    y-=50
    racers.append(tim)

print("User's guess: ")
user_bet = Screen().textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the color: ")
print(user_bet)

end_race = False

while not end_race:
    turn = random.choice(racers)
    random_speed(turn)
    end_race = check_winner(turn)
    

print(f"The winner is the {turn.pencolor()} turtle!")
if turn.pencolor() == user_bet:
    print(art.win)
else:
    print(art.lose)
    


Screen().exitonclick()
