import copy
import random
def ListRemove(l1 , l2):
    for item in l1:
        if item in l2:
            l2.remove(item)


def MaxInTable(t):
    maxt = t[0][0]
    pos = (0 , 0)
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] > maxt :
                maxt = t[i][j]
                pos = (i , j)
    return pos

def MinInTable(t):
    mint = t[0][0]
    pos = (0 , 0)
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] < mint :
                mint = t[i][j]
                pos = (i , j)
    return pos

def ABS(L):
    for i in range(len(L)):
        if L[i] < 0:
            L[i] = -L[i]

class Node:
    def __init__(self, value, color , numDomain , colorDomain ,nflag = False,cflag=False ):
        self.value = value
        self.color = color
        self.numDomain = numDomain
        self.colorDomain = colorDomain
        self.cflag = cflag
        self.nflag = nflag
    def Color(self):
        return self.color
    def Value(self):
        return self.value
    def NumericalDomain(self):
        return copy.deepcopy(self.numDomain)
    def ColorDomain(self):
        return copy.deepcopy(self.colorDomain)
    def SetNdomain(self , d):
        self.numDomain = d
    def SetCdomain(self , d):
        self.colorDomain = d
    def SetColor(self , c):
        self.color = c
    def SetValue(self , n):
        self.value = n



def ParSer(s):
    c = s[len(s)-1]
    if s[0:len(s)-1] == '*':
        n = s[0:len(s)-1]
    else:
        n = int(s[0:len(s)-1])
    return n , c


