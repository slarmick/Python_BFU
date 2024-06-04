def gen_pas_tri(n):
    tri = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(tri[i - 1][j - 1] + tri[i - 1][j])
        tri.append(row)
    return tri


def print_pas_tri(tri):
    for row in tri:
        print(' '.join(map(str, row)).center(len(' '.join(map(str, tri[-1])))))


n = int(input("Stroke num: "))
pascal_tri = gen_pas_tri(n)
print_pas_tri(pascal_tri)
