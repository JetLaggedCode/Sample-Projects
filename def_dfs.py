start = [problem.getStartState()]
    for item in start:
        Open=[item]
        Closed=[]
        Path=[]

    if problem.isGoalState(Open[0]) is True:
        return 
    else:
        count=0
        while Open:
            if count==0:
                visit=Open.pop()
            else:
                temp=Open.pop()
                visit=temp[0]

                Closed.append(visit)                            
                if problem.isGoalState(visit) is True:
                    return Path
                else:
                    Successors= problem.getSuccessors(visit)
                    for index in Successors:
                            if index[0] not in Closed :
                              Open.append((index[0],index[1]))
                print Open
                count=count+1
