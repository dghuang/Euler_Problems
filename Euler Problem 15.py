#Find number of lattice paths in a 20 by 20 Grid
#this is essentially a Pascal triangle

def lattice_paths(length):
    lattice = [[1 for x in range(length+1)] for x in range(length+1)]
    for x in range(1,length+1):
        for y in range(1,length+1):
            lattice[x][y] = lattice[x-1][y] + lattice[x][y-1]
    return lattice[length][length]

print lattice_paths(20)