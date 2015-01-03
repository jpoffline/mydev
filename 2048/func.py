def getloc(i, SP, S, M):
	return M + i * (SP + S)


# Function to return the ID of a tile, from the (i,j)-Cartesian location on the board
def getind(i, nx, j, ny):
    return i * ny + j
    
    
def GetRandomTileID(nt):
    return math.random.randint(0, nt-1)