class dfa:
    def scan(self, types):
        state = "start"
        i=0
        while i < len(types):
            if state == "start":
                if types[i] == "repeat":
                    state = "inrepeat"
                else:
                    state = "error"
            elif state == "inrepeat":
                if types[i] == "ID":
                    state = "inid"
                elif types[i] == "until":
                    state = "inuntil"
                else:
                    state = "error"
            elif state == "inid":
                if types[i] == "assign":
                    state = "inassign"
                else:
                    state = "error"
            elif state == "inassign":
                if types[i] == "ID" or types[i] == "NUM":
                    state = "finishedassign"
                else:
                    state = "error"
            elif state == "finishedassign":
                if types[i] == ";":
                    state = "finishedstatement"
                else:
                    state = "error"
            elif state == "finishedstatement":
                if types[i] == "ID":
                    state = "inid"
                elif types[i] == "until":
                    state = "inuntil"
                else:
                    state = "error"
            elif state == "inuntil":
                if types[i] == "ID" or types[i] == "NUM":
                    state = "infirstoperand"
                else:
                    state = "error"
            elif state == "infirstoperand":
                if types[i] == "COMP":
                    state = "incomp"
                else:
                    state = "error"
            elif state == "incomp":
                if types[i] == "ID" or types[i] == "NUM":
                    state = "finished"
                else:
                    state = "error"
            else:  # if something comes up after the second operand in the until statement
                state = "error"
            i += 1

        if state != "finished":
            return "Rejected"
        return "Accepted"
