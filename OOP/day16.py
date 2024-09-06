# from turtle import Turtle, Screen

# timmy = Turtle()

# print(timmy)

# timmy.shape("turtle")
# timmy.color("HotPink")
# timmy.forward(100)

# myscreen = Screen()

# print(myscreen.canvheight)

# myscreen.exitonclick()  

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type",]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)
table.align = "l"

print(table)
