separators = [';',',',' ',"'", '(', ')', '=', ':', '-', '{', '}']

def isSeparator(separator):
    if separator in separators:
        return True
    return False
