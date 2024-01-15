import math

X = "X"
O = "O"
emp = None


def initial_state():
    return [[emp, emp, emp],
            [emp, emp, emp],
            [emp, emp, emp]]


def player(board):
    count_x_turn=0
    count_o_turn=0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_x_turn+=1
            elif board[i][j] == O:
                count_o_turn+=1
    
    if count_o_turn > count_x_turn:
        return X
    else:
        return O


def actions(board):
    acts=[]
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                acts.append((i,j))
    
    return acts


def result(board, action):
    next_player=player(board)
    (x,y) = action
    new_board=initial_state()
    for i in range(3):
        for j in range(3):
            if x == i and y == j:
                new_board[i][j] = next_player
            else:
                new_board[i][j] = board[i][j] 
    return new_board


def winner(board):
    winner=utility(board)
    if winner == 0:
        return None
    elif winner == 1:
        return "X"
    elif winner == -1:
        return "O"


def terminal(board):
    coor_X=[]
    coor_Y=[]
    filled=True
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                coor_X.append((i,j))
            elif board[i][j] == "O":
                coor_Y.append((i,j))
            elif board[i][j] == None:
                filled=False
    
    if len(coor_X) > 2 or len(coor_Y) > 2:
        if check(coor_X):
            return True
        if check(coor_Y):
            return True
    
    if filled:
        return True
    else:
        return False


def utility(board):
    coor_X=[]
    coor_Y=[]
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                coor_X.append((i,j))
            elif board[i][j] == "O":
                coor_Y.append((i,j))
    
    if len(coor_X) > 2 or len(coor_Y) > 2:
        if check(coor_X):
            return 1
        if check(coor_Y):
            return -1
    
    return 0


def minimax(board):
    current_player=player(board)
    acts=actions(board)
    utilities=[]
    for act in acts:
        r=result(board,act)
        if terminal(r):
            score = utility(r)
            utilities.append(score)
        else:
            a = minimax(r)
            re = result(r,a)
            score = utility(re)
            utilities.append(score)
    
    max = [0,-1]
    least = [0,1]
    for index,score in enumerate(utilities):
        if max[1] < score:
            max[1] = score
            max[0] = index
        if least[1] > score:
            least[1] = score
            least[0] = index
    
    if current_player == X:
        return acts[max[0]]
    elif current_player == O:
        return acts[least[0]]


def check(_map):
    c=0
    c1=0
    abscissa=[]
    ordinate=[]
    for (i,j) in _map:
        abscissa.append(i)
        ordinate.append(j)
        if i+j == 2:
            c+=1
        if i == j:
            c1+=1
    if c == 3:
        return True
    if c1 == 3:
        return True
    
    count_x=[0,0,0]
    for i in abscissa:
        count_x[i]=count_x[i]+1
    
    count_y=[0,0,0]
    for i in ordinate:
        count_y[i]=count_y[i]+1
    for x in count_x:
        for y in count_y:
            if x == 3 or y == 3:
                return True
    
    return False

