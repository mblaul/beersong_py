## author Matt Blaul
## 1/26/2018
## CSI 3370
def main():
    ninety_nine_bottles_of_beer()

def ninety_nine_bottles_of_beer():
    numbottles = 99

    for x in range(numbottles, 0, -1):
        if (x > 1):
            print(str(x) + " bottles of beer on the wall, " + str(x) + " bottles of beer")
            if(x-1 > 1):
                print("take	one	down, pass it around, " + str(x-1) + " bottles of beer on the wall.")
            else:
                print("take	one	down, pass it around, " + str(x-1) + " bottle of beer on the wall.")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer")
            print("take	one	down, pass it around, no more bottles of beer on the wall.")


main()

##DESIRED OUTPUT
# 2	bottles	of	beer	on	the	wall,	2	bottles	of	beer
# take	one	down,	pass	it	around,	1	bottle	of	beer	on	the	wall.
# 1	bottle	of	beer	on	the	wall,	1	bottle	of	beer
# take	one	down,	pass	it	around,	no	more	bottles	of	beer	on	the	wall.
