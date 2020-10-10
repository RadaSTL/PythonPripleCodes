myUniqueList = []
myLeftovers = []

def pushLeftover(val):
    myLeftovers.append(val);

def valuePush(val):

    try:
        myUniqueList.index(val)
        pushLeftover(val)
        return False
    except:
        myUniqueList.append(val)
        return True

valuePush("ASD")
valuePush("DFG")
valuePush("ABC")
print(myUniqueList)
valuePush("ASD")
valuePush("DFG")
print(myUniqueList)
print(myLeftovers)

