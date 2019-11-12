import grid
import point


class Player:
    def count(self, grids):
        ress = 0
        for i in range(len(grids)):
            for x in range(len(grids[i])):
                if grids[i][x] == 'X':
                    ress += 1
        return ress


# Main driver

# player 1
player1 = Player()
p1Matrix = grid.Grid()
p1Pointer = point.Point()

# for Player 2
player2 = Player()
p2Matrix = grid.Grid()
p2Pointer = point.Point()


sizeGrid = int(input())  # size of grids
sizeShip = int(input())  # size of ships

sKoorP1 = str(input())  # coordinat ship that will be placed
sKoorP2 = str(input())

siziMissils = int(input())  # size of missils
eKoor1 = str(input())  # coordinat that player x will be placed their missils
eKoor2 = str(input())

p1 = p1Matrix.marking(sizeGrid, sKoorP1, eKoor2)
p2 = p2Matrix.marking(sizeGrid, sKoorP2, eKoor1)

a = player1.count(p1)
b = player2.count(p2)

print('P1 attack:', a)
print('P2 attack:', b)

"""
contoh inputan, langsung copy saja
5
5
1,1:2,0:2,3:4,4:1,3
2,1:4,0:3,3:1,1:2,2
5
2,1:4,0:4,1:3,0:1,3
1,2:0,0:2,3:3,4:4,3
"""
