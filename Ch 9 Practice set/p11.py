with open("p8_this.txt") as f:
    content = f.read()

with open("p11_this.txt", "w") as f:
    f.write(content)