#create the chessboard
chessboard = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
			  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
			  [' ', '.', ' ', '.', ' ', '.', ' ', '.'],
			  ['.', ' ', '.', ' ', '.', ' ', '.', ' '],
              [' ', '.', ' ', '.', ' ', '.', ' ', '.'],
              ['.', ' ', '.', ' ', '.', ' ', '.', ' '],
              ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
              ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
              
#print the board
def print_board(board):
	for row in board:
		print(' '.join(str(piece) for piece in row))
		
#code for movements
def move_piece(board, start_row, start_col, end_row, end_col):
	piece = board[start_row][start_col]
	board[start_row][start_col] = ' '
	board[end_row][end_col] = piece
	
# the main game
while True:
	#print the board
	print_board(chessboard)
	
	#ask the player to enter a move
	start_pos = input('Enter the starting position of the piece (e.g. "e2"): ')
	end_pos = input('Enter the ending position of the piece (e.g. "e4"): ')
	
	#convert input into rows and column numbers
	start_col = ord(start_pos[0]) - ord('a')
	start_row = int(start_pos[1]) - 1
	end_col = ord(end_pos[0]) - ord('a')
	end_row = int(end_pos[1]) - 1
	
	#move the piece on the board
	move_piece(chessboard, start_row, start_col, end_row, end_col)
