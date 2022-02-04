import turtle

screen = turtle.Screen()
screen.setup(800,800)
screen.title("Min Max Tic Tac Toe")
screen.setworldcoordinates(-5,-5,5,5)
screen.bgcolor('black')
screen.tracer(0,0)
turtle.hideturtle()

def draw_board():
    turtle.pencolor('light gray')
    turtle.pensize(10)
    turtle.up()
    turtle.goto(-3,-1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-3,1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)

def draw_circle(x,y):
    turtle.up()
    turtle.goto(x,y-0.75)
    turtle.seth(0)
    turtle.color('light green')
    turtle.down()
    turtle.circle(0.75, steps=100)

def draw_x(x,y):
    turtle.color('cyan')
    turtle.up()
    turtle.goto(x-0.75,y-0.75)
    turtle.down()
    turtle.goto(x+0.75,y+0.75)
    turtle.up()
    turtle.goto(x-0.75,y+0.75)
    turtle.down()
    turtle.goto(x+0.75,y-0.75)
    
def draw_piece(i,j,p):
    if p==0: 
        return
    x,y = 2*(j-1), -2*(i-1)
    if p=='x':
        draw_x(x,y)
    else:
        draw_circle(x,y)
        
def draw(game):
    draw_board()
    for i in range(3):
        for j in range(3):
            draw_piece(i,j,game[i][j])
    screen.update()

def user_turn(i, j):
    game[i][j] = 'x'
    draw(game)


def computer_turn():
    global a, b
    bestscore = 10
    for i in range(0, 3):
        for j in range(0, 3):
            occupied = check(i, j)
            if not occupied:
                game[i][j] = 'o'
                score = minimax(game, True)
                game[i][j] = 0
                if score < bestscore:
                    a = i
                    b = j
                bestscore = min(score, bestscore)
    game[a][b] = 'o'
    draw(game)
    

def check(i, j):
    if game[i][j] == 'x' or game[i][j] == 'o':
        return True
    elif game[i][j] == 0:
        return False


def minimax(game, maximizingPlayer):
    board = board_is_full()
    w = declareWinner(game)
    if board:
        return w
    if not board and (w == 1 or w == -1):
        return w
    if maximizingPlayer:
        maxeval = -10
        for i in range(0, 3):
            for j in range(0, 3):
                occupied = check(i, j)
                if not occupied:
                    game[i][j] = 'x'
                    eval = minimax(game, False)
                    game[i][j] = 0
                    maxeval = max(eval, maxeval)
        return maxeval
    else:
        mineval = 10
        for m in range(0, 3):
            for n in range(0, 3):
                occupied = check(m, n)
                if not occupied:
                    game[m][n] = 'o'
                    eval = minimax(game, True)
                    game[m][n] = 0
                    mineval = min(eval, mineval)
        return mineval


def declareWinner(game):
    u = 0
    while u < 3:
        if game[u][0] == game[u][1] == game[u][2] == 'x':
            return 1
        elif game[u][0] == game[u][1] == game[u][2] == 'o':
            return -1
        if game[0][u] == game[1][u] == game[2][u] == 'x':
            return 1
        elif game[0][u] == game[1][u] == game[2][u] == 'o':
            return -1
        u += 1
    if game[0][0] == game[1][1] == game[2][2] == 'x':
        return 1
    elif game[0][0] == game[1][1] == game[2][2] == 'o':
        return -1
    if game[0][2] == game[1][1] == game[2][0] == 'x':
        return 1
    elif game[0][2] == game[1][1] == game[2][0] == 'o':
        return -1
    return 0


def board_is_full():
    for i in range(0, 3):
        for j in range(0, 3):
            occupied = check(i, j)
            if not occupied:
                return False
    return True



def play(x, y):
	i = 3-int(y+5)//2
	j = int(x+5)//2 - 1
	user_turn(i, j)
	if declareWinner(game) == 1:
		screen.textinput("Game over!","X won!")
		quit()
	computer_turn()
	if declareWinner(game) == -1:
		screen.textinput("Game over!","Computer won!")
		quit()
	if board_is_full():
		if declareWinner(game) == 0:
		    screen.textinput("Game over!", "Tie!")
		quit()

game = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]
draw(game)
screen.onclick(play)
turtle.mainloop()		  
