import turtle as t
import math

t.tracer(False)
#   t.update() put this somewhere idk where but itll make it instant gotta fix later

def bowling_game():
    t.speed(1000)

    screen = t.Screen()
    arrow = t.Turtle()
    playerball = t.Turtle()
    score = 0
    t.hideturtle()
    playerball.hideturtle()

    old_angle = 5
    ball_in_motion = False  # Flag to track if the ball is in motion

    class Pin(t.Turtle):
        def __init__(self, x, y):
            super().__init__()
            self.penup()
            self.goto(x, y)
            self.pendown()
            self.shape("circle")
            self.color("black")
            self.speed(1000)
            self.radius = 70

    def player_ball():
        playerball.pendown()
        playerball.begin_fill()
        playerball.pencolor("black")
        playerball.circle(20)
        playerball.end_fill()

    def move_left():
        angle = arrow.heading()
        arrow.setheading(angle + old_angle)

    def move_right():
        angle = arrow.heading()
        arrow.setheading(angle - old_angle)

    def launch_ball():
        nonlocal ball_in_motion
        angle = arrow.heading()
        speed = 30
        playerball.setheading(angle)

        def move_ball(frames=50):
            nonlocal ball_in_motion

            playerball.hideturtle()
            playerball.clear()
            playerball.penup()
            playerball.forward(speed)
            playerball.pendown()
            player_ball()
            check_collision()
            check_boundary()
            screen.update()

            frames -= 1
            if frames > 0 and ball_in_motion:
                t.ontimer(move_ball, 50)
            else:
                reset_ball()

        ball_in_motion = True
        move_ball()

    def check_collision():
        for pin in pins:
            if is_collision(playerball, pin):
                remove_pin(pin)

    def check_boundary():
        if (
            playerball.xcor() < -screen.window_width() / 2
            or playerball.xcor() > screen.window_width() / 2
            or playerball.ycor() < -screen.window_height() / 2
            or playerball.ycor() > screen.window_height() / 2
        ):
            reset_ball()

    def reset_ball():
        nonlocal ball_in_motion
        ball_in_motion = False

        playerball.penup()
        playerball.goto(20, -100)
        playerball.pendown()
        playerball.clear()
        screen.clear()
        t.write(
            f"You scored {score} points!!",
            font=("Arial", 90, "normal"),
            align=("center"),
        )

    def is_collision(t1, t2):
        distance = math.sqrt(
            (t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2
        )
        return distance < t2.radius + 20

    def remove_pin(pin):
        pin.hideturtle()
        pins.remove(pin)
        nonlocal score
        score += 1

    playerball.speed(1000)

    screen.listen()
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    screen.onkey(launch_ball, "space")

    pins = [
        Pin(-60, 300),
        Pin(-10, 300),
        Pin(40, 300),
        Pin(90, 300),
        Pin(70, 250),
        Pin(20, 250),
        Pin(-30, 250),
        Pin(-5, 200),
        Pin(45, 200),
        Pin(20, 150),
    ]

    playerball.penup()
    playerball.goto(20, -100)
    playerball.pendown()
    player_ball()

    arrow.penup()
    arrow.goto(20, -20)
    arrow.left(90)

    t.mainloop()


bowling_game()
