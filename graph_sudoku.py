from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from sudoku import Sudoku as SudokuSolver

Window.clearcolor = (1, 1, 1, 1)


class DigitInput(TextInput):
    """ Class to accept Input only integers fro 1-9"""
    min_value = NumericProperty()
    max_value = NumericProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.input_filter = 'int'
        self.multiline = False

    # Overwrite the insert_text method
    def insert_text(self, string, from_undo=False):
        new_text = self.text + string
        if new_text.isdigit():
            if self.min_value <= int(new_text) <= self.max_value:
                TextInput.insert_text(self, string, from_undo=from_undo)

class Board(BoxLayout):
    """ Create a 9 x 9 board with 9 blocks 3 x 3"""
    fields = [0] * 81
    block = [None] * 9

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        bsize = .33333
        fsize = 25
        fwidth = 30
        self.game_box = GridLayout(cols=3, size_hint=(1, .9))
        # Create tha blocks
        for i in range(9):
            self.block[i] = GridLayout(cols=3, size_hint=(.33, .1),
                                       spacing=(5, 5), padding=(10, 10))
            self.game_box.add_widget(self.block[i])

        # Create the 9 x 9 tables and set the position of field inside blocks
        for i in range(81):
            blk = ((i // 9) // 3) * 3 + (i % 9) // 3
            self.fields[i] = DigitInput(font_size=fsize, height=bsize, width=fwidth, halign='center',
                                        size_hint=(.9, 9), min_value=1, max_value=9)
            self.block[blk].add_widget(self.fields[i])

        # Create the Solve and Clear buttons
        self.button_box = BoxLayout(size_hint=(1, .1))
        self.solve = Button(text="Solve", font_size=fsize, size_hint=(.5, .9))
        self.solve.bind(on_press=self.solve_game)
        self.clear = Button(text="Clear", font_size=fsize, size_hint=(.5, .9))
        self.clear.bind(on_press=self.clear_board)
        self.button_box.add_widget(self.solve)
        self.button_box.add_widget(self.clear)
        # put the table and the buttons inside the board
        self.add_widget(self.game_box)
        self.add_widget(self.button_box)

    def get_values(self):
        """ Return the content of the board in 81 position list """
        mygame = [0] * 81
        for i in range(81):
            value = self.fields[i].text
            if value.isnumeric():
                mygame[i] = int(value)
        return mygame

    def update_board(self, values):
        """ Updates the board with the values """
        for i in range(81):
            self.fields[i].text = str(values[i])

    def solve_game(self, instance):
        """ Calls the SudokuSolver class to try to solve the sudoku """
        game = SudokuSolver(self.get_values())
        if game.solve():
            print('=========== Game Solved ==============')
        else:
            print('=========== Game Not Solved ==============')
        self.update_board(game.get_solved())
        del game

    def clear_board(self, instance):
        """ Fill the whole boar with blank spaces"""
        for i in range(81):
            self.fields[i].text = ''

class SudokuBoard(App):
    def build(self):
        return Board()

if __name__ == '__main__':
    SudokuBoard().run()
