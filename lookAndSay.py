from typing import List, Tuple


def parse(sequence)->List[Tuple[int, str]]:
    sequenceList = []
    count = 0
    curLetter = ""
    for l in sequence:
        if curLetter == "":
            curLetter = l
            count += 1
        elif l == curLetter:
            count += 1
        else:
            sequenceList.append((count, curLetter))
            count = 1
            curLetter = l
    return sequenceList


def write(initialSequence) -> str:
    result = ""
    sequenceList = parse(initialSequence)
    for rule in sequenceList:
        result += str(rule[0]) + rule[1]
    result += "X"
    print(result[:-1])
    return result


def lookAndSay(n) -> None:
    curSequence = "1X"
    print(curSequence[:-1])
    for i in range(n):
        curSequence = write(curSequence)


lookAndSay(10)