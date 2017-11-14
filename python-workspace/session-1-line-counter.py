# a simple line counter code for any text file
f=open("/home/yashok/run-docker-grav.sh")
st=f.read()
# making a list out of entire file string where each line is one element
print(len(st.split('\n'))-1)
f.close()