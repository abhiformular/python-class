class Tower:
    def drawPole(self):
        for x in range(1,5,1):
            print('    |')

    def drawBase(self):
        print('---------')

    def drawTitle(self,title):
       print(f'     {title}')
       
       
    def draw(self, title):   
        self.drawPole()
        self.drawBase()
        self.drawTitle(title)

towerA = Tower()
towerA.draw('Tower-A')

towerB = Tower()
towerB.draw('Tower-B')

towerC = Tower()
towerC.draw('Tower-C')


