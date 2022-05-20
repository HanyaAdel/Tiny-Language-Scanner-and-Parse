# (stmt-seq)' -> stmt-seq                           
# stmt-seq -> stmt-seq statement                        2
# stmt-seq -> statement                                 3
# statement -> repeat-stmt                              4
# statement ->  assign-stmt                             5
# repeat-stmt -> repeat stmt-seq until identifier       6
# assign-stmt -> identifier := factor ;                 7
# factor -> identifier                                  8
# factor -> number                                      9


##### DICTIONARY 1 #####

#1 ---> (stmt-seq)'
#2 ---> stmt-seq
#3 ---> stmt-seq 
#4 ---> statement
#5 ---> statement
#6 ---> repeat-stmt 
#7 ---> assign-stmt 
#8 ---> factor
#9 ---> factor


##### DICTIONARY 2 #####
#1 ---> stmt-seq
#2 ---> stmt-seq statement 
#3 ---> statement    
#4 ---> repeat-stmt   
#5 ---> assign-stmt 
#6 ---> repeat stmt-seq until identifier  
#7 ---> identifier := factor ;
#8 ---> identifier
#9 ---> number


import copy


parseTable = {
    0: {
        'repeat': 's5',
        'identifier': 's6',
        'stmt-seq': '1',
        'statement': '2',
        'repeat-stmt': '3',
        'assign-stmt': '4'
    },
    1: {
        'repeat': 's5',
        'identifier': 's6',
        '$': 'acc',
        'statement': '7',
        'repeat-stmt': '3',
        'assign-stmt': '4'
    },
    2: {
        'repeat': 'r3',
        'until': 'r3',
        'identifier': 'r3',
        '$': 'r3'
    },
    3: {
        'repeat': 'r4',
        'until': 'r4',
        'identifier': 'r4',
        '$': 'r4'
    },  
    4: {
        'repeat': 'r5',
        'until': 'r5',
        'identifier': 'r5',
        '$': 'r5'
    },  
    5: {
        'repeat': 's5',
        'identifier': 's6',
        'stmt-seq'  : '8',
        'statement': '2',
        'repeat-stmt': '3',
        'assign-stmt': '4'
    },      
    6: {
        ':=': 's9'
    },            
    7: {
        'repeat': 'r2',
        'until': 'r2',
        'identifier': 'r2',
        '$'  : 'r2'
    },
    8: {
        'repeat': 's5',
        'until': 's10',
        'identifier': 's6',
        'statement': '7',
        'repeat-stmt': '3',
        'assign-stmt': '4'
    }, 
    9: {
        'identifier': 's12',
        'number': 's13',
        'factor': '11',
    },                 
    10: {
        'identifier': 's14',
    },                      
    11: {
        ';': 's15',
    },             
    12: {
        ';': 'r8',
    },
    13: {
        ';': 'r9',
    },   
    14: {
        'repeat': 'r6',
        'until': 'r6',
        'identifier': 'r6',
        '$': 'r6',    
    },     
    15: {
        'repeat': 'r7',
        'until': 'r7',
        'identifier': 'r7',
        '$': 'r7',    
    },                                  
    
}


leftOp_dict = {
    1: "(stmt-seq)'",
    2: "stmt-seq",
    3: "stmt-seq",
    4: "statement",
    5: "statement",
    6: "repeat-stmt",
    7: "assign-stmt",
    8: "factor",
    9: "factor"
}


rightOp_dict = {
    1: ["stmt-seq"],
    2: ["stmt-seq", "statement"],
    3: ['statement'],
    4: ["repeat-stmt"],
    5: ["assign-stmt"],
    6: ["repeat", "stmt-seq", "until", "identifier"],
    7: ["identifier", ":=", "factor", ';'],
    8: ["identifier"],
    9: ["number"]
}

stack, symbols = [0], []

In = ["repeat", 
        "repeat", 
            "identifier", ":=", "number", ";",
            "identifier", ":=", "number", ";",
        'until', 'identifier', 
    'until', 'identifier', '$']


#In = ["identifier", ":=", "number", ";","$"]

stack_table = []
cnt =  1

def func():
    while len(In) > 0:

        
        global cnt
        temp = []
        temp.append(cnt)
        cnt +=1
        stackCpy = copy.deepcopy(stack)
        symbolCpy = copy.deepcopy(symbols)
        inCpy = copy.deepcopy(In)
        temp.append(stackCpy)
        temp.append(symbolCpy)
        temp.append(inCpy)



        currInput = In[0]
        
        lastElement = stack[-1]

        action = ""

        if currInput in parseTable[lastElement].keys():
            action = parseTable[lastElement][currInput]
        else:
            print("not accepted")
            break
        
        temp.append(action)

        stack_table.append(temp)

        if action == "acc":
            print("accepted")
            break

        
        elif action[0] == 's':
            In.pop(0)
            stack.append(int(action[1:]))
            symbols.append(currInput)
        

        elif action[0] == 'r':
            state = int(action[1:])
            seq = rightOp_dict[state]
            
            subList = symbols[-len(seq):]

            if (subList == seq):
                del symbols[-len(seq):]
                leftOp = leftOp_dict[state]
                symbols.append(leftOp)

                del stack[-len(seq):]
                lastElement = stack[-1]
                element = parseTable[lastElement][symbols[-1]]

                stack.append(int (element))
        
        else:
            print ("not accepted" )
            break

        #print(temp)

    for l in stack_table:
        print(l)


func()
        



