print("Solve Sudoku2")

Sudoku_Board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]
Sudoku_Number_Board= list()



def Get_Board(): # 원본 보드를 보여준다.
  for i in range(9):
    print(Sudoku_Board[i])


def Set_Board(): # 보드를 입력받는다.
  try:
    for i in range(9):
      line = input()
      for j in range(9):
        Sudoku_Board[i][j] = int(line[j * 2])

  except:
    print("다른 입력이 받아짐")
    return None


# 보드가 정상 범위 안에 있는지 확인한다.

def SearchInSquare(y, x, num): # 해당 위치가 속해있는 구역을 찾고, 그 구역에서 입력받은 num과 같은 값이 있는지 확인한다. return bool
  PosX = x // 3
  PosY = y // 3
  for b in range(PosY * 3, (PosY + 1) * 3):
    for a in range(PosX * 3, (PosX + 1) * 3):
      if Sudoku_Board[b][a] is num:
        return False
  return True


def SearchInWidth(y, x, num): # 해당 위치가 속해있는 가로줄에서 입력받은 num과 같은 값이 있는지 확인한다. return bool
  for a in range(0, 9):
    if Sudoku_Board[y][a] is num:
      return False
  return True


def SearchInVertex(y, x, num): # 해당 위치가 속해있는 세로줄에서 입력받은 num과 같은 값이 있는지 확인한다. return bool
  for a in range(0, 9):
    if Sudoku_Board[a][x] is num:
      return False
  return True


def NakedSingle(y, x, num): # 각 칸을 기준으로, 그 칸이 속한 가로줄, 세로줄과 3x3 칸 내에 속한 다른 중복된 번호들을 후보목록에서 제거한다.  

  if not SearchInSquare(y, x, num): # 해당 구역안에 이미 숫자가 존재하는 경우 그 구역에는 더이상 해당 값이 들어갈 수 없기 때문에 해당 구역을 정리해준다.
    posx = x // 3
    posy = y // 3
    for i in range(posy * 3, (posy + 1) * 3):
      for j in range(posx * 3, (posx + 1) * 3):
        Sudoku_Number_Board[i * j * 9 + num] = -1

  if not SearchInWidth(y, x, num):
    for i in range(0, 9):
      Sudoku_Number_Board[i * y * 9 + num] = -1

  if not SearchInVertex(y, x, num):
    for i in range(0, 9):
      Sudoku_Number_Board[i * x * 9 + num] = -1

  if SearchInSquare and SearchInWidth and SearchInVertex :
    return True

  return False


def MakeNumberBoard():
  try:
    for i in range(0, 9):
      for j in range(0, 9):
        for k in range(1, 10):
          Sudoku_Number_Board.append(k)
  except:
    print("ERROR")
  return None


def DoHiddenSingle(y, x):

  return None

def HiddenSingle(y, x, num): # 주어진 3x3 칸 내에 어떤 숫자가 들어갈 수 있는 칸이 단 하나만 있다면, 그 칸에는 그 숫자가 들어가야만한다.

  return None

def DoNakedSingle(y, x):
  rear = [0, 0, 0, 0] # 갯수 / 최근 y / 최근 x / 최근 값

  for num in range(1, 10): # 값을 찾아 바꾸는데 성공하면 True 실패하면 False
    if NakedSingle(y, x, num): # True인 경우 해당 위치에 값이 들어갈 수 있다.
      rear[0] += 1
      rear[1] = y
      rear[2] = x
      rear[3] = num
  if rear[0] is 1:
    Sudoku_Board[rear[1]][rear[2]] = rear[3]
    return True
  return False

def DoSolving():
  for count in range(1000):
    for i in range(0, 9):
      for j in range(0, 9):
        if Sudoku_Board[i][j] is 0:
          SolveSudoku(i, j)
        else:
          for k in range(0, 9):
            Sudoku_Number_Board[i * j * 9 + k] = -1

  return None

def SolveSudoku(y, x):
  if DoNakedSingle(y, x):
    print("DoNakedSingle")
  elif DoHiddenSingle(y, x):
    print("DoHiddenSingle")


Set_Board()
MakeNumberBoard()
DoSolving()
Get_Board()


print("GOOD")

#Set_Board()
#Get_Board()


