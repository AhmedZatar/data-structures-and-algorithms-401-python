import re

def multi_bracket_validation(input):
    x=False
    if input.count('{')==input.count('}') and input.count('(')==input.count(')') and input.count('[')==input.count(']'):
        x=True
    try :
       if re.search("\(.?}", input) or re.search("\[.?}", input) or re.search("\[.?)", input) or re.search("\(.?]", input) or re.search("\{.?)", input) or re.search("\{.?]", input):
            x=False
    except:
        return x
    
    return x

print(multi_bracket_validation('{}'))
print(multi_bracket_validation('{}(){}'))
print(multi_bracket_validation('()[[Extra Characters]]'))
print(multi_bracket_validation('(){}[[]]'))
print(multi_bracket_validation('{}{Code}[Fellows](())'))
print(multi_bracket_validation('[({}]'))
print(multi_bracket_validation('(]('))
print(multi_bracket_validation('{(})'))
print(multi_bracket_validation('{'))
print(multi_bracket_validation(')'))
print(multi_bracket_validation('[}'))














