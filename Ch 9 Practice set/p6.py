with open("log.html") as f:
    content = f.read()

if("python" in content):
    print("Yes python in content")

else:
    print("No python is not in content")