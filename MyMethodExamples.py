def welcomeToPython():
        print("My first method without inputs or outputs")

def welcomeWithInput(name):
        print(f"{name}'s first method without one inputs and no output")
        
def welcomeWithOutput():
        return "First method with output."


def welcome2Input1Output(name,grade):
        print(f"{name} is a {8}th grader and this I his first method with 2 input and 1 output.")
        return name,grade


welcomeToPython()
welcomeWithInput("Abhi")
messege = welcomeWithOutput()
print(messege)
welcome2Input1Output("Abhi","9")
messege2 = welcome2Input1Output("abhi","9")