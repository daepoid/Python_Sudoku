print("Solve Sudoku")
#http://theyearlyprophet.com/solving-every-sudoku-puzzle.html

upper_Board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
Sudoku_Board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# 해당 리스트를 복사하여 해당 값이 몇 번 사용되었는가를 확인한다.1


#        0  1  2  3  4  5  6  7  8  9
Table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# 원본 보드를 보여준다.

def Get_Board():
  for i in range(9):
    print(Sudoku_Board[i])


# 보드를 입력받는다.
def Set_Board():
  try:
    for i in range(9):
      line = input()
      for j in range(9):
        Sudoku_Board[i][j] = int(line[j * 2])

  except:
    print("다른 입력이 받아짐")
    return None

    # 보드가 정상 범위 안에 있는지 확인한다.


# 범위 외의 숫자가 들어올 경우
def Check_Board_Range(board):
  for i in range(9):
    for j in range(9):
      if board[i][j] in range(0, 10):
        continue
      else:
        print("범위 초과")


# 지정된 위치에 잘못된 문자가 들어온 경우를 조사
# 세가지의 확인을 통해 검사
# Check_Board_Overlap(Sudoku_Board_temp, y, x)
def Check_Board_Overlap(board, y, x):
  flag = True
  # 9개의 구역으로 나누어 해당 구역의
  pos_X = x // 3  # 몫이 0, 1, 2으로
  pos_Y = y // 3  # 구분된다.
  # 중복되는 값이 없다면 true, 있다면 false
  if not Check_Square_Part(board, pos_Y, pos_X) and flag is True:
    #print("사각형 안에서 중복")
    flag = False

  if not Check_Width_Part(board, y, x) and flag is True:
    #print("횡방향 범위에서 중복")
    flag = False

  if not Check_Vertical_Part(board, y, x) and flag is True:
    #print("종방향 범위에서 중복")
    flag = False

  return flag


# 문제가 있으면 False 없으면 True
def Check_Square_Part(board, y, x):
  flag = True
  Copy_Table = Table.copy()
  for i in range(y * 3, (y + 1) * 3):
    for j in range(x * 3, (x + 1) * 3):
      Copy_Table[board[i][j]] += 1
  for i in range(1, 10):
    if Copy_Table[i] > 1:
      flag = False
      return flag
  return flag


def Check_Width_Part(board, y, x):
  flag = True
  Copy_Table = Table.copy()
  for i in range(0, 9):
    Copy_Table[board[y][i]] += 1
  for i in range(1, 10):
    if Copy_Table[i] > 1:
      flag = False
      return flag
  return True


def Check_Vertical_Part(board, y, x):
  Copy_Table = Table.copy()
  flag = True
  for i in range(0, 9):
    Copy_Table[board[i][x]] += 1
  for i in range(1, 10):
    if Copy_Table[i] > 1:
      flag = False
      return flag
  return True


def Check_Board_Hard(board, y, x):
  '''
  해당 위치에 해당 값이 들어갈 수 밖에 없는 값인지 확인하는 부분
  x,y가 속해있는 공간을 찾고 그 공간 안에 모든 숫자들을 돌아가면서 해당 값이 들어갈 수 있는지 확인한다.
  '''
  
  count = 0
  num = board[y][x] # 해당 위치에 이미 값이 집어 넣어져있는 상태로
  board[y][x] = 0  # 함수 안으로 들어왔기 때문에 그 값을 추출하고 그 위치를 초기화한다.

  Pos_X = x // 3
  Pos_Y = y // 3
  for b in range(Pos_Y, Pos_Y * 3):
    for a in range(Pos_X, Pos_X * 3):
      if board[b][a] is 0: # 해당 위치에 이미 정해져있는 값이 없는 경우.
        if a is x and b is y: # 해당 위치에 함수에 들어오기 전에 미리 확인해둔 위치인 경우.
          continue 
        else: # 해당 위치에 함수에 들어오기 전에 미리 확인하지 않은 위치인 경우
          board[b][a] = num # 값을 집어넣는다.
          if Check_Board_Overlap(board, y, x): # 확인하는 함수에 값을 집어넣고 8개 공간 모두 실패한다면 미리 확인해둔 위치가 정답이다. 
            count += 1
          board[b][a] = 0
      else: # 해당 위치에 이미 정해져있는 값이 있는 경우
        count += 1
    
  if count is 8:
    # 미리 확인해둔 값이 정답
    return True
  else:
    return False
    # 다른 공간에도 해당 값이 들어갈 가능성이 있음.


def Check_In_Square(board, y, x):
  Pos_X = x // 3
  Pos_Y = y // 3
  count = 0
  Copy_Table = Table.copy()
  for j in range(Pos_Y * 3, (Pos_Y + 1) * 3):
    for i in range(Pos_X * 3, (Pos_X + 1) * 3):
      if board[j][i] is not 0:
        count += 1
        Copy_Table[board[j][i]] += 1
  if count is 8:
    for k in range(1, 10):
      if Copy_Table[k] is 0:
        return Copy_Table[k]


def Check_Board(board, y, x): # Sudoku_Board 안에 집어넣어 갱신할 값을 int로 return 한다.
  count = 0
  rear = 0
  for i in range(1, 10):
    board[y][x] = i
    if Check_Board_Overlap(board, y, x): # 해당 위치에는 i값이 들어갈 수 있는 위치임.
      count += 1
      rear = i
      # 주변에 8개의 공간에서 값을 찾아 이 장소에 꼭 와야하는 숫자를 찾는다.
      if Check_Board_Hard(board, y, x): 
        return i
      
    board[y][x] = 0
  if count is 1:
    return rear
  else:
    return 0
 


#풀이
'''
1. 위치 하나를 잡는다.
2. 해당 위치에 값이 있으면 pass
3. 해당 위치에 값이 없으면 주변을 확인한다.
4. 해당 위치에 들어갈 값이 하나라면 해당 위치에 집어넣는다.
5. 값이 하나가 아니라면 다음위치로 넘어간다.
'''


def solving(board):
  track = 0
  while track < 100:
    for i in range(0, 9):
      for j in range(0, 9):
        if board[i][j] is 0:
          board[i][j] = Check_Board(board, i, j)
          if board[i][j] is 0:
            # TODO: 해당 부분 수정
            return None
          else:
            print("track : ", track)        
    track += 1


# main
# 첫 입력은 문제가 없는 보드가 들어온다고 가정한다.
# 1. 보드를 받는다.
Set_Board()
# 2. 문제를 푼다
solving(Sudoku_Board)
# 3. 보여준다
Get_Board()
