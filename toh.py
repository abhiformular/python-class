def drawPole():
    for x in range(1,5,1):
         print('     |')

def drawBase():
    print('-----------')

def drawTitle(name):
    print(f'     {name}')

def drawTower(title):
    drawPole()
    drawBase()
    drawTitle(title)

drawTower("A")
drawTower("B")
drawTower("C")