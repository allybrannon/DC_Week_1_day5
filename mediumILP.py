array3 = [[2, 1, 3], [3, 4, 5]]
array4 = [[5, 6, 6], [7, 8, 1]]

add_results = []
i = 0
while i < len(array3):
    s_ar = []
    column = 0
    while column < len(array3[0]):
        s_ar.append(array3[i][column] + array4[i][column])
        column += 1
    i += 1
    add_results.append(s_ar)
print(add_results)
