

player1 = ""
player2 = ""
z = 1


def find(n_list):  # Function for ending the game if someone wins, or the board fills up.
    h = 15
    while h > -1:
        if n_list[h] is True:
            return h
        h -= 1
    return 16


def check_board(x):  # This checks the board each turn for a winning game state.

    y = [0, 1, 2]
    m = 2
    truth_table = []

    while m > 0:  # Generates a truth table for each possible win.

        n = 2

        while n > -1:
            win1 = all(i == m for i in x[n])
            win2 = all(x[i][n] == m for i in y)
            truth_table.append(win1)
            truth_table.append(win2)
            n -= 1

        win3 = all(x[i][i] == m for i in y)
        win4 = all(x[2 - i][i] == m for i in y)
        truth_table.append(win3)
        truth_table.append(win4)
        m -= 1

    if find(truth_table) in [0, 1, 2, 3, 4, 5, 6, 7]:  # If any of the first half are true, player 2 wins.
        print("\nPlayer 2 wins!")
        return 1

    elif find(truth_table) in [8, 9, 10, 11, 12, 13, 14, 15]:  # And vice versa.
        print("\nPlayer 1 wins!")
        return 1

    n = 2
    t = []

    while n > -1:
        test = all(game_board[i][n] != 0 for i in y)
        t.append(test)
        n -= 1

    if t.count(True) == 3 and find(truth_table) == 16:
        print("\nNo one wins! Try again!")
        return 1

    else:
        return 0


def cpu_move():  # This is my Tic Tac Toe 'AI'

    b = 0
    x = 0
    y = [0, 1, 2]
    player_one = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    player_two = [[2, 2, 0], [2, 0, 2], [0, 2, 2]]

    move_row = [8]
    move_col = [8]
    move_dia_one = [8]
    move_dia_two = [8]

    move_center = [8]
    move_corner = [8]
    move_side = [8]

    while b < 2 and x == 0:  # Checks game board states for a win, prioritizing victory.

        for i in y:

            check_row = []
            check_col = []
            check_dia_one = []
            check_dia_two = []

            for n in y:  # Algorithm for checking each game state

                row = game_board[i][n]
                col = game_board[n][i]
                dia_one = game_board[n][n]
                dia_two = game_board[2-n][n]

                check_row.append(row)
                check_col.append(col)
                check_dia_one.append(dia_one)
                check_dia_two.append(dia_two)

            players = player_two, player_one
            all_moves = move_row, move_col, move_dia_one, move_dia_two
            check_all = check_row, check_col, check_dia_one, check_dia_two

            if x == 0:

                w = 0

                while w < 4 and x == 0:

                    if check_all[w] in players[b]:  # Records which column results in a win for a player if any

                        all_moves[w].append(i)
                        x += 1

                    w += 1

        b += 1

    if x == 0:

        if game_board[1][1] == 0:  # Records if the center space is empty assuming no player can win in one move

            move_center.append(1)
            x += 1

    if x == 0:

        w = 0
        loop = [0, 0, 2, 2, 0]

        while w < 4 and x == 0:

            if game_board[loop[w]][loop[w + 1]] == 0:  # Checks corners next; starting top left => bottom right.

                move_corner.append(w)
                x += 1

            w += 1

    if x == 0:

        w = 0
        loop = [0, 1, 2, 1, 0]

        while w < 4 and x == 0:

            if game_board[loop[w]][loop[w + 1]] == 0:  # Checks side spaces last.

                move_side.append(w)
                x += 1

            w += 1

