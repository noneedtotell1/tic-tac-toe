print("first call is always O")
board = [[-1,-1,-1] , [-1,-1,-1] , [-1,-1,-1]]
rep = {-1:' ', 0:'O', 1:'X'}


def printboard():
	print('-------------')
	for i in board:
		for j in i:
			print('| ' + rep[j] , end=" ")
		print("|\n-------------")



def isfull():
	for i in board:
		for j in i:
			if j == -1:
				return False
	return True

def inputer(k):
	while True:
		print("enter the position for player" + str(k) + " : ")
		x = int(input())
		y = int(input())
		a = x - 1
		b = y - 1
		if (a < 3) and (a > -1) and (b < 3) and (b > -1):
			if board[a][b] == -1:
				board[a][b] = k - 1
				return
		else:
			print('Know your limits idiot')

def play(user):
	if(user%2==0):
		inputer(1)
		printboard()
		if(check() == 1):
			print("player1 wins!!")
		elif(isfull()):
			print("tie!!")
		else:
			play(1)
	else:
		inputer(2)
		printboard()
		if(check() == 1):
			print("player2 wins!!")
		elif(isfull()):
			print("tie!!")
		else:
			play(0)



def check():
	if(board[0][0]==0 and board[1][1]==0 and board[2][2]==0):
		return 1
	elif(board[0][0]==1 and board[1][1]==1 and board[2][2]==1):
		return 1
	elif(board[0][0]==0 and board[0][1]==0 and board[0][2]==0):
		return 1
	elif(board[0][0]==1 and board[0][1]==1 and board[0][2]==1):
		return 1
	elif(board[1][0]==0 and board[1][1]==0 and board[1][2]==0):
		return 1
	elif(board[1][0]==1 and board[1][1]==1 and board[1][2]==1):
		return 1
	elif(board[2][0]==0 and board[2][1]==0 and board[2][2]==0):
		return 1
	elif(board[2][0]==0 and board[2][1]==0 and board[2][2]==0):
		return 1
	elif(board[2][0]==0 and board[1][1]==0 and board[0][2]==0):
		return 1
	elif(board[2][0]==0 and board[1][1]==0 and board[0][2]==0):
		return 1
	else:
		return 0


printboard()
play(0)
