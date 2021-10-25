def zeichne_kurve():
    global x, y, t
    x = 0
    y = 0
    t = 0
    while t < pi * 2:
        x = Math.round(3 * Math.sin(a * t)) + 3
        y = 7 - (Math.round(3 * Math.sin(b * t - delta_fix - delta_var)) + 3)
        callimatrix.set_matrix_colorbright(0x0000ff, x, y, cbrightness.HP1)
        t = t + number_curve
t = 0
y = 0
x = 0
number_curve = 0
delta_var = 0
delta_fix = 0
b = 0
a = 0
pi = 0
Single_Step = False
callimatrix.init_neo_matrix(DigitalPin.P1)
pi = 3.1415926
a = 1
b = 1
delta_fix = 0
delta_var = 0
animation = True
number_points = 26
number_frames = 12
number_curve = pi * 2 / number_points
number_animation = pi * 2 / min(a, b) / number_frames
verzoegerung = 500 / number_frames

def on_forever():
    global delta_var
    zeichne_kurve()
    callimatrix.callimatrix_show()
    if animation:
        basic.pause(20)
        callimatrix.callimatrix_del()
        delta_var = delta_var + number_animation
basic.forever(on_forever)
