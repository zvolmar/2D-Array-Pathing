#Goal is to create a grid of 0s that is iterated through algorithmically to get from 1 to 111.
#999 acts as an obstacle for the algorithm to work around. I have not figured out how to accomplish this algorithmically, hence the comments on the lines related.

#Creates grid
n=7
rows=n
cols=n
board=[[0 for x in range(rows)] for y in range(cols)]

#Shorthand for row and column length
nrows=len(board)
ncols=len(board[0])

#Sets the start and end goal
board[0][0]=1
board[n-1][n-1]=111
#board[n//2][n//3]=999

#Checks adjacent grid locations and changes them based on their current value. If it's 0, it gets iterated through, otherwise it's left alone.
def getAdj(i,j,x):
    for i2 in range(i-1,i+1):
        for j2 in range(j-1,j+1):
            if (-1<i<(nrows-1)) and (-1<j<(ncols-1)):
                if board[i+1][j]==0:
                    board[i+1][j]=x+1
                if board[i][j+1]==0:
                    board[i][j+1]=x+1
#Cycles through the grid itself, changing the value of each tile to mark where it's been, as well as incrementing adjacent nodes to indicate a valid path.
def boardFill():
    for i in range(nrows):
        for j in range(ncols):
           # if board[i][j]!=999:
                x=(board[i][j])
                getAdj(i,j,x)
                x+=1
        print(board[i])

           



boardFill()