class sudoku:

    def __init__(self , n , m):
        self.n = n
        self.m = m
        self.colors = ['' for i in range(self.m)]
        self.table = [[Node(0 , '' , [] , []) for j in range(self.n)] for i in range(self.n)]
        self.checked = []
    def SetColors(self):
        inp = input('Please Enter the colors : ')
        inp = inp.split()
        for i in range(self.m):
            self.colors[i]  = inp[i]

    def GetColors(self):
        return copy.deepcopy(self.colors)

    def SetTable(self):
        for i1 in range(self.n):
            print('Pleas Enter statment of ',i1+1,'th place')
            inp = input()
            linei = inp.split()
            for i2 in range(self.n):
                n,c = ParSer(linei[i2])
                if n != '*':
                    self.table[i1][i2].nflag = True
                if c != '#':
                    self.table[i1][i2].cflag = True
                self.table[i1][i2].SetValue(n)
                self.table[i1][i2].SetColor(c)

    def PrintTable(self , wc = 0):
        for i1 in range(self.n):
            for i2 in range(self.n):
                node = self.table[i1][i2]
                if wc == 0 :
                        print(colordict[node.Color()] ,node.Value() ,  end = '\t')
                else:
                    print(node.Value(),node.Color() , sep = '' ,  end = '\t')
            print('\n')
        print(colordict['#'] , '\n')

    def SetInitialDomain(self):
        nd = [k+1 for k in range(self.n)]
        cd = copy.deepcopy(self.colors)
        for i1 in range(self.n):
            for i2 in range(self.n):
                node = self.table[i1][i2]
                if node.Value() == '*':
                    node.SetNdomain(copy.deepcopy(nd))
                else:
                    node.SetNdomain('None')
                if node.Color() == '#':
                    node.SetCdomain(copy.deepcopy(cd))
                else:
                    node.SetCdomain('None')

    def PrintDomain(self , allnodes = 0):
        if not allnodes:
            for i1 in range(self.n):
                for i2 in range(self.n):
                    node = self.table[i1][i2]
                    print(node.Value() , node.Color() , sep='' , end = ' :')
                    print(node.NumericalDomain() ,  node.ColorDomain()  , sep =' ' , end = '\t ')
                print('\n')
        else :
            i1 = allnodes[0]
            i2 = allnodes[1]
            node = self.table[i1][i2]
            print(node.Value() , node.Color() , sep='' , end = ' :')
            print(node.NumericalDomain() ,  node.ColorDomain()  , sep =' ')



    def NumCheck(self):

        for i in range(self.n):
            for j in range(self.n):


                if self.table[i][j].Value() == '*':
                    for num in self.table[i][j].numDomain:
                        if not self.SafeLocatiorforNumbering(i , j , num):
                            self.table[i][j].numDomain.remove(num)


                if self.table[i][j].Color()=='#':
                    for c1 in self.table[i][j].colorDomain:
                        if not self.SafeLocatiorforColoring(i , j , c1):
                            self.table[i][j].colorDomain.remove(c1)








    def ColorCheck(self):

        for i in range(self.n):
            for j in range(self.n):


                if self.table[i][j].Value() == '*':
                    for num in self.table[i][j].numDomain:
                        if not self.SafeLocatiorforNumbering(i , j , num):
                            self.table[i][j].numDomain.remove(num)



                if self.table[i][j].Color()=='#':
                    for c1 in self.table[i][j].colorDomain:
                        if not self.SafeLocatiorforColoring(i , j , c1):
                            self.table[i][j].colorDomain.remove(c1)




    def EmptyDomains(self):
        for i in range(self.n):
            for j in range(self.n):
                if len(self.table[i][j].NumericalDomain())==0 or len(self.table[i][j].ColorDomain()) ==0:
                   # print('There is no Solution ! ')
                    return True
        return False


    def Only1Choice(self):
        sn = False
        sc = False
        for i in range(self.n):
            for j in range(self.n):
                if len(self.table[i][j].NumericalDomain())==1:
                    self.table[i][j].SetValue(self.table[i][j].numDomain.pop())
                    self.table[i][j].SetNdomain('None')
                    sn = True
        for i in range(self.n):
            for j in range(self.n):
                if len(self.table[i][j].ColorDomain())==1:
                    self.table[i][j].SetColor(self.table[i][j].colorDomain.pop())
                    self.table[i][j].SetCdomain('None')
                    sc = True

        whole = sn or sc
        return whole

    def Degree(self, allnode = 0):
        if not allnode:
            d = [[-(self.n *self.n *self.m) for k1 in range(self.n)] for k2 in range(self.n)]
            for i in range(self.n):
                for j in range(self.n):
                    if self.table[i][j].Color() == '#':
                        if i-1>=0:
                            if self.table[i-1][j].Color() == '#':
                                d[i][j] = d[i][j] + 1
                        if i+1<self.n:
                            if self.table[i+1][j].Color() == '#':
                                d[i][j] = d[i][j] + 1
                        if j-1>=0:
                            if self.table[i][j-1].Color() == '#':
                                d[i][j] = d[i][j] + 1
                        if j+1>self.n:
                            if self.table[i][j+1].Color() == '#':
                                d[i][j] = d[i][j] + 1
        else:
            i = allnode[0]
            j = allnode[1]
            d= 0
            if self.table[i][j].Color() == '#':
                if i-1>=0:
                    if self.table[i-1][j].Color() == '#':
                        d = d+ 1
                if i+1<self.n:
                    if self.table[i+1][j].Color() == '#':
                        d = d + 1
                if j-1>=0:
                    if self.table[i][j-1].Color() == '#':
                        d = d + 1
                if j+1>self.n:
                    if self.table[i][j+1].Color() == '#':
                        d = d + 1
        return d

    def AllSatisfied(self):

        for i in range(self.n):
            for j in range(self.n):
                if self.table[i][j].Value()=='*':
                    return False
                if self.table[i][j].Color()=='#':
                    return False
        return True

    def MRV(self , allnode = 0):
        if not allnode:
            total = [[0 for k1 in range(self.n)] for k2 in range(self.n)]
            mrn = [[0 for k1 in range(self.n)] for k2 in range(self.n)]
            mrc = [[0 for k1 in range(self.n)] for k2 in range(self.n)]
            for i in range(self.n):
                for j in range(self.n):
                    if self.table[i][j].Value() == '*':
                        mrn[i][j] = len(self.table[i][j].NumericalDomain())
                    else:
                         mrn[i][j] = self.n * self.n

                    if self.table[i][j].Color() == '#':
                        mrc[i][j] = len(self.table[i][j].ColorDomain())
                    else:
                        mrc[i][j] = self.m * self.m
                    total[i][j] = (mrc[i][j]+ mrn[i][j])
        else:
            i = allnode[0]
            j = allnode[1]
            mrn = len(self.table[i][j].NumericalDomain())
            mrc = len(self.table[i][j].ColorDomain())
            total = mrn+mrc

        return total

    def Coloring(self , i , j , c = 0):
        if self.table[i][j].Value() != '*' and self.table[i][j].Color() == '#':
            up = 0
            down = 0
            right = 0
            left = 0
            direction = []
            if i-1>=0:
                if self.table[i-1][j].Value() != '*':
                    left = self.table[i-1][j].Value() ,self.table[i-1][j].Color()

            if i+1<self.n:
                if self.table[i+1][j].Value() != '*':
                    right =self.table[i+1][j].Value(), self.table[i-1][j].Color()


            if j-1>=0:
                if self.table[i][j - 1].Value() != '*':
                    up =self.table[i][j - 1].Value(), self.table[i][j-1].Color()
            if j+1<self.n:
                if self.table[i][j+1].Value() != '*':
                    down = self.table[i][j+1].Value() ,self.table[i][j+1].Color()
            if up:
                direction.append(up)
            if down:
                direction.append(down)
            if right :
                direction.append(right)
            if left:
                direction.append(left)
            if len(direction)>0:
                minim = 0
                maxim = 0
                d2 = copy.deepcopy(direction)
                while len(direction):
                    if max(direction)[0] > self.table[i][j].Value() :
                        maxim = max(direction)
                        direction.remove(max(direction))
                    else:
                        break


                while len(d2):
                    if min(d2)[0] < self.table[i][j].Value() :
                        minim = min(d2)
                        d2.remove(min(d2))
                    else:
                        break


                clr = copy.deepcopy(self.GetColors())
                if minim :
                    while minim[1] in clr:
                        clr.pop()
                if maxim:
                    while maxim[1] in clr:
                        clr.pop(0)
                lastc = []
                for c in clr:
                    if c in self.table[i][j].ColorDomain():
                        lastc.append(c)
                self.table[i][j].SetCdomain(lastc)
                if c==1 :
                    for k in range(len(lastc)):
                        if self.SafeLocatiorforColoring(i , j ,lastc[i] ):
                            self.table[i][j].SetCdomain('None')
                            self.table[i][j].SetColor(lastc[i])

    def ColorAll(self):
        for i in range(self.n):
            for j in range(self.n):
                self.Coloring(i , j)


    def SafeLocatiorforColoring(self , i , j , c):
        if i-1>=0:
            if self.table[i-1][j].Color() == c:
                return False
            if self.table[i-1][j].Value() != '*' and self.table[i][j].Value() != '*' and self.table[i-1][j].Color() != '#' :
                if self.table[i-1][j].Value() > self.table[i][j].Value():
                    if self.GetColors().index(self.table[i-1][j].Color()) > self.GetColors().index(c):
                        return False
                else:
                    if self.GetColors().index(self.table[i-1][j].Color()) < self.GetColors().index(c):
                        return False
        if i+1<self.n:
            if self.table[i+1][j].Color() == c:
                return False
            if self.table[i+1][j].Value() != '*' and self.table[i][j].Value() != '*' and self.table[i+1][j].Color() != '#' :
                if self.table[i+1][j].Value() > self.table[i][j].Value():
                    if self.GetColors().index(self.table[i+1][j].Color()) > self.GetColors().index(c):
                        return False
                else:
                    if self.GetColors().index(self.table[i+1][j].Color()) < self.GetColors().index(c):
                        return False


        if j-1>=0:
            if self.table[i][j - 1].Color() == c:
                return False
            if self.table[i][j-1].Value() != '*' and self.table[i][j].Value() != '*' and self.table[i][j-1].Color() != '#' :
                if self.table[i][j-1].Value() > self.table[i][j].Value():
                    if self.GetColors().index(self.table[i][j-1].Color()) > self.GetColors().index(c):
                        return False
                else:
                    if self.GetColors().index(self.table[i][j-1].Color()) < self.GetColors().index(c):
                        return False




        if j+1<self.n:
            if self.table[i][j + 1].Color() == c:
                return False

            if self.table[i][j+1].Value() != '*' and self.table[i][j].Value() != '*' and self.table[i][j+1].Color() != '#' :
                if self.table[i][j+1].Value() > self.table[i][j].Value():
                    if self.GetColors().index(self.table[i][j+1].Color()) > self.GetColors().index(c):
                        return False
                else:
                    if self.GetColors().index(self.table[i][j+1].Color()) < self.GetColors().index(c):
                        return False

        return True


    def BusyRow(self , row , num):
        for i in range(self.n):
            if(self.table[row][i].Value() == num):
                return True
        return False
    def BusyColumn(self, col, num):
        for i in range(self.n):
            if(self.table[i][col].Value() == num):
                return True
        return False
    def SafeLocatiorforNumbering(self , i , j , num):
        if self.table[i][j].Color() == '#':
            return not self.BusyRow( i , num) and not self.BusyColumn(j , num)
        else:
            self.table[i][j].SetValue(num)
            cn = self.SafeLocatiorforColoring(i , j , self.table[i][j].Color())
            self.table[i][j].SetValue('*')
            return not self.BusyRow( i , num) and not self.BusyColumn(j , num) and cn

    def UniqueRow(self , row):
        helplist = [0 for i in range(self.n)]
        for i in range(self.n):
            helplist[i] = self.table[row][i].Value()
        for i in range(self.n):
            if helplist[i] != '*':
                if helplist[i] in helplist[0:i]+helplist[i+1 : self.n+1]:
                    return False
        return True
    def UniqueColumn(self , col):
        helplist = [0 for i in range(self.n)]
        for i in range(self.n):
            helplist[i] = self.table[i][col].Value()
        for i in range(self.n):
            if helplist[i] != '*':
                if helplist[i] in helplist[0:i]+helplist[i+1 : self.n+1]:
                    return False
        return True

    def UniqueCellNumber(self , row , col):
        return self.UniqueColumn(col) and self.UniqueRow(row)

    def UniqueCellColor(self , i , j):
        helplist = [self.table[i][j].Color()]
        if i-1>=0:
            helplist.append(self.table[i-1][j].Color())
        if i+1<self.n:
            helplist.append(self.table[i+1][j].Color())
        if j-1>=0:
            helplist.append(self.table[i][j - 1].Color())
        if j+1<self.n:
            helplist.append(self.table[i][j + 1].Color())
        length = len(helplist)
        for k in range(length):
            if helplist[k] != '#':
                if helplist[k] in helplist[0:k]+helplist[k+1:length+1]:
                    return False
        return True


    def Contradiction(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.table[i][j].Color() != '#':
                    if not self.SafeLocatiorforColoring(i , j , self.table[i][j].Color()):
                        return True
                if self.table[i][j].Value() != '*':
                    num = self.table[i][j].Value()
                    self.table[i][j].SetValue('*')
                    if not self.SafeLocatiorforNumbering(i , j , num):
                        self.table[i][j].SetValue(num)
                        return True
                    self.table[i][j].SetValue(num)
                if self.table[i][j].Color() != '#' and self.table[i][j].Value() != '*':
                    c = self.SafeLocatiorforColoring(i , j , self.table[i][j].Color())
                    num = self.table[i][j].Value()
                    self.table[i][j].SetValue('*')
                    v = self.SafeLocatiorforNumbering(i , j , num)
                    self.table[i][j].SetValue(num)
                    if not c or not v:
                        return True

        return False

colordict = {
    'g':'\033[42m' ,
    'y' : '\033[43m',
    'r' : '\033[41m',
    'p':'\033[45m',
    'c':'\033[46m',
    'b' :'\033[0;30;44m',
    'bold':'\033[01m',
    '#':'\033[0m'
}


def AllMin(t):
    m1 , m2 = MinInTable(t)
    m = t[m1][m2]
    mins = []
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] == m:
                mins.append((i, j))
    return mins

