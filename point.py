class Point:

    def point(self, kor):
        koor = kor.split()
        kLength = len(koor[0])
        i = 0
        ress = []
        while i < kLength:
            x = ' '
            y = ' '
            if (koor[0][i] == ','):
                x = koor[0][i-1]
                y = koor[0][i+1]
                tmp = [x, y]
                ress.append(tmp)
            i += 1
        return ress
