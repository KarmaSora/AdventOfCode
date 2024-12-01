def main():
    print("hello world")

    # Take the input
    data = ""
    with open("2024/task1List.txt", "r") as file:
        for line in file:
            data += line + " "
    file.close()

    allData = data.split()

    # Split the input into two lists
    rightList = []
    leftList = []
    for i in range(len(allData)):
        if i % 2 == 0:
            leftList.append(int(allData[i]))
        else:
            rightList.append(int(allData[i]))

    # Call the function and print the result
    total = getCalc(leftList, rightList)
    
    print(f"Total Distance: {total}")
    print(f"Total Distance P2: {getCalcP2(leftList, rightList)}")

def convertListToDict(lst):
    freq_dict = {}
    for value in lst:
        if value in freq_dict:
            freq_dict[value] += 1
        else:
            freq_dict[value] = 1
    return freq_dict

def getCalc(leftList, rightList):
    leftList.sort()
    rightList.sort()

    total = 0

    for i in range(len(leftList)):
        total += abs(leftList[i] - rightList[i])

    return total

def getCalcP2(leftList, rightList):
    # Sort both lists
    leftList.sort()
    rightList.sort()

    leftDict = convertListToDict(leftList)
    rightDict = convertListToDict(rightList)

    total = 0

    for value in leftDict.keys():
        if value in rightDict:
            total += value * rightDict[value]

    return total

if __name__ == "__main__":
    main()