def AllMax(t):
    m1 , m2 = MaxInTable(t)
    m = t[m1][m2]
    maxs = []
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] == m:
                maxs.append((i, j))
    return maxs


def Choose(s ,mains):
    mrv = s.MRV()
    deg = s.Degree()
    if len(mains.checked) > 0:
        for loc in mains.checked:
            l1 = loc[0]
            l2 = loc[1]
            mrv[l1][l2] = mrv[l1][l2] + 1
            deg[l1][l2] = deg[l1][l2] - 1
    pmrv = AllMin(mrv)
    pdeg = AllMax(deg)


    if len(pmrv) == 1:
        c1 , c2 =  pmrv[0]
        mains.checked.append((c1,c2))
        return c1 , c2
    if len(pdeg) == 1:
        c1 , c2 =  pdeg[0]
        mains.checked.append((c1,c2))
        return c1 , c2
    if len(pmrv) > 0:
        if len(pdeg) > 0:
            for a ,b in pmrv :
                if (a ,b) in pdeg :
                    c1 , c2 =  a, b
                    mains.checked.append((c1,c2))
                    return c1 , c2
        else:
            if len(pdeg) > 0 :
                a, b = pdeg[0]
                c1 , c2 =  a, b
                mains.checked.append((c1,c2))
                return c1 , c2


    c1 , c2 = random.choice(pdeg + pmrv)
    mains.checked.append((c1,c2))
    return c1 , c2



