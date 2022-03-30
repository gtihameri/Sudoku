class Field:
    """
    A sudoku field which consists of a value (default is 0 = empty),position information
    given by row, col and blk a list of permitted values, which is to be filled later by a
    sudoku board method
    """
    def __init__(self, row: int, col: int,  value: int = 0):
        self.row = row
        self.col = col
        self.blk = ((row - 1) // 3) * 3 + (col - 1) // 3
        self.value = value
        self.index = (row - 1) * 9 + col - 1
        self.related = self.find_related()

    def __str__(self) -> str:
        """When printing print the value"""
        return f' {str(self.value)}'

    def __lt__(self, other):
        return self.index < other.index

    def find_related(self):
        """
        Find all the fields that are related to this field.
        The fields that are in the same row, col or block
        """
        related = []
        for row in range(1, 10):
            for col in range(1, 10):
                blk = ((row - 1) // 3) * 3 + (col - 1) // 3
                if col == self.col or row == self.row or blk == self.blk:
                    related.append((row - 1) * 9 + col - 1)
        return related

class Sudoku:
    """
    Sudoku board consisting of an ordered list of field objects
    which link row/col/blk and value a filled attributed which tracks
    how many fields are already filled
    """
    _num_tries = 0

    def __init__(self, fields):
        self.position = []
        self.empty_pos = []
        if len(fields) != 81:
            print(f'Wrong length size ({len(fields)} expected is 81)')
            raise IndexError
        for ix, val in enumerate(fields):
            row = ix // 9 + 1
            col = ix % 9 + 1
            f = Field(row, col, val)
            self.position.append(f)
            if val == 0:
                self.empty_pos.append(f)
            self.empty_pos.sort()

    def __str__(self):
        """ Print the content of the sudoku in formated table """
        board_str = ''
        line_len = (len(f'{str(self.position[0]):7s}')) * 9 + 5
        print("")
        horizontal_separator = ' +' + '-' * line_len + '+\n'
        for p in range(81):
            if p % 27 == 0:
                if p == 0:
                    board_str += '\n' + horizontal_separator
                else:
                    board_str += '|\n' + horizontal_separator
            if p % 9 == 0:
                if p in [0, 27, 54]:
                    board_str += ' | '
                else:
                    board_str += '| \n | '
            elif p % 3 == 0:
                board_str += ' |'
            board_str += f'{str(self.position[p]):^7s}'
        board_str += '|\n' + horizontal_separator
        return board_str

    def valid_values(self, field: Field) -> list:
        """
        Find the valid values for a position from the range 1-10, excluding the values used on same row,
        same column and same block
        """
        if field.value == 0:
            values = set(range(1, 10))
            used_values = [self.position[i].value for i in field.related]
            values -= set(used_values)
        else:
            values = []
        return list(values)

    def next_field(self):
        """
        Returns the position of the next best position to fill. The best are the fields that have
        less valid values.
        """
        self.empty_pos.sort()
        for num_valid_values in range(1, 9):
            for pos in self.empty_pos:
                if len(self.valid_values(pos)) == num_valid_values:
                    return pos
        return False

    def solve(self) -> bool:
        """
        Solve the sudoku recursively. Try each valid values.
        """
        self.count_tries()
        position = self.next_field()
        if position:
            # try each valid values for that position
            for value in self.valid_values(position):
                position.value = value
                self.empty_pos.remove(position)
                if self.solve():
                    return True
                else:
                    # If not solved return value
                    position.value = 0
                    self.empty_pos.insert(0, position)
        else:
            if len(self.empty_pos) == 0:
                return True
        return False

    def count_tries(self):
        self._num_tries += 1
        if self._num_tries % 100_000 == 0:
            print(f'Number of trys {self._num_tries}')
            if self._num_tries == 1_000_000:
                print(f'  *****  Impossible to solve  *****')
                exit(0)

    def get_solved(self) -> list:
        return [p.value for p in self.position]
