import  re
startList = ['e','o']
totalList = [startList,]

def addRanks(value):
    return ["e"+value,"o"+value]

def increaseRank(list):
    newList =[]
    for i in range(len(list)):
        newRanks = addRanks(list[i])
        newList.append(newRanks[0])
        newList.append(newRanks[1])
    return newList

def calculateMC(pattern):
    even = 0
    odd = 0
    constant = 0
    doubleOdd = False

    m = re.search('oo|(^o.*o+$)', pattern)
    if m != None:
        doubleOdd = True

    while len(pattern)>0:
        value = pattern[-1]
        pattern=pattern[:-1]
        #print(constant)
        if value == "e":

            #constant *= pow(2, even)
            even+=1
        else:
            if value == "o":
                constant*=3
                constant+=1*pow(2, even)
                odd+=1
            else:
                print("fail  "+value.__str__())
    #print(constant)
    #print(odd.__str__()+"  "+even.__str__())
    #if(constant!=0):
    #    print("r:"+(constant%(pow(2,even)- pow(3,odd))).__str__())

    return [pow(2,even)- pow(3,odd),constant, doubleOdd]




for i in range(25):
    lastIndex = totalList[len(totalList)-1]
    for i in range(len(lastIndex)):
        mc = calculateMC(lastIndex[i])
        if(not mc[2] and mc[0]>=0 and mc[1]%mc[0]==0):
            print(len(lastIndex).__str__() + "  "+lastIndex[i].__str__()
                  +" "
                  + mc.__str__()
                  +" "
                  +(mc[1]/mc[0]).__str__())

    totalList.append(increaseRank(lastIndex))
    #print(totalList)
