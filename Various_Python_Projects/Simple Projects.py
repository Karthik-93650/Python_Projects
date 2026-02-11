#Draw a heart
'''import turtle
pen = turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
heart()
turtle.done()'''

#Password Generator;
'''import secrets
import string

def create_pwd(pw_length=12):
    letters = string.ascii_letters
    digits= string.digits
    special_chars = string.punctuation

    alphabets = letters + digits + special_chars
    pw = ' '
    pw_strong = False

    while not pw_strong:
        pw = ' '
        for i in range(pw_length):
            pw += ' '.join(secrets.choice(alphabets))

        if (any(char in special_chars for char in pw) and sum(char in digits for char in pw) >= 2):
            pw_strong = True

    return pw

if __name__ == '__main__':
    print(create_pwd())'''

#Timer:
'''import winsound
import time

def beep_alarm():
    for repeats in range(7):
        winsound.Beep(3000, 500)
        winsound.Beep(6000, 300)

TimeDuration = int(input("Duration in seconds:"))

hours, minutes, seconds = 0,0,0
for i in range(TimeDuration):
    print('\n' * 100)

    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0

    print(str(hours) + ':' +str(minutes) + ':' +str(seconds))
    time.sleep(1)

if __name__ ==  '__main__':
    beep_alarm()'''











