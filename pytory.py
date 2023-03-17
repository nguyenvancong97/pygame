import tkinter
import pygame
cx=0
cy=200

px = 400
py = 500

x_houkou1 = 1
y_houkou1 = 1

tensu = 0
speed = 10

ojyamaon = 0

ox = 400
oy = 300
ox_houkou1 = 1
oy_houkou1 = 1

def teki1move():
    global cx, cy, x_houkou1, y_houkou1, tensu, speed
    if cx - (img1.width()/2) <=0:
        x_houkou1 = 1
    elif cx + (img1.width()/2) >= 800:
        x_houkou1 = -1

    if cy - (img1.height()/2) <= 0:
        y_houkou1 = 1
    elif cy + (img1.height()/2) >= 600:
        music.stop()
        return

    if atari(img1, img2):
        if y_houkou1 == 1:
            y_houkou1 = -1
            tensu = tensu + 1
            label1.configure(text = tensu)
            sound1.play()

    if tensu >= 5:
        speed = 8

    cx = cx + 5 * x_houkou1
    cy = cy + 5 * y_houkou1
    canvas.coords("chick", cx, cy)
    root.after(speed, teki1move)
def ojyamove():
    global tensu, ojyamaon, ox, oy, ox_houkou1, oy_houkou1
    if tensu >= 3:
        if ojyamaon == 0:
            canvas.create_image(400, 300, image=img3, tag="chicken")
            ojyamaon = 1
        if ojyamaon == 1:
            if ox - (img3.width()/2) <= 0:
                ox_houkou1 = 1
            elif ox + (img3.width()/2) >= 800:
                ox_houkou1 = -1

            if oy - (img3.height()/2) <= 0:
                oy_houkou1 = 1
            elif oy + (img3.height()/2) >= 600:
                music.stop()
                return
            ox = ox + 5 * ox_houkou1
            oy = oy + 5 * oy_houkou1
            if atari1(img2, img3):
                if oy_houkou1 == 1:
                    oy_houkou1 = -1
                    tensu = tensu + 1
                    label1.configure(text = tensu)
                    sound1.play()

    canvas.coords("chicken",ox ,oy)
    root.after(20,ojyamove)

def pad1move(event):
    global px, py
    px = event.x
    canvas.coords("PAD1", px, py)

def atari(imgA, imgB):
    cxl = cx - imgA.width()/2
    cxr = cx + imgA.width()/2
    cyt = cy - imgA.height()/2
    cyb = cy + imgA.height()/2

    pxl = px - imgB.width()/2
    pxr = px + imgB.width()/2
    pyt = py - imgB.height()/2
    pyb = py + imgB.height()/2

    if cxr > pxl:
        if cxl < pxr:
            if cyb > pyt:
                if cyt < pyb:
                    return True
    return False
def atari1(imgA, imgB):
    oxl = ox - imgA.width()/2
    oxr = ox + imgA.width()/2
    oyt = oy - imgA.height()/2
    oyb = oy + imgA.height()/2

    pxl = px - imgB.width()/2
    pxr = px + imgB.width()/2
    pyt = py - imgB.height()/2
    pyb = py + imgB.height()/2

    if oxr > pxl:
        if oxl < pxr:
            if oyb > pyt:
                if oyt < pyb:
                    return True
    return False

root = tkinter.Tk()
canvas = tkinter.Canvas(width=800,height=600)
canvas.pack()
img0 = tkinter.PhotoImage(file = "BG560a_800.png")
img1 = tkinter.PhotoImage(file = "chick.png")
img2 = tkinter.PhotoImage(file = "paddle.png")
img3 = tkinter.PhotoImage(file = "chicken.png")

canvas.create_image(400,300, image= img0, tag="BAK")
canvas.create_image(cx,cy, image=img1, tag="chick")
canvas.create_image(px,py, image=img2, tag="PAD1")

label1 = tkinter.Label(root, text = tensu, font =("Times","20"))
label2 = tkinter.Label(root, text = "419518" + "NGUYEN VAN CONG",font =("Times","20"))
label1.place(x=700, y = 0)
label2.place(x=0, y = 0)
pygame.init()
sound1 = pygame.mixer.Sound("point29.ogg")

music = pygame.mixer.music
music.load("fantasy.ogg")
music.set_volume(0.3)
music.play(-1)

teki1move()
ojyamove()
canvas.bind('<Motion>', pad1move)
root.mainloop()

