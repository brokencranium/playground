import string


def draw_hacker_rank():
    thickness = int(input())  # This must be an odd number
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
            thickness * 6))


def draw_map():
    """
    # Size: 7 x 21
    # ---------.|.---------
    # ------.|..|..|.------
    # ---.|..|..|..|..|.---
    # -------WELCOME-------
    #        13+7+13=> 21 - 7 / 2
    # ---.|..|..|..|..|.---
    # ------.|..|..|.------
    # ---------.|.---------
    :return:
    """
    n, m = map(int, input().split(" "))
    mid = int(m / 2) - 1

    hyphens = "-"
    center = ".|."
    center_text = "WELCOME"

    for i in range(int(n / 2)):
        print((hyphens * (mid - 3 * i)) + (center * (2 * i + 1)) + (hyphens * (mid - 3 * i)))

    print((hyphens * int((m - 7) / 2)) + center_text + (hyphens * int((m - 7) / 2)))

    for i in reversed(range(int(n / 2))):
        print((hyphens * (mid - 3 * i)) + (center * (2 * i + 1)) + (hyphens * (mid - 3 * i)))


def print_formatted(number):
    """
     1  1  1  1
    2  2  2 10
    :param number:
    :return:
    """
    width = len(f"{number:b}")
    for i in range(1, number + 1):
        for base in 'doXb':
            print('{0:{width}{base}}'.format(i, base=base, width=width), end=' ')
        print()


def rangoli():
    """
    --  --c----
    --c-b-c--
    c-b-a-b-c
    --c-b-c--
    ----c----
    a = 97
    -- -- -- --e-- -- -- --
    """

    def format_output(left_chars, width):
        output = []
        for index in range(2, width + 2):
            if not len(left_chars) or index % 2 == 0:
                output.append(hyphen)
            else:
                output.append(left_chars.pop())

        return output

    def print_format(ascii_number, i, width):
        left_chars = [chr(j) for j in range(ascii_number, i, -1)]
        right_chars = [chr(j) for j in range(i + 1, ascii_number + 1, 1)]
        right_chars.reverse()

        left_output: list = format_output(left_chars, width)
        right_output: list = format_output(right_chars, width)
        print("".join(reversed(left_output)) + chr(i) + "".join(right_output))

    def top_half(ascii_number: int, width: int):
        for i in range(ascii_number, 96, -1):
            print_format(ascii_number, i, width)

    def bottom_half(ascii_number: int, width: int):
        for i in range(98, ascii_number + 1, 1):
            print_format(ascii_number, i, width)

    num_chars = int(input())
    input_ascii_number = num_chars + 97 - 1
    hyphen = '-'
    width = (2 * num_chars - 2)

    top_half(input_ascii_number, width)
    bottom_half(input_ascii_number, width)


def rangoli_v2():
    # import string
    # string.ascii_lowercase

    size = int(input())
    chars = 'abcdefghijklmnopqrstuvwxyz'[:size]
    for i in range(size - 1, -size, -1):
        abs_i = abs(i)
        line = chars[:abs_i:-1] + chars[abs_i:]
        print("--" * int(abs_i) + "--".join(line) + "--" * int(abs_i))


def word_combinations_v1():
    string = "BANANA"
    size = len(string)
    vowels = 'AEIOU'

    kevin, stuart = list(zip(*[(string[i:j], '') if string[i:i + 1] in vowels
                               else ('', string[i:j])
                               for i in range(size)
                               for j in range(i + 1, size + 1)]
                             )
                         )

    kevin_scores = sum([kevin.count(k) for k in sorted(set(kevin), key=len) if k != ""])
    stuart_scores = sum([stuart.count(k) for k in sorted(set(stuart), key=len) if k != ""])

    if kevin_scores > stuart_scores:
        print(f"Kevin {kevin_scores}")
    elif stuart_scores > kevin_scores:
        print(f"Stuart {stuart_scores}")
    else:
        print("Draw")


def word_combination_v2():
    string = "BANANA"
    size = len(string)

    vowels = 'AEIOU'
    stuart_total = 0
    kevin_total = 0

    for i in range(size):
        if string[i:i + 1] in vowels:
            kevin_total += size - i
        else:
            stuart_total += size - i

    if kevin_total > stuart_total:
        print(f"Kevin {kevin_total}")
    elif stuart_total > kevin_total:
        print(f"Stuart {stuart_total}")
    else:
        print("Draw")


if __name__ == '__main__':
    word = int(input())
