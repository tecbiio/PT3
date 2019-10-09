import pprint
import Face

class RubbiksCube:

    def init_tab(self):
        tab = [[[ Face(0, "") for i in xrange(6)] for j in xrange(3)] for k in xrange(3)]
        pprint.pprint(tab)
        for i in range(0,6):
            for j in range(0,3):
                for k in range(0,3):
                    if (i==0):
                        tab[i][j][k] = Face(0,"Vert")
                    if (i==1):
                        tab[i][j][k] = Face(1,"Rouge")

r = RubbiksCube()
r.init_tab()
