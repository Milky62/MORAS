def _parse_macros(self):

    self._init_macro()
    self._wc = 0  # loop counter
    self._wl = []
    self.iter_lines(self._parse_macro)


def _parse_macro(self, line, p, o):
    l = line[1:].split(")")

    # ako line nije macro, samo vrati
    if line[0] != "$":
        return line


    elif line.split("(")[0] not in self._mac:
        self._flag = False
        self._line = o
        self._errm = "Macro nonexistent"
        return ""


    elif l[1] != "" or len(l) > 2:
        self._flag = False
        self._line = o
        self._errm = "Code after macro"
        return ""

    else:
        # $MV (A -> B)
        if line.split("(")[0] == self._mac[0]:
            l = line.split("(")[1].split(",")
            A = l[0]
            B = ""

            #parsiranje argumenta B
            for i in l[1]:
                if i.isdigit() or i.isalpha():
                    B += i

            return f"@{A}\nD=M\n@{B}\nM=D"

        # $SWP (A & B)
        elif line.split("(")[0] == self._mac[1]:
            l = line.split("(")[1].split(",")
            A = l[0]
            B = ""

            # parsiranje argumenta B
            for i in l[1]:
                if i.isdigit() or i.isalpha():
                    B += i


            return f"@{A}\nD=M\n@swp\nM=D\n@{B}\nD=M\n@{A}\nM=D\n@swp\nD=M\n@{B}\nM=D"

        # $ADD (A + B -> D)
        elif line.split("(")[0] == self._mac[2]:
            l = line.split("(")[1].split(",")
            A = l[0]
            B = ""
            D = ""

            #parsiranje arg B
            for i in l[1]:
                if i.isdigit() or i.isalpha():
                    B += i

            #parsiranje arg D
            for i in l[2]:
                if i.isdigit() or i.isalpha():
                    D += i

            return f"@{A}\nD=M\n@{D}\nM=D\n@{B}\nD=M\n@{D}\nM=D+M"

        # $WHILE
        elif line.split("(")[0] == self._mac[3]:
            l = line.split("(")
            n = ""

            # parsiranje argumenta
            for i in l[1]:
                if i.isdigit() or i.isalpha():
                    n += i

            #inkrementiranje loopa
            self._wc += 1
            self._wl.append(self._wc)


            return f"(WHILE{self._wc})\n@{n}\nD=M\n@END{self._wc}\nD;JEQ"

        # $END
        elif line.split("(")[0] == self._mac[4]:
            if not self._wl:
                self._flag = False
                self._line = o
                self._errm = "Unmatched $END macro"
                return ""

            #pop zadnjeg WHILE loop counter iz self._wl
            g = self._wl.pop()

            return f"@WHILE{g}\n0;JMP\n(END{g})"

        # ako nije prepoznati macro samo vrati line
        else:
            return line


def _init_macro(self):
    self._mac = ["$MV", "$SWP", "$ADD", "$WHILE", "$END"]
