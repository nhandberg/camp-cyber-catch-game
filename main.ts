input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    win = false
})
input.onButtonPressed(Button.B, function () {
    if (position == 2) {
        win = true
        basic.pause(100)
        basic.showString("W")
    }
})
let win = false
let position = 0
position = 0
let changeBy = 1
win = false
basic.forever(function () {
    if (win == false) {
        basic.pause(100)
        led.unplot(position, 2)
        position += changeBy
        led.plot(position, 2)
        if (position == 4) {
            changeBy = -1
        }
        if (position == 0) {
            changeBy = 1
        }
    }
})
