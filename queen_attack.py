# -*- coding: utf-8 -*-
"""QueenAttack docstrings.

This module demonstrates documentation as specified by the LSV seedbed.

"""


class QueenAttack:

    """
    This is the model of the class.

    """

    def __init__(self):
        """
        This is the contructor of the class.

        """
        self.file = None
        self.queen_location = ()
        self.board = []
        self.board_size = None

    def read_file(self):
        """ Read a file.

            Parameters:
                None.

            Returns:
                file: The file with the data to run the QueenAttack.

        """
        try:
            self.file = open('data.txt')
            return self.file
        except FileNotFoundError:
            print('The file does not exists')
            return None

    def validate_file(self):
        """ Validate that a file is correct, set the queen's position on the board and set the size of the board.

            Parameters:
                None.

            Returns:
                list: list with the size of the board, amount of obstacles,
                      the Queen's position and the obstacles positions.

        """

        var = []
        for line in self.file.readlines():
            line = line.replace("\n", "")
            var.append(line.split(' '))
        if var[0][1].isnumeric() and var[0][0].isnumeric() and var[1][0].isnumeric() and var[1][1].isnumeric():
            if len(var) != int(var[0][1]) + 2:
                print('The file does not have the necessary lines')
                return None
            elif int(var[0][0])>990:
                print('The maximum size of the matrix is ​​990 * 990')
                return None
        else:
            print('Only Accept numeric data')
            return None
        enter = 0
        for item in var:
            if len(item) != 2:
                print('The lines have to contain two data, separated by a space')
                return None
            elif not item[0].isnumeric() or not item[1].isnumeric():
                print('All data must be numeric')
                return None
            elif enter > 0:
                if int(item[0]) > int(var[0][0]) or int(item[0]) < 1 or int(item[1]) > int(var[0][0]) or int(item[1]) < 1:
                    print('The data can not be less than 1 or the maximum number of the assigned table')
                    return None
            elif enter > 1:
                if var[1][0] == item[0] and var[1][1] == item[1]:
                    print('The position of the queen can not be repeated')
                    return None
            enter += 1
            # setting queen location
            self.queen_location = (int(var[1][0]) - 1, int(var[1][1]) - 1)
            # setting board size
            self.board_size = int(var[0][0])
        return var

    @staticmethod
    def setting_positions(var):
        """Generate the board with the position of the queen
           and the positions of the obstacles to iterate with these.


            Parameters:
                var(list):
                    list with the size of the board, amount of obstacles,
                    the Queen's position and the obstacles positions.



            Returns:
                list[list[str]]: The board with the position of the queen
                      and the positions of the obstacles to iterate with these.
        """
        table = []
        for i in range(int(var[0][0])):
            table.append([''] * int(var[0][0]))

        if int(var[0][1]) != 0:
            for i in range(2, int(var[0][1]) + 2):
                table[int(var[i][0]) - 1][int(var[i][1]) - 1] = 'X'
        table[int(var[1][0]) - 1][int(var[1][1]) - 1] = 'Q'
        return table

    def queen_attack_validation(self, queen_row, queen_column, move, count):
        """Calculate the possible movements of the queen on the board, move the queen across the board
           and validates that the queen does not leave the board.
            Parameters:
                queen_row (int): The row in which the queen will be.
                queen_column(int): The column in which the queen will be.
                move(list): A list with the movement that the queen will make.
                count(int): The possible movements of the queen.

            Returns:
                int: The int the which contain the posibles Queen's moves.
        """
        queen_row = queen_row + move[0]
        queen_column = queen_column + move[1]
        if self.board_size - 1 >= queen_row >= 0 and self.board_size - 1 >= queen_column >= 0:
            if self.board[queen_row][queen_column] != 'X':
                self.board[queen_row][queen_column] = 'o'
                count += 1
                return self.queen_attack_validation(queen_row, queen_column, move, count)
            else:
                return count
        else:
            return count

    def queen_position_validation(self):
        """Generate the Queen's moves and calculate the possible movements of the queen on the board.


            Parameters:
                None.

            Returns:
                int: The int the which contain the posibles Queen's moves.
        """
        q_move = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        count = 0
        for move in q_move:
            tem = self.queen_attack_validation(self.queen_location[0], self.queen_location[1], move, 0)
            count += tem
        return count

    @staticmethod
    def print_board(var, board):
        """Generate the board to show it on the screen.


            Parameters:
                var(list):
                    list with the size of the board, amount of obstacles,
                    the Queen's position and the obstacles positions.
                board(list[list[str]]):
                    The board with the position of the queen
                    and the positions of the obstacles to iterate with these.



            Returns:
                None.
        """
        for loop in range(int(var[0][0])):
            print("\n")
            for j in range(int(var[0][0])):
                print("|", end="")
                middle = (5 - len(str(board[loop][j]))) // 2
                for k in range(middle):
                    print(" ", end="")
                print(board[loop][j], end=" ")
                for k in range(middle):
                    print(" ", end="")
                if (5 - len(str(board[loop][j]))) % 2 != 0:
                    print(" ", end="")
            print("|", end="")

    def main(self):
        """The main method of the QueenAttack class.

            Parameters:
                None.

            Returns:
                str: Returns a string with the Queen's possible movements.
        """
        self.file = self.read_file()
        if self.file is not None:
            input_data = self.validate_file()
            if input_data is not None:
                self.board = self.setting_positions(input_data)
                output = self.queen_position_validation()
                self.print_board(input_data, self.board)
                return "\n Queen's possible movements = {}".format(output)


if __name__ == '__main__':
    queen_attack = QueenAttack()
    print(queen_attack.main())
