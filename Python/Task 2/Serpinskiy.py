def gen_ser_tri(n):
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


def print_ser_tri(tri):
    for row in tri:
        mod_row = ['*' if n % 2 != 0 else ' ' for n in row]
        print(' '.join(mod_row).center(len(' '.join(map(str, tri[-1])))))


n = int(input("Stroke num: "))
sepniskiy_tri = gen_ser_tri(n)
print_ser_tri(sepniskiy_tri)
