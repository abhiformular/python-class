class student:
    def __init__(self,age):
        self.age = age

    def getpermit(self):
        if self.age < 13:
            raise Exception('You are not old enough.')
        else:
            print('you are old enough to get a permit.')


age = int(input('what is your age? '))

student1 = student(age)
try:
    student1.getpermit()
except Exception as e:
    print(f"ERROR {e}")
