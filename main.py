def zeichne_kurve():
    global x, y, t
    x = 0
    y = 0
    t = 0
    while t < pi * 2:
        x = Math.round(3 * Math.sin(a * t)) + 3
        y = 7 - (Math.round(3 * Math.sin(b * t - delta_fix - delta_var)) + 3)
        callimatrix.set_matrix_colorbright(0x0000ff, x, y, cbrightness.HP1)
        t = t + schritt_kurve
t = 0
y = 0
x = 0
schritt_kurve = 0
delta_var = 0
delta_fix = 0
b = 0
a = 0
pi = 0
callimatrix.init_neo_matrix(DigitalPin.P1)
einzelschritt = False
pi = 3.1415926
a = 1
b = 1
delta_fix = 0
delta_var = 0
animation = True
anzahl_punkte = 26
anzahl_frames = 12
schritt_kurve = pi * 2 / anzahl_punkte
schritt_animation = pi * 2 / min(a, b) / anzahl_frames
verzoegerung = 500 / anzahl_frames

def on_forever():
    global delta_var
    zeichne_kurve()
    callimatrix.callimatrix_show()
    if animation:
        basic.pause(20)
        callimatrix.callimatrix_del()
        delta_var = delta_var + schritt_animation
basic.forever(on_forever)
