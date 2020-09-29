class car:
  def __init__(self, model, make, type):
    self.model = model
    self.make = make
    self.type = type
car1 = car("John", 36, 1)
car2 = car("bob", 46, 1)
car3 = car("bill", 46, 0)

thislist = [car1, car2, car3]

for x in thislist:
    if x.type == 1:
        fuel =  'electric'
    elif x.type == 0:
        fuel = 'gas'
    print(f'the cars model is {x.model} the make cost {x.make} the fuel type is {fuel}')


