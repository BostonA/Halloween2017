Table = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
Wait = []
done = False
def FindLoc (Num, Table):
    x = 0
    for s in Table:
        done = False
        if done:
            break
        x = x + 1
        y = 0
        for z in s:
            y = y + 1
            Pick = [x, y]
            if z == Num:
                print "Pick " + str(Num) + " at loc:", str(Pick)
                done = True
                if done:
                    break
        if done:
            break
        
    Table[Pick[0] - 1][Pick[1] - 1] = 0
    print Table
    return Table, Pick
    #Com.Numaral(Pick[0])
    #Com.Numaral(Pick[1])
while True:
    Inputs = raw_input(">>> ")
    #Table, PickLoc = FindLoc(1, Table)
    if Inputs == "1":
        Table, PickLoc = FindLoc(1, Table)
    elif Inputs == "2":
        Table, PickLoc = FindLoc(2, Table)
    elif Inputs == "3":
        Table, PickLoc = FindLoc(3, Table)
    elif Inputs == "4":
        Table, PickLoc = FindLoc(4, Table)
    print
    print Table
    print PickLoc
    