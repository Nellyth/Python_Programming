class QueenAttack:

    def __init__(self):
        self.file = None
        self.queen_location = ()
        self.board = []
        self.board_size = None

    def read_file(self):
        try:
            self.file = open('data.txt')
            return self.file
        except FileNotFoundError:
            print('The file does not exists')
            return None

    def validate_file(self):
        var = []
        for line in self.file.readlines():
            line = line.replace("\n", "")
            var.append(line.split(' '))
        if var[0][1].isnumeric() or var[0][0].isnumeric():
            if len(var) != int(var[0][1]) + 2:
                print('The file does not have the necessary lines')
                return None
            if int(var[0][0])>990:
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
            if not item[0].isnumeric() or not item[1].isnumeric():
                print('All data must be numeric')
                return None
            if int(item[0]) > int(var[0][0]) or int(item[0]) < 1 or int(item[1]) > int(var[0][0]) or int(item[1]) < 1:
                print('The data can not be less than 1 or the maximum number of the assigned table')
                return None
            if enter > 1:
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
        table = []
        for i in range(int(var[0][0])):
            table.append([''] * int(var[0][0]))

        if int(var[0][1]) != 0:
            for i in range(2, int(var[0][1]) + 2):
                table[int(var[i][0]) - 1][int(var[i][1]) - 1] = 'X'
        table[int(var[1][0]) - 1][int(var[1][1]) - 1] = 'Q'
        return table

    def queen_attack_validation(self, queen_file, queen_column, move, count):
        queen_file = queen_file + move[0]
        queen_column = queen_column + move[1]
        if self.board_size - 1 >= queen_file >= 0 and self.board_size - 1 >= queen_column >= 0:
            if self.board[queen_file][queen_column] != 'X':
                self.board[queen_file][queen_column] = 'o'
                count += 1
                return self.queen_attack_validation(queen_file, queen_column, move, count)
            else:
                return count
        else:
            return count

    def queen_position_validation(self):
        q_move = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        count = 0
        for move in q_move:
            tem = self.queen_attack_validation(self.queen_location[0], self.queen_location[1], move, 0)
            count += tem
        return count

    @staticmethod
    def print_board(var, board):
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
