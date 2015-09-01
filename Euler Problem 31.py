#Problem 31: In england there are 8 coins: 1p, 2p, 5p, 10p, 20p, 50p, 100p, and 200p
#How many different ways can you make 200p using different coins?

#the ones don't matter, since the ones can just make up the rest all the way up to 200
count = 1
for a in range(0, 3):
    for b in range(0, 5):
        for c in range(0, 11):
            for d in range(0, 21):
                for e in range(0, 41):
                    for f in range(0, 101):
                        if a*100 + b*50 + c*20 + d*10 + e*5 + f*2 > 200:
                            break
                        else:
                            count += 1

print count