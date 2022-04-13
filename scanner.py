class Scanner:

    def scan(self, input_text):
        reserved_words = ('repeat', 'until')

        comparison_operators = ('=', '>', '<', '>=', '<=')
        comp = ('<', '>')

        white_spaces = ('\n', '\t', ' ')  # consider adding \0
        assignment = (':=')

        special_tokens = (';', '=')
        special_characters = ('<', '>', '=', ':', ";")
        tokens = []
        types = []

        i = 0
        state = "start"
        temp_token = ""
        while i < len(input_text):
            if input_text[i].isdigit() or input_text[i].isalpha() or input_text[i] in white_spaces or input_text[i] in special_characters:
                if state == "start":
                    if input_text[i] in white_spaces:
                        state = "start"
                    elif input_text[i].isalpha():
                        temp_token += input_text[i]
                        state = "inid"
                    elif input_text[i].isdigit():
                        temp_token += input_text[i]
                        state = "innum"
                    elif input_text[i] in comp:
                        temp_token += input_text[i]
                        state = "incomp"
                    elif input_text[i] == ':':
                        temp_token += input_text[i]
                        state = "inassign"
                    elif input_text[i] == "=":
                        temp_token += input_text[i]
                        state = "doneincr"
                    elif input_text[i] in special_tokens:
                        temp_token += input_text[i]
                        state = "doneincr"

                elif state == "inid":
                    if input_text[i].isdigit() or input_text[i].isalpha():
                        temp_token += input_text[i]
                        state = "inid"
                    else:
                        state = "done"
                elif state == "innum":
                    if input_text[i].isdigit():
                        temp_token += input_text[i]
                        state = "innum"
                    elif input_text[i].isalpha():
                        state = "error"
                    else:
                        state = "done"
                elif state == "inassign":
                    if input_text[i] == "=":
                        temp_token += input_text[i]
                        state = "doneincr"
                    else:
                        state = "error"
                elif state == "incomp":
                    if input_text[i] == "=":
                        temp_token += input_text[i]
                        state = "doneincr"
                    else:
                        state = "done"
            else:
                state = "error"
            if state == "error":
                print("syntax error")
                break
            if state != "done":
                i += 1
            if state == "done" or state == "doneincr":
                tokens.append(temp_token)
                temp_token = ""
                # i-=1
                state = "start"
        if (state == "inassign"):
            print("syntax error")
        elif (state != "start" and state != "doneincr"):
            tokens.append(temp_token)
        status = "Accepted"
        if state == "error":
            status = "Rejected"

        for i in tokens:
            if i in reserved_words:
                types.append(i)
            elif i in comparison_operators:
                types.append("COMP")
            elif i == ";":
                types.append(";")
            elif i.isdigit():
                types.append("NUM")
            elif i == ":=":
                types.append("assign")
            else:
                types.append("ID")
        return (status,tokens, types)
