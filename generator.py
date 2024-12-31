import sys
import random
from tabulate import tabulate

with open("input.txt", encoding='utf-8') as file:
    content = file.read()


participants = sys.argv[1:]
max_length = 25

content = content.split("---\n")

def insert_line_breaks(text, min_length=20):
    words = text.split()
    result = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 > min_length:
            result.append(current_line.strip().ljust(max_length))
            current_line = word
        else:
            current_line += " " + word

    if current_line:
        result.append(current_line.strip().ljust(max_length))

    return "\n".join(result)

def generate_board_content():
    categories = []
    result = []

    for i in range(0, len(content), 2):
        elm = (int(content[i].strip()), content[i+1].strip())
        categories.append(elm)

    for count, elm in categories:
        elm = elm.split("\n")
        random.shuffle(elm)
        result += elm[:count]
    random.shuffle(result)
    return result

for p in participants:
    res = generate_board_content()

    outdict = {}
    for i in range(5):
        outdict[i] = [insert_line_breaks(item) for item in res[i*5:(i+1)*5]]

    f = open(f"{p}.txt", "w", encoding='utf-8')
    f.write(tabulate(outdict, tablefmt="grid"))
    f.close()