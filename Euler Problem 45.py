#a triangle number follows the formula Tn = n(n+1)/2
#a pentagonal number follows the formula Pn = n(3n-1)/2
#a hexagonal number follows the formula Hn = n(2n-1)
#find the number after 40755 that is triangle, pentagonal, and hexagonal

def triangle(n):
    return n * (n + 1)/2

def pentagonal(n):
    return n * (3*n - 1) / 2

def hexagonal(n):
    return n * (2*n - 1)

tri = []
pen = []
hex = []
n = 286

while True:
    t = triangle(n)
    tri.append(t)
    pen.append(pentagonal(n-120))
    hex.append(hexagonal(n-142))
    if t in pen and t in hex:
        print t
        break
    else:
        n += 1