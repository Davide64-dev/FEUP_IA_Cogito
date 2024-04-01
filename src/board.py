
# Class that represents Cogito's board
class Board:

    # Constructor - Constructs a new board, receiving the size of it
    def __init__(self, board_size):
        self.board = [[False for _ in range(board_size)] for _ in range(board_size)]
        self.objective = [[False for _ in range(board_size)] for _ in range(board_size)]

        for i in range(3, 6):
             for j in range(3, 6):
                self.board[i][j] = True
                self.objective[i][j] = True

    def getBoardSize(self):
        return len(self.board)

    # Shifs a specific row to the right
    def rotateRowRight(self, row):
        self.board[row] = self.board[row][-1:] + self.board[row][:-1]

    # Shifts a specific row to the left
    def rotateRowLeft(self, row):
        self.board[row] = self.board[row][1:] + self.board[row][:1]

    # Rotate down a column
    def rotateColumnDown(self, col):
        previous = self.board[0][col]
        self.board[0][col] = self.board[-1][col]
        for i in range(1, self.getBoardSize()):
            new_previous = self.board[i][col]
            self.board[i][col] = previous 
            previous = new_previous

    # ROtate up a column
    def rotateColumnUp(self, col):
        previous = self.board[-1][col]
        for i in range(self.getBoardSize() - 2, -1, -1):
            new_previous = self.board[i][col]
            self.board[i][col] = previous 
            previous = new_previous
        self.board[-1][col] = previous

    # Check if a Board object is a winning board according to Cogito's rules
    def isWinningBoard(self):
        for row in range(self.getBoardSize()):
            for col in range(self.getBoardSize()):
                if self.board[row][col] != self.objective[row][col]:
                    return False
        return True

    # Convert the board into a string so that we can print it
    def __str__(self):
        board_str = ""
        for row in self.board:
            board_str += str(row) + "\n"
        return board_str

    
    # < Operator override
    def __lt__(self, other):
        return (len(self.board) < len(other.board))
    
    # == operator override
    def __eq__(self, other):
        for row in range (len(self.board)):
            for col in range (len(self.board)):
                if (self.board[row][col] != other.board[row][col]):
                    return False
        return True


    def __hash__(self):
        return hash(tuple(map(tuple, self.board)))

