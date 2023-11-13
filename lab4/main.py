import re

from Finite_Automata import Finite_Automata
from SymbolTable import SymbolTable

def get_reserved_words():
    words = []
    with open("reserved_words.in", "r") as file:
        for line in file:
            words.append(line.strip())

    return words

reserved_words = get_reserved_words()
PIF = []
identifier_table = SymbolTable(size=2)
constant_table = SymbolTable(size=2)
err = ""


def is_reserved_word(word):
    if word in reserved_words:
        return True
    return False


def is_identifier(word):
    fa = Finite_Automata("fainput_identifiers.in")
    return fa.check_validity(word)

def is_string(word):
    pattern = r'"[^"]*"'
    if re.match(pattern, word):
        return True
    else:
        return False

def is_integer(word):
    fa = Finite_Automata("fainput_constants.in")
    return fa.check_validity(word)

def is_separator(char):
    pattern = r"[ ,.!()]"
    if re.match(pattern, char):
        return True
    else:
        return False

def is_operator(char):
    pattern = r"[+-\/*]"
    if re.match(pattern, char):
        return True
    else:
        return False


def process_file(input_file, err=""):
    with open(input_file, "r") as file:
        current_word = ""
        row, column = 1, 1
        while True:
            char = file.read(1)

            if not char:
                break

            elif char == "\"":
                current_word += char
                char = file.read(1)
                current_word += char
                while char != "\"":
                    char = file.read(1)
                    current_word += char

            elif is_separator(char):
                if is_reserved_word(current_word):
                    if current_word == "Footnote":
                        while char != "\n":
                            char = file.read(1)
                    # print(current_word + " is reserved word")

                    else:
                        PIF.append((current_word, -1))

                elif is_identifier(current_word):
                    # print(current_word + " is identifier")
                    value_in_table, position = identifier_table.lookup(current_word)
                    if position is None:
                        identifier_table.insert(current_word, 0)
                        value_in_table, position = identifier_table.lookup(current_word)
                    PIF.append(("id", position))

                elif is_string(current_word):
                    # print(current_word + " is string")
                    value_in_table, position = constant_table.lookup(current_word)
                    if position is None:
                        constant_table.insert(current_word, 0)
                        value_in_table, position = constant_table.lookup(current_word)
                    PIF.append(("const", position))

                elif is_integer(current_word):
                    # print(current_word + " is integer")
                    value_in_table, position = constant_table.lookup(int(current_word))
                    if position is None:
                        constant_table.insert(int(current_word), 0)
                        value_in_table, position = constant_table.lookup(int(current_word))
                    PIF.append(("const", position))

                elif is_operator(current_word):
                    # print(current_word + " is integer")
                    PIF.append(('operator', -1))

                elif not current_word == "":
                    err += "Error with \'" + current_word + "\' at line " + str(row) + ", column " + str(column) + "\n"
                    # print("Not gud " + current_word)
                    pass

                # if not char.isspace():
                #     print(char + " is separator")
                current_word = ""

            else:
                if not char.isspace():
                    current_word += char

            if char == "\n":
                row += 1
                column = 1

            else:
                column += 1

    with open((input_file.split(".")[0] + "_PIF.out"), 'w') as file:
        for p in PIF:
            file.write(str(p) + "\n")

    with open((input_file.split(".")[0] + "_identifier_table.out"), 'w') as file:
        for i in identifier_table.table:
            file.write(str(i) + "\n")

    with open((input_file.split(".")[0] + "_constant_table.out"), 'w') as file:
        for c in constant_table.table:
            file.write(str(c) + "\n")

    # print(PIF)
    # print(identifier_table.table)
    # print(constant_table.table)
    if err == "":
        with open((input_file.split(".")[0] + "_error.out"), 'w') as file:
            file.write("No errors")
    else:
        with open((input_file.split(".")[0] + "_error.out"), 'w') as file:
            file.write(err)

process_file("p1.in")
process_file("p2.in")
process_file("p3.in")
process_file("p1error.in")