def Select(s , c1, c2):
    if s.table[c1][c2].Value() == '*' and s.table[c1][c2].Color() == '#' :
        #print('changing value and color')
        numbers = copy.deepcopy(s.table[c1][c2].NumericalDomain())
        clrs = copy.deepcopy(s.table[c1][c2].ColorDomain())
        clrs.reverse()
        cond = True
       # while cond:
        for num in numbers:
            for clr in clrs :
               # print('checking : ' , num , clr)
                nc = s.SafeLocatiorforNumbering(c1 , c2 , num)
                s.table[c1][c2].SetValue(num)
                cc = s.SafeLocatiorforColoring(c1 ,c2 , clr)
           # num = random.choice(numbers)
            #clr = random.choice(clrs)
                   # if s.SafeLocatiorforNumbering(c1 , c2 , num) and s.SafeLocatiorforColoring(c1 ,c2 , clr):
                  #  s.table[c1][c2].SetValue(num)
                   # s.table[c1][c2].SetColor(clr)
                if nc and cc:
                 #   print('they are ok')
                    s.table[c1][c2].SetColor(clr)
                    s.table[c1][c2].SetNdomain('None')
                    s.table[c1][c2].SetCdomain('None')
                    cond = False
                    return True
                else:
                  #  print('try others')
                    s.table[c1][c2].SetValue('*')
                    s.table[c1][c2].SetColor('#')
    if s.table[c1][c2].Value() == '*' and s.table[c1][c2].Color() != '#':
        #print('chaning value')
        cond = True
        numbers = copy.deepcopy(s.table[c1][c2].NumericalDomain())
        #while cond:
        for num in numbers:
       #     num = random.choice(numbers)
            if s.SafeLocatiorforNumbering(c1 , c2 , num):
                s.table[c1][c2].SetValue(num)
               # if not s.Contradiction():
                s.table[c1][c2].SetNdomain('None')
                cond = False
                return True



    if s.table[c1][c2].Value() != '*' and s.table[c1][c2].Color() == '#':
       # print('changing color')
        clrs = copy.deepcopy(s.table[c1][c2].ColorDomain())
        clrs.reverse()
        cond = True
        #while cond:
        for clr in clrs:
            #clr = random.choice(clrs)
            if s.SafeLocatiorforColoring(c1 ,c2 , clr):
                s.table[c1][c2].SetColor(clr)
               # if not s.Contradiction():
                s.table[c1][c2].SetCdomain('None')
                cond = False
                return True


    return False





