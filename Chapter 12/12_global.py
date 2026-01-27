a = 90

def sed():
    global a #gobal a lagne se sirf function ki a ki value count ki jaegi.Kyunki global function me laga hai
    a = 3
    print(a)

sed()
print(a)
#agar global a function me nhi lagta to 3 and 90 print hota.