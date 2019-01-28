#Tic Tac Toe
#print the game board

def print_horiz_line():
  print(" --- " * board_size)

def print_vert_line():
  print("|   " * (board_size + 1))

board_size = int(input("What size of game board? "))

for index in range(board_size):
  print_horiz_line()
  print_vert_line()

#find who wins
set_horiz = ()
set_vertic = ()

def horiz_match(game):
  for i in range(3):
    set_horiz = set(game[i])
    if len(set_horiz) == 1 and game[i][0] != 0:
      return game[i][0]
  return 0

def diag_match(game):
  if game[1][1] != 0:
    if game [1][1] == game[0][0] == game[2][2]:
      return game[1][1]
    elif game [1][1] == game[0][2] == game[2][0]:
      return game[1][1]
  return 0

def vertic_match(game):
  for i in range(0,3):
    column = set([game[0][i], game[1][i], game[2][i]])
    if len(column) == 1 and game[1][i] !=0:
      return game[0][i]
  return 0


def print_winner(game):
  if horiz_match(game) != 0:
    print("Player {} wins".format(horiz_match(game)))
  elif diag_match(game) != 0:
    print("Player {} wins".format(diag_match(game)))
  elif vertic_match(game) !=0:
    print("Player {} wins".format(vertic_match(game)))
  else:
    print("No winner")

print_winner([[2, 2, 0],
  [2, 1, 0],
  [2, 1, 1]])

print_winner([[1, 2, 0],
  [2, 1, 0],
  [2, 1, 1]])

print_winner([[1, 2, 0],
  [2, 1, 0],
  [2, 1, 2]])

