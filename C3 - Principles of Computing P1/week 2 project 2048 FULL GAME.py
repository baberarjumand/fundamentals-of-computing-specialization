"""
http://www.codeskulptor.org/#user47_sVP5DBhCSVbdSbN.py
Clone of 2048 game.
"""

import poc_2048_gui
#import poc_simpletest as tsuite
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def slide_items_left(line):
    """
    Helper function that slides all items to the left in a list
    """    
    input_list = list(line)
    slide_list = [0] * len(input_list)
    slide_list_idx = 0
    for val in input_list:        
        if val != 0:
            slide_list.insert(slide_list_idx, val)
            slide_list_idx += 1
            slide_list.pop()
    return slide_list

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    input_list = list(line)    
    slid_items = slide_items_left(input_list)
    for idx in range(0, len(slid_items) - 1):
        if slid_items[idx] == slid_items[idx + 1]:
            slid_items[idx] *= 2
            slid_items[idx + 1] = 0            
    output_list = slide_items_left(slid_items)    
    return output_list

# testing merge function

# [2, 0, 2, 4] should return [4, 4, 0, 0]
# [0, 0, 2, 2] should return [4, 0, 0, 0]
# [2, 2, 0, 0] should return [4, 0, 0, 0]
# [2, 2, 2, 2] should return [4, 4, 0, 0]
# [8, 16, 16, 8] should return [8, 32, 8, 0]

#test = tsuite.TestSuite()
#
#input = [2, 0, 2, 4]
#expected = [4, 4, 0, 0]
#test.run_test(merge(input), expected, 'Testing merge')
#
#input = [0, 0, 2, 2]
#expected = [4, 0, 0, 0]
#test.run_test(merge(input), expected, 'Testing merge')
#
#input = [2, 2, 0, 0]
#expected = [4, 0, 0, 0]
#test.run_test(merge(input), expected, 'Testing merge')
#
#input = [2, 2, 2, 2]
#expected = [4, 4, 0, 0]
#test.run_test(merge(input), expected, 'Testing merge')
#
#input = [8, 16, 16, 8]
#expected = [8, 32, 8, 0]
#test.run_test(merge(input), expected, 'Testing merge')
#
#input = [4, 0, 0, 0]
#expected = [4, 0, 0, 0]
#test.run_test(merge(input), expected, 'Testing merge')
#
#input = [0, 0, 0, 0]
#expected = [0, 0, 0, 0]
#test.run_test(merge(input), expected, 'Testing merge')
#
#input = [0, 0, 0, 2]
#expected = [2, 0, 0, 0]
#test.run_test(merge(input), expected, 'Testing merge')
#
#test.report_results()

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height # no of rows
        self._width = grid_width # no of cols
#        self.grid = [[0 + 0 for col in range(self.width)]
#                            for row in range(self.height)]
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
#        self._grid = [[0 + 0 for dummy_col in range(self._width)]
#                           for dummy_row in range(self._height)]
        self._grid = [[0 for dummy_col in range(self._width)] for dummy_row in range(self._height)]

        self.new_tile()
        self.new_tile()
        

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # owltest expected a different format here
        grid_str = ''
        for row in range(self._height):
            grid_str += str(self._grid[row])
            grid_str += '\n'
        return grid_str
        
        # implementation 2
#        grid_str = '['
#        for row in range(self._height):
#            grid_str += str(self._grid[row])
#            if row == self._height - 1:
#                grid_str += ']'
#            else:
#                grid_str += '\n'
#        
#        return grid_str
    
        # implementation 3
#        a_str = ""
#        for row in range(self._height):
#            for col in range (self._width):
#                a_str += ( str(self.get_tile(row, col)) + " " )
#            a_str += '\n'
#        return a_str
    
        # implementation 4
#        str_val = ""
#        for row_grid in range(self._height):
#            str_val += "\n"+'_'.join(str(x) for x in self._grid[row_grid])
#        
#        return str_val

        # implmentation 5
        # replaced the initialization of _grid in reset()
