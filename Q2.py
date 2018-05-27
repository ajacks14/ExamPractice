#     for x in slst:



def search (s, slst, size):
    for x in range(size):
        if s in slst[x]:
            return "Grade: " + slst[x][-2:]

    return "Student not in list"



ContinueToAsk = False
while not ContinueToAsk:
    name = input("enter a name : ")
    if name == "XXX":
        print("Good bye")
        ContinueToAsk = True
    else:
        print(search(name,["JBrown 42", "MBlack 55", "SPrunty 68", "LHughes 36"],4))

