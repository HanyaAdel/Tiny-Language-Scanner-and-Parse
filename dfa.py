class dfa:
    def scan(self, types):
        state = "start"
        states=[]
        states.append(state)
        i=0
        while i < len(types):
            if state == "start":
                if types[i] == "repeat":
                    state = "inrepeat"
                    states.append(state)
                else:
                    state = "error"
                    states.append(state)
            elif state == "inrepeat":
                if types[i] == "ID":
                    state = "inid"
                    states.append(state)
                elif types[i]=="until":
                    state = "inuntil"
                    states.append(state)
                else:
                    state = "error"
                    states.append(state)
            elif state == "inid":
                if types[i] == "assign":
                    state = "inassign"
                    states.append(state)
                else:
                    state = "error"
                    states.append(state)
            elif state == "inassign":
                if types[i] == "ID" or types[i] == "NUM":
                    state = "finishedassign"
                    states.append(state)
                else:
                    state = "error"
                    states.append(state)
            elif state == "finishedassign":
                if types[i] == ";":
                    state = "finishedstatement"
                    states.append(state)
                else:
                    state = "error"
                    states.append(state)
            elif state == "finishedstatement":
                if types[i] == "ID":
                    state = "inid"
                    states.append(state)
                elif types[i] == "until":
                    state = "inuntil"
                    states.append(state)
                else:
                    state = "error"
                    states.append(state)
            elif state == "inuntil":
                if types[i] == "ID" or types[i] == "NUM":
                    state = "infirstoperand"
                    states.append(state)
                else:
                    state = "error"
                    states.append(state)
            elif state == "infirstoperand":
                if types[i] == "COMP":
                    state = "incomp"
                    states.append(state)
                else:
                    state = "error"
                    states.append(state)
            elif state == "incomp":
                if types[i] == "ID" or types[i] == "NUM":
                    state = "finished"
                    states.append(state)
                else:
                    state = "error"
                    states.append(state)
            else:  # if something comes up after the second operand in the until statement, or we are already in dead state
                state = "error"
                states.append(state)
            i += 1

        if state != "finished":
            return ("Rejected",states)
        return ("Accepted",states)