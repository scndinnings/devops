# A simple description of function and optional argument
def func_loop(counter=None):
    if counter == None:
        counter=5
    for i in range(counter):
        print(i)


func_loop(10)
print("\nSee difference when call is made without passing an argument\n")
func_loop()
