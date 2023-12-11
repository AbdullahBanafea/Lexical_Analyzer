import keyword  # importing a library of keywords

operators = ['+', '-', '*', '/', '%', '**', '//'
    , '=', '+=', '-=', '/=', '%=', '//=', '**='
    , '&=', '|=', '^=', '>>=', '<<=', '==', '!='
    , '>', '<', '>=', '<=', '&', '|', '^', '~', '<<', '>>']
punctuators = ['{', '}', '[', ']', '(', ')', ',', ':', '#', '.']


def lex_num(code):  # a method that takes the given characters and add it in a variable then check if it is a digit
    # or return it to lex_id method then return the variables
    num = ''
    for c in code:
        if c.isdigit() or c.isalpha():
            num += c
        else:
            break

    if num.isdigit():
        return int(num), "Digit", len(num)
    else:
        return num, "Invalid ID", len(num)


def lex_id(code):  # a method that takes the given characters and
    # add it in a variable then check if it is an ID or a Keyword or Invalid ID then return the variables

    id = ''
    for c in code:
        if c.isdigit() or c.isalpha() or c == '_':
            id += c
        else:
            break

    if keyword.iskeyword(id):
        return id, "keyword", len(id)
    elif id.isalpha() or '_':
        return id, 'ID', len(id)


def lex_op(code):  # a method that takes the given characters and
    # add it in a variable then check if it is a Operator or not method then return the variables
    operators = {'+': 'Addition', '-': 'Subtraction', '*': 'Multiplication', '/': 'Division'
        , '%': 'Modulus', '**': 'Exponentiation', '//': 'Floor division', '=': 'Assignment'
        , '+=': 'Addition Assignment', '-=': 'Subtraction Assignment', '/=': 'Division Assignment'
        , '%=': 'Remainder Assignment', '//=': 'Floor division Assignment', '**=': 'Exponent Assignment'
        , '&=': 'Bitwise AND', '|=': 'Bitwise OR', '^=': 'Bitwise XOR', '>>=': 'Bitwise Right shift'
        , '<<=': 'Bitwise Left shift', '==': 'Equal To', '!=': 'Not Equal To', '>': 'Greater Than'
        , '<': 'Less Than', '>=': 'Greater Than or Equal To', '<=': 'Less Than or Equal To'
        , '&': 'Bitwise AND', '|': 'Bitwise OR', '^': 'Bitwise XOR', '~': 'Bitwise NOT'
        , '<<': 'Bitwise Left shift', '>>': 'Bitwise Right shift'}
    o = ''
    op = ''
    for c in code:
        if c in operators:
            op += c
        else:
            break

    if op in operators:
        o = operators[op]
        return op, o + ' Operator', len(op)
    else:
        return op, 'Invalid Operator', len(op)


def lex_pun(
        code):  # a method that takes the given character and check if it is a punctuator
    # or not then return the variables
    punctuators = {'{': 'Open Braces', '}': 'Close Braces', '[': 'Open Brackets'
        , ']': 'Close Brackets', '(': 'Open Parenthes', ')': 'Close Parenthes'
        , ',': 'Comma', ':': 'Colon', '#': 'Pound Sign', '.': 'Dot Notation'}
    p = ''
    if code in punctuators:
        p = punctuators[code]
        return code, p, len(code)
    return code


def get_char(code, count):  # a method that return the characters from input code and return it
    char = code[count]
    return char


def lexeme(code):
    lexeme_count = 0  # identify a variable as a counter
    while lexeme_count < len(code):
        class_char = get_char(code, lexeme_count)  # a variable to check the type of the lexeme

        if class_char.isdigit():  # check if the given character is a digit
            lex, tok, consumed = lex_num(code[lexeme_count:])
            print(lex, tok)
            lexeme_count += consumed
        elif class_char.isalpha() or class_char == '_':  # check if the given character is an identifier
            lex, tok, consumed = lex_id(code[lexeme_count:])
            print(lex, tok)
            lexeme_count += consumed
        elif class_char in operators:  # check if the given character is an operator
            lex, tok, consumed = lex_op(code[lexeme_count:])
            print(lex, tok)
            lexeme_count += consumed
        elif class_char in punctuators:  # check if the given character is a punctuator
            lex, tok, consumed = lex_pun(code[lexeme_count])
            print(lex, tok)
            lexeme_count += consumed
        else:  # none of above, it will increment lexeme_count by 1
            lexeme_count += 1


code = input()  # inserting the input into the variable
lexeme(code)  # call lexem method
