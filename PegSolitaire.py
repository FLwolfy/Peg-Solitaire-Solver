class PegSolitaire:
    def solve_test(board: str) -> None:
        import time
        start = time.time()
        answer = PegSolitaire.solve(board)
        end = time.time()
        print(f'It takes {end - start} seconds to run solve the peg solitaire with the following board:\n{board}The answer is:\n{answer}\n')
        
    def show_steps(board: str) -> None:
        def board_to_string(boardLst: list) -> str:
            return '\n'.join([''.join(row) for row in boardLst]) + '\n'
        
        answer = PegSolitaire.solve(board)
        board = [list(string) for string in (board).split("\n")[:-1]]
        
        if (answer == None): 
            print("There is no solution for this board!\n")
            return 
        
        print(f"The answer is:\n{answer}\n")
        print("--> STEP 0 [Original Board]:")
        print(board_to_string(board))
        stepCount = 1
        for step in answer:
            print(f"--> STEP {stepCount} ", end='')
            fr,fc,tr,tc = step[0],step[1],step[2],step[3]
            mr,mc = (fr + tr) // 2, (fc + tc) // 2
            print(f"[{fr, fc}->{tr, tc}]:")
            board[fr][fc] = 'X'
            board[mr][mc] = 'X'
            board[tr][tc] = 'O'
            print(board_to_string(board))
            stepCount += 1       
        
    def solve(board: str) -> list:
        '''
        The board should be in this form:\n
            XOX    \n
            XOX    \n
        XXXOXXX\n
        XXXOXXX\n
        XXXOXXX\n
            XOX    \n
            XOX    \n
        where 'X' stands for empty slots, 'O' stands for pegs. See Board.py for details.      
        '''
        boardLst = [list(string) for string in (board).split("\n")[:-1]]
        size = len(boardLst)
        assert(size % 2 == 1 and len(row) == size for row in boardLst)
        
        pegsPos = []
        for row in range(size):
            for col in range(size):
                if (boardLst[row][col] == 'O'):
                    pegsPos.append((row, col))
        
        memo = {} # store the situations that have already solved
    
        return PegSolitaire.__peg_solitaire_solver_inner(boardLst, pegsPos, [], memo)
        
    def __peg_solitaire_solver_inner(board: list, pegsPos: list, currentMoves: list, memo: dict) -> list:
        size = len(board)
        
        if(len(pegsPos) == 1 and board[size // 2][size // 2] == 'O'):
            return currentMoves
        elif(len(pegsPos) == 1):
            return None
        
        # Check in memory
        boardKey = tuple(tuple(row) for row in board)
        if boardKey in memo:
            return memo[boardKey]
        
        # Get reflections
        boardKey1 = tuple(tuple(row[::-1]) for row in board[::-1])
        boardKey2 = tuple(tuple(row[::-1]) for row in zip(*board))[::-1]
        boardKey3 = tuple(tuple(row) for row in zip(*board))
        boardKey4 = tuple(tuple(row) for row in board[::-1])
        boardKey5 = tuple(tuple(row[::-1]) for row in zip(*board))
        boardKey6 = tuple(tuple(row[::-1]) for row in board[::-1])
        boardKey7 = tuple(tuple(row) for row in zip(*board))[::-1]
        
        for pos in pegsPos:
            pegRow = pos[0]
            pegCol = pos[1]
            
            for row, col in [(pegRow - 2, pegCol),(pegRow + 2, pegCol),(pegRow, pegCol - 2),(pegRow, pegCol + 2)]:          
                if(row < 0 or row >= size or col < 0 or col >= size):
                    continue
                
                if(PegSolitaire.__check_move(board, pegRow, pegCol, row, col)):        
                    afterMove = PegSolitaire.__move(board, pegRow, pegCol, row, col, pegsPos)
                    result = PegSolitaire.__peg_solitaire_solver_inner(afterMove[0], afterMove[1], currentMoves + [afterMove[2]], memo)
                    if (result != None): # Backtracking
                        moves = [afterMove[2]] + result
                        moves1 = [(size - 1 - fr, fc, size - 1 - tr, tc) for fr, fc, tr, tc in moves]
                        moves2 = [(size - 1 - fr, size - 1 - fc, size - 1 - tr, size - 1 - tc) for fr, fc, tr, tc in moves]
                        moves3 = [(fr, size - 1 - fc, tr, size - 1 - tc) for fr, fc, tr, tc in moves]
                        moves4 = [(size - 1 - fr, fc, size - 1 - tr, tc) for fr, fc, tr, tc in moves]
                        moves5 = [(fr, size - 1 - fc, tr, size - 1 - tc) for fr, fc, tr, tc in moves]
                        moves6 = [(size - 1 - fr, size - 1 - fc, size - 1 - tr, size - 1 - tc) for fr, fc, tr, tc in moves]
                        moves7 = [(fr, size - 1 - fc, tr, size - 1 - tc) for fr, fc, tr, tc in moves]
                        
                        # Adding 8 reflected situations
                        memo[boardKey] = moves
                        memo[boardKey1] = moves1
                        memo[boardKey2] = moves2
                        memo[boardKey3] = moves3
                        memo[boardKey4] = moves4
                        memo[boardKey5] = moves5
                        memo[boardKey6] = moves6
                        memo[boardKey7] = moves7
                        return result 
        
        # Adding 8 reflected situations            
        memo[boardKey] = None
        memo[boardKey1] = None
        memo[boardKey2] = None
        memo[boardKey3] = None
        memo[boardKey4] = None
        memo[boardKey5] = None
        memo[boardKey6] = None
        memo[boardKey7] = None                                            
        return None
            
    def __check_move(board: list, pegRow: int, pegCol: int, toRow: int, toCol: int) -> bool:
        midRow = (pegRow + toRow) // 2
        midCol = (pegCol + toCol) // 2
        
        return board[midRow][midCol] == 'O' and board[toRow][toCol] == 'X'

    def __move(board: list, fromRow: int, fromCol: int, toRow: int, toCol: int, pegsPos: list) -> tuple:
        boardCopy = [row[:] for row in board] # deep copy
        pegsPosCopy = pegsPos[:]
        
        midRow = (fromRow + toRow) // 2
        midCol = (fromCol + toCol) // 2
        
        boardCopy[fromRow][fromCol] = 'X'
        boardCopy[midRow][midCol] = 'X'
        boardCopy[toRow][toCol] = 'O'
        
        pegsPosCopy.remove((fromRow,fromCol))
        pegsPosCopy.remove((midRow,midCol))
        pegsPosCopy.insert(0, (toRow,toCol)) # Make sure go through the same peg first until blocked
        
        return (boardCopy, pegsPosCopy, (fromRow, fromCol, toRow, toCol))