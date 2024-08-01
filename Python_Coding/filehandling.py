import logging

with open("test_file.txt", 'w') as file:
    lines=["This is the first line.\n",
        "This is the second line.\n",
        "This is the third line.\n"]
    file.writelines(lines)

file=open('test_file.txt', 'r')
print(file)


logger=logging.getLogger("")

handler= logging.FileHandler("")
formatter= logging.Formatter("")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.setLevel(logging.INFO)