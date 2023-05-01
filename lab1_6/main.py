def levenshtein(str_a, str_b):
    t = [[0 for x in range(len(str_b) + 1)] for y in range(len(str_a) + 1)]
    for x in range(len(str_b) + 1):
        t[0][x] = x
    for y in range(len(str_a) + 1):
        t[y][0] = y

    for i in range(1, len(str_a) + 1):
        for j in range(1, len(str_b) + 1):
            if str_a[i - 1] == str_b[j - 1]:
                cost = 0
            else:
                cost = 1
            t[i][j] = min(t[i - 1][j] + 1, t[i][j - 1] + 1, t[i - 1][j - 1] + cost)
    return t[len(str_a)][len(str_b)]


if __name__ == '__main__':
    print(levenshtein("pies", "pies"))
