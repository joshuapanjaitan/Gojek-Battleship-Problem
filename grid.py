import point


class Grid:
    P = point.Point()

    def size(self, leng):  # generate the grids
        a = ' '
        M = []
        i = 0
        x = 0
        while i < leng:
            inside = []
            while x < leng:
                inside.append(a)
                x += 1
            x = 0
            M.append(inside)
            i += 1
        return M

    def marking(self, M, point, ePoint):  # marking all the coordinat
        matriks = self.size(M)
        koor = Grid.P.point(point)
        eKoor = Grid.P.point(ePoint)
        j = 0
        t = 0
        for i in range(len(matriks)):  # for the ship
            while j < len(koor):
                x = int(koor[j][0])
                y = int(koor[j][1])
                matriks[x][y] = 'S'
                j += 1

        for a in range(len(matriks)):  # for the missils
            while t < len(eKoor):
                x = int(eKoor[t][0])
                y = int(eKoor[t][1])
                enemy = matriks[x][y]
                if enemy == 'S':
                    matriks[x][y] = 'X'
                else:
                    matriks[x][y] = 'O'
                t += 1

        return matriks
