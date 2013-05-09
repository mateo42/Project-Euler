# Largest product of 4 adjacent numbers in a grid

class Product:
	def __init__( self, value ):
		self.value = value
		self.group = []

	def update( self, value, group ):
		if (value > self.value):
			self.value = value
			self.group = group

	def getValue( self ):
		return self.value

class Grid:
	def __init__( self, file ):
		self.grid = []
		f = open( file )
		self.rowCount = 0
		for line in f:
			self.grid.append( map( int, line.split() ) )
			self.rowCount += 1
		self.colCount = len( self.grid[0] )

	def get( self, x, y ):
		return self.grid[x][y]

	def display( self, group ):
		for r in range( self.rowCount ):
			for c in range( self.colCount ):
				if (r, c) in group:
					print( "\033[92m%02d\033[0m " % self.grid[r][c] ),
				else:
					print( "%02d " % self.grid[r][c] ),
			print( "\n" ),

def findLargestGrouping():
	grid  = Grid( 'problem011.txt' )
	largestProduct = Product( 0 )
	
	# Check horizontal groups
	for row in range( grid.rowCount ):
		for col in range( grid.colCount - 3 ):
			p = 1
			g = []
			for i in range( 4 ):
				p *= grid.get( row, col+i ) 
				g.append( (row, col+i) )

			largestProduct.update( p, g )

	# Check veritcle groups
	for col in range( grid.colCount ):
		for row in range ( grid.rowCount - 3 ):
			p = 1
			g = []
			for i in range( 4 ):
				p *= grid.get( row+i, col )
				g.append( (row+i, col) )
			largestProduct.update( p, g )

	# Check \ diagonal groups
	for row in range( grid.rowCount - 3 ):
		for col in range( grid.colCount - 3 ):
			p = 1
			g = []
			for i in range( 4 ):
				p *= grid.get( row+i, col+i )
				g.append( (row+i, col+i) )
			largestProduct.update( p, g )

	# Check / diagonal groups
	for row in range( grid.rowCount - 3 ):
		for col in range( 3, grid.colCount ):
			p = 1
			g = []
			for i in range( 4 ):
				p *= grid.get( row+i, col-i)
				g.append( (row+i, col-i) )
			largestProduct.update( p, g )

	grid.display( largestProduct.group )
	return largestProduct.getValue()

print findLargestGrouping()