def OneChoice(s):
    step = 0
    while s.Only1Choice():
        s.NumCheck()
        s.ColorCheck()
       # s.ColorAll()
        step = step + 1
    s.NumCheck()
    s.ColorCheck()
    #s.ColorAll()


def UpdateColor(s):
    for i in range(s.n):
        for j in range(s.n):
            if s.table[i][j].Color() != '#' and not s.table[i][j].cflag:
                if s.table[i][j].Value() != '*' and not s.table[i][j].nflag:
                    if not s.SafeLocatiorforColoring(i , j , s.table[i][j].Color()):
                        s.table[i][j].SetColor('#')
                        s.table[i][j].SetCdomain(copy.deepcopy(s.GetColors()))
                        s.ColorCheck()
                        s.table[i][j].SetValue('*')
                        s.table[i][j].SetNdomain([k+1 for k in range(s.n)])
def UpdateNumber(s):
    for i in range(s.n):
        for j in range(s.n):
            if s.table[i][j].Value() != '*' and not s.table[i][j].nflag:
                vs =  s.table[i][j].Value()
                s.table[i][j].SetValue('*')
                if not s.SafeLocatiorforNumbering(i , j , vs):
                   # print('i , j : ' , i, j , s.table[i][j].Value())
                    s.table[i][j].SetValue('*')
                    s.table[i][j].SetNdomain([k+1 for k in range(s.n)])
                    s.NumCheck()
                    s.table[i][j].SetColor('#')
                    s.table[i][j].SetCdomain(copy.deepcopy(s.GetColors()))
                    s.ColorCheck()
                else :
                    s.table[i][j].SetValue(vs)


