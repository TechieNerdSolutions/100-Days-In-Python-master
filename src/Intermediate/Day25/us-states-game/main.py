import turtle as t
import pandas

screen = t.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        #  AM  *([new_item for item in list]) ([new_item for item in list if test])
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        tim = t.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        tim.goto(*state_data.x, *state_data.y)  # Another Method tim.goto(int(state_data.x), int(state_data.y))
        tim.write(answer_state)  # AM tim.write(state_data.state.item())


#################################################
# # function for getting the coordinate        ##
# # def get_mouse_click_coor(x, y):            ##
# #     print(x, y)                            ##
# #                                            ##
# # t.onscreenclick(get_mouse_click_coor)      ##
# #                                            ##
# # t.mainloop()                               ##
#################################################
