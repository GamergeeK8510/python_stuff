player1 = ""
player2 = ""
z = 1

while z == 1:
    game_board = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

    print("")
    print(game_board[0])
    print(game_board[1])
    print(game_board[2])


    def find(n_list):
        h = 15
        while h > -1:
            if n_list[h] is True:
                return h
            h -= 1
        return 16


    def check_board(x):

        y = [0, 1, 2]
        m = 2
        truth_table = []

        while m > 0:

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

        if find(truth_table) in [0, 1, 2, 3, 4, 5, 6, 7]:
            print("\nPlayer 2 wins!")
            return 1

        elif find(truth_table) in [8, 9, 10, 11, 12, 13, 14, 15]:
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


    def player_move(a, b, player):

        if a in ["1", "2", "3"] and b in ["1", "2", "3"]:
            x = int(a)
            y = int(b)

            if game_board[(x - 1)][(y - 1)] != 0:
                print("\nThat space is already filled!")
                return 1

            game_board[(x - 1)].insert((y - 1), player)
            game_board[(x - 1)].pop(y)
            print("")
            print(game_board[0])
            print(game_board[1])
            print(game_board[2])
            return 0

        elif player1 == "quit      " or player2 == "quit      ":
            pass
        elif player2 == "reset      " or player2 == "reset      ":
            pass

        else:
            print("\nPlease enter ROW [1, 2, 3], COL [1, 2, 3]")
            return 1


    u = 1

    while u == 1 or u == 2:

        while u == 1:

            player1 = input("\nPlayer 1 enter move: ROW, COL []: ")

            if player1 == "reset":
                u += 1
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
