import turtle

list_of_colors = ["blue", "red", "yellow",
                  "pink", "cadetblue", "pink", "darkorange", "darkseagreen", "firebrick", "pink", "goldenrod", "gray", "lawngreen", "lightcyan", "lightseagreen", "cadetblue", "pink", "darkorange", "darkseagreen", "firebrick", "pink", "goldenrod", "gray", "lawngreen"]


def change_color(al, ls):
    color = 0
    print("i am color the firs time:", color)
    if color <= len(ls):
        al.color(list_of_colors[color])
        if color >= 0:
            color += 1
    else:
        return


def create_square(al):
    for g in range(24):
        for e in range(4):
            al.forward(100)
            al.left(90)
        print("Doing g range one more time:", g)
        change_color(al, list_of_colors)
        al.left(15)


def main():
    turtle.Turtle()
    wn = turtle.Screen()
    al = turtle.Turtle()
    wn.bgcolor("green")
    al.pensize(2)
    al.speed(3)

    create_square(al)

    wn.exitonclick()


main()
