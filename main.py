def on_button_pressed_a():
    global win
    basic.clear_screen()
    win = False
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global win
    if position == 3:
        win = True
        basic.pause(100)
        basic.show_string("W")
input.on_button_pressed(Button.B, on_button_pressed_b)

win = False
position = 0
position = 2
changeBy = 1
win = False

def on_forever():
    global position, changeBy
    if win == False:
        basic.pause(100)
        led.unplot(position, 2)
        position += changeBy
        if position == 4:
            changeBy = -1
        if position == 0:
            changeBy = 1
        led.plot(position, 2)
basic.forever(on_forever)
