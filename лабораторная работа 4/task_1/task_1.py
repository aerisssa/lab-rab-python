# TODO решите задачу
def task() -> float:
    rez = 0
    ch1 = 0
    ch2 = 0

    f = open("input.json", "r")
    file = f.readlines()

    for i in range(len(file)):
        if file[i].find("score") != -1:
            ch1 = float(file[i][((file[i].find("score")) + 8):len(file[i]) - 2])
        elif (file[i].find("weight")) != -1:
            ch2 = float(file[i][((file[i].find("weight")) + 9):len(file[i]) - 1])
        if (ch1 != 0) and (ch2 != 0):
            rez += ch1 * ch2
            ch1, ch2 = 0, 0

    f.close()

    return round(rez, 3)


print(task())
