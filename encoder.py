import pickle


def encode(word):

    tem = ["aa", "i", "u", "ri", "e", "ai",
           "o", "au", "ka", "kha", "ga", "gha",
           "ca", "cha", "ja", "jha", "ta", "tha",
           "da", "dha", "na", "pa",
           "pha", "ba", "bha", "ma", "ya", "ra",
           "la", "sa", "ha"]

    print(len(tem))

    groups = [["aa", "a"], ["i", "ee"], ["u", "w"], ["ri", "r"], ["e"], ["ai", "oi"],
              ["o", "oo"], ["au", "ou", "ow"], ["ka", "k"], ["kha", "kh"], ["ga", "g"], ["gha", "gh"],
              ["ca", "c"], ["cha", "ch"], ["ja", "j", "z", "x"], ["jha", "jh"], ["ta", "t"], ["tha", "th"],
              ["da", "d"], ["dha", "dh"], ["ta", "t"], ["tha", "th"], ["na", "n"], ["pa", "p"],
              ["pha", "ph", "f"], ["ba", "b"], ["bha", "bh", "v"], ["ma", "m"], ["ya", "y"], ["ra", "r", "rh"],
              ["la", "l"], ["sa", "s", "sh"], ["ha", "h"]]

    pos, encoding = 0, []

    while pos < len(word):
        CHK_TR, CHK_BI, CHK_UN = word[pos:pos + 3], word[pos:pos + 2], word[pos:pos + 1]
        CON_TR, CON_BI, CON_UN = False, False, False
        # CHECK TR
        for group in groups:
            if CHK_TR in group:
                pos += 3
                encoding.append(tem.index(group[0]) + 1)
                CON_TR = True
                break
        # CHECK BI
        if not CON_TR:
            for group in groups:
                if CHK_BI in group:
                    pos += 2
                    encoding.append(tem.index(group[0]) + 1)
                    CON_BI = True
                    break
        # CHECK UN
        if not CON_TR and not CON_BI:
            for group in groups:
                if CHK_UN in group:
                    pos += 1
                    encoding.append(tem.index(group[0]) + 1)
                    CON_UN = True
                    break
        # CHECK NOT IN LIST
        if not CON_TR and not CON_BI and not CON_UN:
            pos += 1
            encoding.append(35)

    return encoding # + [0]*(15 - len(encoding))


print(encode("krci"))

# [9, 7, 4, 14, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [9, 4, 14, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



encodings = []
show = open("encodings_bn.txt", "w", encoding="utf-8")
for word in open("bn_words.txt", encoding="utf-8").read().split("\n")[:-1]:
    encoded = encode(word.strip())
    show.write(str(encoded) + "\n")
    encodings.append(encoded)

show.close()
#
# with open("bn_encodings_lo.pkl", "wb") as f:
#     pickle.dump(encodings, f)
#
