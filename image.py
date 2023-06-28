def imageSmoother_661(img):
    row = len(img)
    col = len(img[0])
    result = [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            total = 0
            count = 0
            for m in range(i - 1, i + 2):
                for n in range(j - 1, j + 2):
                    if 0 <= m < row and 0 <= n < col:
                        total += img[m][n]
                        count += 1
            result[i][j] = int(total / count)
    return result
