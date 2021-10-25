function Draw_Curve () {
    x = 0
    y = 0
    t = 0
    while (t < pi * 2) {
        x = Math.round(3 * Math.sin(a * t)) + 3
        y = 7 - (Math.round(3 * Math.sin(b * t - delta_fix - delta_var)) + 3)
        callimatrix.SetMatrixColorbright(0x0000ff, x, y, cbrightness.hp1)
        t = t + number_curve
    }
}
let t = 0
let y = 0
let x = 0
let number_curve = 0
let delta_var = 0
let delta_fix = 0
let b = 0
let a = 0
let pi = 0
let Single_Step = false
callimatrix.initNeoMatrix(DigitalPin.P1)
pi = 3.1415926
a = 1
b = 1
delta_fix = 0
delta_var = 0
let animation = true
let number_points = 26
let number_frames = 12
number_curve = pi * 2 / number_points
let number_animation = pi * 2 / Math.min(a, b) / number_frames
let delay = 500 / number_frames
basic.forever(function () {
    Draw_Curve()
    callimatrix.callimatrix_show()
    if (animation) {
        basic.pause(20)
        callimatrix.callimatrix_del()
        delta_var = delta_var + number_animation
    }
})
