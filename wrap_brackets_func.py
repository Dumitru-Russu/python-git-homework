

def wrap_brackets( text ):
    return "(" + text + ")"

def wrap_box_brackets( text ):
    return "[" + text + "]"

def wrap_sign( text ):
    return "<" + text + ">"




print(    wrap_sign\
        (wrap_sign\
        (wrap_sign\
        (wrap_box_brackets\
        (wrap_box_brackets\
        (wrap_box_brackets\
        (wrap_brackets("12345"))))))))