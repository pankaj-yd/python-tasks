import pygame as pyg

boxes = [None]*9

pyg.init()

W = 540
H = 540
black = (0, 0, 0)

screen = pyg.display.set_mode((W, H))
screen2 = pyg.display.set_mode((W, H))

X = pyg.image.load("./x.png")
O = pyg.image.load("./o.png")
X = pyg.transform.scale(X, (180, 180))
O = pyg.transform.scale(O, (180, 180))

def isWinner(boxes, player):
    return (boxes[0] == player and boxes[1] == player and boxes[2] == player) or (boxes[3] == player and boxes[4] == player and boxes[5] == player) or (boxes[6] == player and boxes[7] == player and boxes[8] == player) or (boxes[0] == player and boxes[3] == player and boxes[6] == player) or (boxes[1] == player and boxes[4] == player and boxes[7] == player) or (boxes[2] == player and boxes[5] == player and boxes[8] == player) or (boxes[0] == player and boxes[4] == player and boxes[8] == player) or (boxes[2] == player and boxes[4] == player and boxes[6] == player)

player = 'x'

screen.fill((255, 255, 255))

while True:
    if isWinner(boxes, 'x'):
	    print('X won')
	    break
    elif isWinner(boxes, 'o'):
	    print('O won')
	    break
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            quit()

        if event.type == pyg.MOUSEBUTTONDOWN:
            if pyg.mouse.get_pressed()[0]:
                x, y = pyg.mouse.get_pos()
                x //= 180
                y //= 180

                mx = x*180
                my = y*180
                if player == 'x' and boxes[x+3*y] == None:
                    screen.blit(X, (mx, my))
                    boxes[x+3*y] = 'x'
                    player = 'o'
                elif player == 'o' and boxes[x+3*y] == None:
                    screen.blit(O, (mx, my))
                    boxes[x+3*y] = 'o'
                    player = 'x'


    pyg.draw.line(screen, black, (W/3, 0), (W/3, H), 3)
    pyg.draw.line(screen, black, (2*W/3, 0), (2*W/3, H), 3)
    pyg.draw.line(screen, black, (0, H/3), (W, H/3), 3)
    pyg.draw.line(screen, black, (0, 2*H/3), (W, 2*H/3), 3)

    pyg.display.update()
