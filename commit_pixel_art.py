import os

pixelArt = [[0, 0, 2, 2, 2, 0, 0],
			[0, 2, 2, 2, 2, 2, 0],
			[2, 0, 4, 2, 0, 4, 2],
			[2, 0, 4, 2, 0, 4, 2],
			[2, 2, 2, 2, 2, 2, 2],
			[2, 0, 2, 0, 2, 0, 2],
			[0, 0, 0, 0, 0, 0, 0]]

def colorToCommitNumber(color):
	return {
        0: 0,
        1: 1,
        2: 3,
        3: 7,
        4: 11
    }.get(color, 0)

days = 65

for y in range(0,7):
	for x in range(0,7):
		commitsCount = colorToCommitNumber(pixelArt[x][y])
		while commitsCount > 0:
			file = open("pixelart.txt", 'a')
			file.write("day " + str(days) + " --- [" + str(x) + ";" + str(y) + "] : " + str(pixelArt[x][y]) + " makes " + str(colorToCommitNumber(pixelArt[x][y])) + " commits, " + str(commitsCount) + " left\n")
			file.close()
			os.system("git add .")
			os.system("git commit --date=\"\'date --date=\'" + str(days) + " day ago''\" -am \"[" + str(x) + ";" + str(y) + "] : " + str(commitsCount) + "/" + str(colorToCommitNumber(pixelArt[x][y])) + "\"")
			commitsCount = commitsCount - 1
		days = days - 1

# os.system("git push")
