# This class implements a Sudoku grid.
#
class Grid:
	
	#
	# Initialize a 9x9 grid of numbers.
	#
	def __init__(self, grid = None):
		self.__G = np.zeros((9, 9), dtype = np.int8)
	
	#
	# Set the number in a position, specified by row and column number, to
	# a specific value.
	#
	def set_number(self, row, column, value):
		self.__G[row, column] = value
	
	#
	# Return the number assigned to a specific position, specified by row
	# and column number.
	#
	def get_number(self, row, column):
		return self.__G[row, column]
	
	#
	# Sets all entries in this grid to zero (unknown) state.
	#
	def clear(self):
		
		#
		# Iterate over the rows.
		#
		for row in range(9):
			
			#
			# Iterate over the columns.
			#
			for column in range(9):
				self.__G[row, column] = 0
	
	#
	# Set all values in the grid via a NumPy array.
