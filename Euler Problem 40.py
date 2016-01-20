#an irrational decimal is created by concatenating every consecutive number from 1 onwards
#ie. 0.123456789101112, etc.
#if dn is the nth digit, find d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

dec = ""
counter = 1
while len(dec) < 1000000:
    dec = dec + str(counter)
    counter += 1

prod = int(dec[0]) * int(dec[9]) * int(dec[99]) * int(dec[999]) * int(dec[9999]) * int(dec[99999]) * int(dec[999999])
print prod