f = open("colorfile", "a")
f.write("pink")
f.close()

f = open("colorfile" , "r")
print(f.read())
f.close()