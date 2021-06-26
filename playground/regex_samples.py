import re


def vowels_sequence():
    consonants = "qwrtypsdfghjklzxcvbnm"
    vowels = "aeiou"
    input_str = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
    regex_exp = re.compile(f'(?<=[{consonants}])([{vowels}]{{2,}})(?=[{consonants}])', flags=re.I)

    vowel_groups = list(map(lambda x: x.group(),
                            re.finditer(regex_exp,
                                        input_str)))
    print('\n'.join(vowel_groups or ['-1']))


def start_end_overlapping_matches():
    s = "aaadaa"
    k = "aa"
    match_expr = f'(?={k})'
    matches = [(match.start(), match.start() + len(k) - 1) for match in re.finditer(match_expr, s)]
    [print(match) for match in matches] if matches else print("(-1, -1)")


def floating_points():
    count = int(input())
    match_expr = r'^[-+]?[0-9]*\.[0-9]+$'
    for _ in range(count):
        print(True) if re.fullmatch(match_expr, input()) else print(False)


def group_numbers_sep():
    txt = "000,000, 100"
    match_expr = r'[.|,]'
    print(re.split(match_expr, txt))


def group_similar_numbers():
    txt = "..aa  12345678910122131415161718202123.."
    match_expr = r'([0-9a-zA-Z])\1+'
    result = re.search(match_expr, txt)
    print(result.group(1) if result else -1)


def sample_groups():
    m = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@hackerrank.com')
    #  m.group(0, 1,2,3)
    #  m.group(0)       # The entire match
    m = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@hackerrank.com')
    # m.groups() ('username', 'hackerrank', 'com')
    re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)', 'myname@hackerrank.com')
    # m.groupdict() {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}


def transform_string():
    def square(match):
        number = int(match.group(0))
        return str(number ** 2)

    print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))


def replace_strings():
    txt = "if a + b > 0 && || a - b < 0: &&"
    result = re.sub(r"(?<= )(&&|\|\|)(?= )",
                    lambda x: "and" if x.group() == "&&" else "or",
                    txt)
    print(result)


def validate_roman_strings():
    txt = "MDIV"
    thousands = r'M{0,3}'
    hundreds = r'(C[MD]|D?C{0,3})'
    tens = r'(X[L|C]|L?X{0,3})'
    ones = r'(V?I{0,3}|I[VX])'
    result = re.match(thousands + hundreds + tens + ones + "$", txt)
    print(result)


def parse_email_id():
    username = r'[a-zA-Z][\w|\-|\.|_]{0,}'
    domain = r"([a-zA-Z]+)"
    extension = r"([a-zA-Z]{1,3})"
    pattern = "<" + username + "@" + domain + "\." + extension + ">$"

    # counts = int(input())
    counts = 1
    for _ in range(counts):
        # name, email = input().split()
        name, email = "DEXTER", "<dexter@hotmail.com>"
        if re.match(pattern, email):
            print(name, email)


def match_hex_codes():
    input = 'color: #FfFdF8; background-color:#aef;'
    # do not match if the line is starting with hex code
    pattern = r'(?<!^)(#(?:[a-fA-F0-9]{3}){1,2})'
    matches = re.findall(pattern, input)
    for match in matches:
        print(match)


# ste {}, suite {}, suite {} and {}, # {}, suite {{}-{}}, ste. {} ,
# Suite {{}/{}}, Unit {}, Box {}, Bldg {}


if __name__ == '__main__':
    data = 'this is a #413 # 413 Suite:413 suite:413 suite 413'
    input = data.lower

    addr_identifiers = ['ste', 'suite', '#', 'unit', 'box', 'bldg', 'apt']
    for id in addr_identifiers:
        try:
            print("Searching for ", id)
            index = input.index(id)
            print(id, index, input[10:])
        except ValueError as ex:
            pass



#
    # pattern = r'(?<!^)(#(?:[a-fA-F0-9])+)'
    # matches = re.findall(pattern, input)
    # for match in matches:
    #     print(match)

    # match_expr = r'(^[-|+|0-9][0-9]+\.[0-9]+) | (^[-|+|]\.[0-9]+) | (^\.[0-9]+)'

    # thousand = 'M{0,3}'
    # hundred = '(C[MD]|D?C{0,3})'
    # ten = '(X[CL]|L?X{0,3})'
    # digit = '(I[VX]|V?I{0,3})'
    # print (bool(re.match(thousand + hundred+ten+digit +'$', txt)))
