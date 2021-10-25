a  =  1   # frequency horizontal
b  =  2   # vertical frequency (interesting pairs a / b are e.g .: 1/1, 1/2, 1/3, 2/3)
delta_fix  =  0   # fixed phase shift (in radians, e.g .: Math.PI / 2)
delta_var  =  0   # auxiliary variable for variable phase shift (animation)
animation  =  True    # variable phase shift on / off
single_step  =  False   # 100 ms pause after each calculated point
number_points  =  26   # Number of calculated points per curve
number_frames  =  8   # Number of calculated curves in the animation
step_curve  =  Math . PI  *  2  /  number_points   # Sin has a period of 2 * Pi
step_animation  =  Math . PI  *  2  /  min ( a ,  b )  /  number_frames   # Cycle repeats itself at 2 * Pi / min (a, b)
delay  =  4000  /  number_frames   # approx. 4 seconds total animation duration (without single step)

def  draw_curve ():
    x  =  0   # screen x-coord. point to be drawn
    y  =  0   # screen y-coord. point to be drawn
    t  =  0   # time
    while  t  <  Math . PI  *  2 :   # for the complete curve:
        x  =  math.round ( 2  *  Math . sin ( a  *  t ))  +  2   # x-coord. to calculate
        y  =  4  -  ( Math . round ( 2  *  Math . sin ( b  *  t  -  delta_fix  -  delta_var ))  +  2 )   # Calculate y-coordinate
        led . plot ( x ,  y )   # draw pixel
        if  single_step :   # in single step mode :
            basic . pause ( 100 )   # 100 ms pause after each calculated point
        t  +=  step_curve   # look at the next point on the curve

def  on_forever ():
    global  delta_var   # we access the variable phase shift in writing
    draw_curve ()   # draw curve with current parameters
    if  animation :   # with animation switched on:
        basic . pause ( delay )   # wait after each frame
        basic.clear_screen()   # clear screen
        delta_var  +=  step_animation   # next animation step

basic . forever ( on_forever )