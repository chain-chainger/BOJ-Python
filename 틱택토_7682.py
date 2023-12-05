import sys
input = sys.stdin.readline

def check_win_condition(board, player):
	if board[0] == board[1] == board[2] == player:
		return True
	if board[0] == board[3] == board[6] == player:
		return True
	if board[0] == board[4] == board[8] == player:
		return True
	if board[1] == board[4] == board[7] == player:
		return True
	if board[2] == board[4] == board[6] == player:
		return True
	if board[2] == board[5] == board[8] == player:
		return True
	if board[3] == board[4] == board[5] == player:
		return True
	if board[6] == board[7] == board[8] == player:
		return True
	return False

while True:
	test_case = input().rstrip()
	if test_case == "end":
		break
	o_cnt, x_cnt = test_case.count('O'), test_case.count('X')
	if o_cnt == x_cnt and check_win_condition(test_case, 'O') and check_win_condition(test_case, 'X') == False:
		print("valid")
		continue
	elif o_cnt + 1 == x_cnt and check_win_condition(test_case, 'X') and check_win_condition(test_case, 'O') == False:
		print("valid")
		continue
	elif o_cnt == 4 and x_cnt == 5 and check_win_condition(test_case, 'O') == False:
		print("valid")
		continue
	print("invalid")
