ballX = 0
ballY = 0

ballXSpeed = -2
ballYSpeed = 2
def setup():
    size(900,600)
    global ballX,ballY
    ballX = width/2
    ballY = height/2
def draw():
    global ballX,ballY,ballXSpeed,ballYSpeed
    ballX += ballXSpeed
    ballY += ballYSpeed
    if ballX <=0 :
        ballXSpeed = -ballXSpeed
    if ballX >= width :
        ballXSpeed = -ballXSpeed
    if ballY <=0 :
        ballYSpeed = -ballYSpeed
    if ballY >= height - 10 :
        ballYSpeed = - ballYSpeed
    rect(10,10,880,580)#place
    line(450,10,450,590)#net
    rect(10,100,10,100)#player1
    rect(880,350,10,100)#player2
    triangle(450,20,440,10,460,10)#NetHolderTop
    triangle(450,580,440,590,460,590)#NetHolderDown
    ellipse(ballX,ballY,20,20)#ball
