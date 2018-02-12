import encoder as en

x = open("encodings_readable.txt", "w", encoding="utf-8")

words = []
for line in open("new_test_data.txt", encoding="utf-8").read().split("\n")[:1400]:
    words.append(line.strip())

for word in words:
    x.write(str(en.encode(word)) + "\n")

x.close()
