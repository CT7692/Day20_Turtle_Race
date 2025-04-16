from turtle import Turtle, Screen
import secrets


def place_bet(color_list, screen_obj):
    user_bet = screen_obj.textinput(title="Your Bet", prompt="Which colored turtle will win the race?")
    if user_bet not in color_list:
        correct = False
        while not correct:
            user_bet = screen_obj.textinput(title="Your Bet",
                                            prompt="Sorry. That color is not in the list.\n"
                                                                     "Which colored turtle will win the race?")
            if user_bet in color_list:
                correct = True
    return user_bet


def turtle_list_setup(color_list):
    turtle_list = []
    for i in color_list:
        turtle_obj = Turtle(shape="turtle")
        turtle_obj.up()
        turtle_obj.color(i)
        turtle_list.append(turtle_obj)
    return turtle_list

def turtles_to_starting_line(x_pos, y_pos):
    for turtle in turtle_list:
        y_pos += 57
        turtle.setpos(x_pos, y_pos)


def race(turtle_list, finish_line, screen_obj, bet):
    winning_color = ""
    line_reached = False
    while not line_reached:
        for turtle in turtle_list:
            turtle.forward(secrets.SystemRandom().randint(0, 10))
            if turtle.xcor() > finish_line:
                winning_color = turtle.fillcolor()
                line_reached = True
    screen_obj.bye()
    outcome = f"The {winning_color} turtle wins! "
    if winning_color == bet:
        outcome += "Congratulations! You won the bet!"
    else:
        outcome += "You lose."
    return     outcome



color_list = ["purple", "blue", "green", "yellow", "orange", "red"]
my_screen = Screen()
user_bet = place_bet(color_list, my_screen)
my_screen.setup(width=500, height=400)
turtle_list = turtle_list_setup(color_list)
turtles_to_starting_line(x_pos=-230,y_pos=-180)
result = race(turtle_list,230, my_screen, user_bet)
print(result)