#        return str(self._grid)


    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        starting_cell_index = {UP: (0, 0),
                               DOWN: (self._height - 1, 0),
                               LEFT: (0, 0),
                               RIGHT: (0, self._width - 1)}
        starting_cell = list(starting_cell_index[direction])
        if direction == UP or direction == DOWN:
            # process one col at a time
            for dummy_col in range(0, self._width):
                temp_list = []
                # extract tiles from one col into a list
                for dummy_row in range(0, self._height):                    
                    temp_list.append(self.get_tile(starting_cell[0], starting_cell[1]))
                    starting_cell[0] += OFFSETS[direction][0]
                    starting_cell[1] += OFFSETS[direction][1]
                merged_list = merge(temp_list)
                starting_cell[0] = starting_cell_index[direction][0]
                # replace each col with new merged tiles
                for new_tile in merged_list:
                    self.set_tile(starting_cell[0], starting_cell[1], new_tile)
                    starting_cell[0] += OFFSETS[direction][0]
                # adjust loop index to process next col
                starting_cell[0] = starting_cell_index[direction][0]
                starting_cell[1] += 1
        if direction == RIGHT or direction == LEFT:
            # process one row at a time
            for dummy_row in range(0, self._height):
                temp_list = []
                # extract tiles from one row into a list
                for dummy_col in range(0, self._width):
                    temp_list.append(self.get_tile(starting_cell[0], starting_cell[1]))
                    starting_cell[0] += OFFSETS[direction][0]
                    starting_cell[1] += OFFSETS[direction][1]
                merged_list = merge(temp_list)
                starting_cell[1] = starting_cell_index[direction][1]
                # replace each row with new merged tiles
                for new_tile in merged_list:
                    self.set_tile(starting_cell[0], starting_cell[1], new_tile)
                    starting_cell[1] += OFFSETS[direction][1]
                # adjust loop index to process next col
                starting_cell[1] = starting_cell_index[direction][1]
                starting_cell[0] += 1
        self.new_tile()
#        print self
#        print '\n'
        

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        
        # the following implementation possibly resulted in testing errors (long runtime)
#        num_of_new_tiles = 0
#        while num_of_new_tiles < 1:
#            new_tile_num = 0
#            rand_num = random.random()
#            if rand_num > 0.1:
#                new_tile_num = 2
#            else:
#                new_tile_num = 4
#            new_tile_row_index = random.randrange(0, self.height)
#            new_tile_col_index = random.randrange(0, self.width)
#            if self.grid[new_tile_row_index][new_tile_col_index] == 0:
#                self.grid[new_tile_row_index][new_tile_col_index] = new_tile_num
#                num_of_new_tiles += 1
        
        # implementation 2
#        new_tile_row_index = random.randrange(0, self.height)
#        new_tile_col_index = random.randrange(0, self.width)
#        
#        while self.get_tile(new_tile_row_index, new_tile_col_index) != 0:
#            new_tile_row_index = random.randrange(0, self.height)
#            new_tile_col_index = random.randrange(0, self.width)
#        
#        new_tile_num = 0
#        rand_num = random.random()
#        if rand_num > 0.1:
#            new_tile_num = 2
#        else:
#            new_tile_num = 4
#        self.set_tile(new_tile_row_index, new_tile_col_index, new_tile_num);

        # implementation 3
        check_zeroes_in_grid_flag = False
        for row in self._grid:
            for tile in row:
                if tile == 0:
                    check_zeroes_in_grid_flag = True
#        print check_zeroes_in_grid_flag
        if check_zeroes_in_grid_flag == True:
            new_tile_row_index = random.randrange(0, self._height)
            new_tile_col_index = random.randrange(0, self._width)

            while self.get_tile(new_tile_row_index, new_tile_col_index) != 0:
                new_tile_row_index = random.randrange(0, self._height)
                new_tile_col_index = random.randrange(0, self._width)

            new_tile_num = 0
            rand_num = random.random()
            if rand_num > 0.1:
                new_tile_num = 2
            else:
                new_tile_num = 4
            self.set_tile(new_tile_row_index, new_tile_col_index, new_tile_num);

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

# run the gui
#poc_2048_gui.run_gui(TwentyFortyEight(5, 4))

# testing the class
#Temp_class = TwentyFortyEight(5, 4)
#print Temp_class
#poc_2048_gui.run_gui(temp_class)
