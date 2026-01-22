with open("p8_this.txt") as f:
    content1 = f.read()

with open("p4_file.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("These files are same")

else:
    print("these files not are same")

