#lets see how handling error works

#lets try to open a file that is not present in the machine
try:
    f = open("xyz")
except:
    print("File not found!")