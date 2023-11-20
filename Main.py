from PegSolitaire import PegSolitaire
import Board

steps3 = PegSolitaire.solve(Board.board3)
steps10 = PegSolitaire.solve(Board.board10)

PegSolitaire.solve_test(Board.board3)
PegSolitaire.solve_test(Board.board10)
PegSolitaire.solve_test(Board.board14)
PegSolitaire.solve_test(Board.board16)
PegSolitaire.solve_test(Board.board32)

PegSolitaire.solve_test(Board.generate_board(3))
PegSolitaire.solve_test(Board.generate_board(10))
PegSolitaire.solve_test(Board.generate_board(16))

PegSolitaire.show_steps(Board.board3)
PegSolitaire.show_steps(Board.board10)
PegSolitaire.show_steps(Board.board14)

PegSolitaire.show_steps(Board.generate_board(3))