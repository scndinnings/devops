# A simple nested list example showing working of pass, continue and break
l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
#Created a nested list
l=[l1,l2,l3]
print(l)

for i in l:
    print("Sublist",i)
    if i==[4,5,6]:
        print("Continue will kick me out of the current iteration")
        continue
        print("Will I be printed?")
    elif i==[1,2,3]:
        print("See how pass works")
        pass
        print("Pass let me print myself")
    elif i==[7,8,9]:
        print("break will kick me out of loop")
        break
        print("break never lets me print")