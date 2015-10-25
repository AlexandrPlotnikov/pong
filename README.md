ballXSpeed = -2
ballYSpeed = 2

py1 = 300
py2 = 300
def setup():
     size(900,600)
     global ballX,ballY,py1,py2
     ballX = width/2
     ballY = height/2
def draw():
    global ballX,ballY,ballXSpeed,ballYSpeed,py1,py2
    ballX += ballXSpeed
    ballY += ballYSpeed
    if ballX <= -100 or (ballX <= 30 and ballY <= py1 + 100 and ballY >= py1):
        ballXSpeed = -ballXSpeed
    if ballX >= width + 100 or (ballX >= width - 30 and ballY <= py2 + 100 and ballY >= py2):
        ballXSpeed = -ballXSpeed
    if ballY >= height - 20 :
         ballYSpeed = - ballYSpeed
    if ballY <= 20:
        ballYSpeed = -ballYSpeed    
    if keyPressed:
        if key == "w" and py1 >= 15:
            py1 -= 5
        if key == "s" and py1 >= 15:
            py1 += 5
    if keyPressed:
        if key == "o" and py2>= 15:
            py2 -= 5
        if key == "l" and py2>= 15:
            py2 += 5
#    if ballX == 10 and ballY >= py1 + 100:
 #       ballXSpeed = -ballXSpeed
    fill(1267216742)
    rect(10,10,880,580)#place
    line(450,10,450,590)#net
    fill(1)
    rect(10,py1,10,100)#player1
    fill(1)
    rect(880,py2,10,100)#player2
    fill(1)
    triangle(450,20,440,10,460,10)#NetHolderTop
    fill(1)
    triangle(450,580,440,590,460,590)#NetHolderDown
    fill(92376732865423)
    ellipse(ballX,ballY,20,20)#ball
