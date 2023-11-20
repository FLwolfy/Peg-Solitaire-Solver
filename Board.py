import random

##  NOTICE:
##  All the rows and columns are ranging from 0 - 6 in the following boards
##  Spaces, periods, and pegs all count as one unit in the coordinates, row goes from up to down, column goes from left to right

def generate_board(pegCount: int = None) -> str:
    '''
    This will return a board with pegCount pegs. pegs should be between 0-32.
    NOTICE: Too large unsolveable boards may will lead to forever run!!!
    '''
    if (pegCount == None): pegCount = random.randint(1,32)
    assert(pegCount >= 1 and pegCount <= 32)
    
    fixed_board = """  XXX  \n  XXX  \nXXXXXXX\nXXXXXXX\nXXXXXXX\n  XXX  \n  XXX  \n"""

    board = [list(string) for string in (fixed_board).split("\n")[:-1]]
    slots = [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 2), (5, 3), (5, 4), (6, 2), (6, 3), (6, 4)]           
    
    posIndex = random.sample(range(0, 33), pegCount)
    for index in posIndex:
        slot = slots[index]
        board[slot[0]][slot[1]] = 'O'
      
    board_str = '\n'.join([''.join(row) for row in board]) + '\n'
    return board_str

##  Here are some example boards
board3 = """\
  XXX  
  XOX  
XOOXXXX
XXXXXXX
XXXXXXX
  XXX  
  XXX  
"""
board10 = """\
  XXX  
  XOX  
XXOOXOX
XOXXXOX
XXOXOXX
  OXO  
  XXX  
"""
board14 = """\
  XXX  
  OOX  
XXOXOOX
OOXXOOX
XOOOXXO
  XOX  
  XXX  
"""
board16 = """\
  XXX  
  OOX  
XXOOXXX
XXOOXOO
OOOXXOO
  OOX  
  XOX  
"""
board32 = """\
  OOO  
  OOO  
OOOOOOO
OOOXOOO
OOOOOOO
  OOO  
  OOO  
"""