def BackTrack(s ,mains):
    s.SetInitialDomain()
    mains.SetInitialDomain()
    s.NumCheck()
    s.ColorCheck()
    #s.ColorAll()
    mains.NumCheck()
    mains.ColorCheck()

    #mains.ColorAll()
    step = 0
    c1o = 0
    c2o = 0

    OneChoice(s)
    c1o , c2o = Choose(s , mains)
    c1 = c1o
    c2 = c2o
    while not s.Contradiction() and  not s.EmptyDomains() and not s.AllSatisfied():
        step = step +1
        OneChoice(s)
        #print('chosen : ' ,c1 , c2)
        val = False
        col = False
        if s.table[c1][c2].Value()=='*':
            val = True
            #print('editing Value')
        if s.table[c1][c2].Color() =='#':
            #print('editing Color')
            col = True
        rs = Select(s , c1 , c2)
        if rs :
            #print('Changed Table')
            #s.PrintTable()
            s.ColorCheck()
            s.NumCheck()
            if s.EmptyDomains() or s.Contradiction():
               # print('BackTrack' , c1 , c2)
               # s.PrintTable()
                if val:
                    s.table[c1][c2].SetValue('*')
                if col:
                    s.table[c1][c2].SetColor('#')
                s.SetInitialDomain()
                s.ColorCheck()
                s.NumCheck()
                c1o = c1
                c2o = c2
                #s.ColorAll()

          #  s.ColorCheck()
           # s.NumCheck()
            #s.ColorAll()
        else:
            if not s.table[c1o][c2o].cflag :
                s.table[c1][c2].SetColor('#')
            if not s.table[c1o][c2o].nflag:
                s.table[c1][c2].SetValue('*')
                s.SetInitialDomain()
                s.ColorCheck()
                s.NumCheck()



       # OneChoice(s)
        c1 , c2 = Choose(s , mains)




    if s.AllSatisfied():
        return True
    else:
        return False


def BackTrackSearch(mains  , lim = 0):
    if mains.Contradiction():
        print('Contradiction')
        return mains
    shat =sudoku(mains.n , mains.m)
    shat.table = copy.deepcopy(mains.table)
    shat.colors = copy.deepcopy(mains.GetColors())
    result = False
    if lim == 0:
        while not result:
            result = BackTrack(shat,mains)
           # shat.PrintTable()
            if result :
                break
            shat =sudoku(mains.n , mains.m)
            shat.table = copy.deepcopy(mains.table)
            shat.colors = copy.deepcopy(mains.GetColors())
    else:
        while lim > 0:
            result = BackTrack(shat,mains)
           # shat.PrintTable()
            lim = lim - 1
            if lim <  1:
                return shat
            if result :
                break
            shat =sudoku(mains.n , mains.m)
            shat.table = copy.deepcopy(mains.table)
            shat.colors = copy.deepcopy(mains.GetColors())


    return shat









#----------main --------


print('Please Enter number of colors  and size of table')
print('for example, enter 2, 3 for a sudoku with 2 colors which contains 1, 2, 3 ')
mn = input()
lmn = mn.split()
m = int(lmn[0])
n = int(lmn[1])
s = sudoku(n, m)
s.SetColors()
s.SetTable()
s.SetInitialDomain()
print('Which format do you prefer to see the table ? ')
print('1 - valuecolor like 1g')
print('2 - value with color at background like',end = ' ')
print(colordict['g'] , 1)
print( colordict['#'] ,'\n' )
p = int(input('Enter 1 or 2 : '))
if p == 2:
    p = 0

print('This is the input table : ')
s.PrintTable(p)
print('Do you want to set a limit for search ? Enter 0 for no limit and Enter other numbers for setting a limit')
lim = int(input('Enter the limit please : '))
r = BackTrackSearch(s, lim)
r.PrintTable(p)