#   Whichever state the board is in, the row or column is sent to another variable.

    move_table = move_row + move_col + move_dia_one + move_dia_two + move_center + move_corner + move_side

    if move_table[1] != 8:  # If a row was selected, finds the column of the needed row and returns the move.

        y = [0, 1, 2]

        for i in y:

            if move_table[1] == i:

                find_col = game_board[i].index(0) + 1
                return "{}, {}".format(i + 1, find_col)

    elif move_table[2] != 8:  # If a column was selected finds the row of the needed column and returns the move.

        y = [0, 1, 2]
        temp_rows = [[game_board[0][0], game_board[1][0], game_board[2][0]],
                     [game_board[0][1], game_board[1][1], game_board[2][1]],
                     [game_board[0][2], game_board[1][2], game_board[2][2]]]

        for i in y:

            if move_table[2] == i:

                find_row = temp_rows[i].index(0) + 1
                return "{}, {}".format(find_row, i + 1)

    elif move_table[3] != 8:  # If a diagonal was selected, returns the empty space.

        temp_dia = [game_board[0][0], game_board[1][1], game_board[2][2]]
        find_move = temp_dia.index(0) + 1
        return "{}, {}".format(find_move, find_move)

    elif move_table[4] != 8:  # If the opposite diagonal was selected, returns the empty space.

        y = [0, 1, 2]
        temp_dia = [game_board[2][0], game_board[1][1], game_board[0][2]]

        for i in y:

            if temp_dia[i] == 0:

                return "{}, {}".format(3 - i, 1 + i)

    elif move_table[5] != 8:  # Returns the center space if it is open and no one can win in one turn.

        return "2, 2"

    elif move_table[6] != 8:  # Returns a corner if open in order from top left to bottom right.

        y = [0, 1, 2, 3]
        loop = [1, 1, 1, 3, 3, 1, 3, 3]

        for i in y:

            if move_table[6] == i:

                return "{}, {}".format(loop[2 * i], loop[2 * i + 1])

    elif move_table[7] != 8:  # Finally, if no other cond were met, returns side; starting top, rotating clockwise.

        y = [0, 1, 2, 3]
        loop = [1, 2, 3, 2, 2, 3, 2, 1]

        for i in y:

            if move_table[7] == i:

                return "{}, {}".format(loop[2 * i], loop[2 * i + 1])


def player_move(a, b, player):  # This is for handling player responses.
    if a in ["1", "2", "3"] and b in ["1", "2", "3"]:

        x = int(a)
        y = int(b)

        if game_board[(x - 1)][(y - 1)] != 0:  # Condition for an entry that is already filled.

            print("\nThat space is already filled!")
            return 1

        game_board[(x - 1)].insert((y - 1), player)  # This generates a new board after a move.
        game_board[(x - 1)].pop(y)

        print("")
        print(game_board[0])
        print(game_board[1])
        print(game_board[2])

        return 0

    elif player1 == "quit      " or player2 == "quit      ":  # Allows either player to quit.

        return 2

    elif player2 == "reset      " or player2 == "reset      ":  # Allows either player to reset the board.

        return 2

    elif player1 != '' or player2 != '':  # In case someone enters something other then a move:

        print("\nPlease enter ROW [1, 2, 3], COL [1, 2, 3]")
        return 1


while z == 1:  # Loop for alternating player turns.

    u = 1
    game_board = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

    print("")
    print(game_board[0])
    print(game_board[1])
    print(game_board[2])

    game_type = input("\nWould you like to play 1 player or 2 player? ENTER '1' or '2' []: ")

    if game_type != "1":

        if game_type == "quit":
            u += 1
            z += 1

        if game_type != "2":
            print("\nYou have failed to select '1' or '2'.\n"
                  "2 player selected by default. To restart type: 'reset'")

    while u == 1 or u == 2:

        while u == 1:

            player1 = input("\nPlayer 1 enter move: ROW, COL []: ")

            if player1 == "reset":
                u += 2

            elif player1 == "quit":
                u += 2
                z += 1

            player1 = player1 + "      "
            repeat_turn = player_move(player1[0], player1[3], 1)
            game_over = check_board(game_board)

            if game_over == 1:
                u += 1

            elif repeat_turn == 1:
                u -= 1

            u += 1

        while u == 2:

            if game_type == "1":

                player2 = cpu_move()

            elif game_type == "2" or game_type != "":

                player2 = input("\nPlayer 2 enter move: ROW, COL []: ")

            if player2 == "reset":
                u += 2

            elif player2 == "quit":
                u += 2
                z += 1

            player2 = player2 + "      "
            repeat_turn = player_move(player2[0], player2[3], 2)
            game_over = check_board(game_board)

            if game_over == 1:
                u += 2

            if repeat_turn == 1:
                u += 1

            u -= 1
