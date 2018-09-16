import math


def counting(lst):
    x = 0
    for i in range(len(lst)):
        x += lst[i].count('o', 0, len(lst[i]))
    return x


def search_div(n):
    div = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            div.add(i)
            div.add(int(n / i))
    div = list(div)
    div.sort()
    return div


def put_parts():
    pass


def make_table(table, x, y, x_map, y_map, a):
    for i in range(y - 1, y + y_map - 1):
        for j in range(x - 1, x + x_map - 1):
            table[i][j] = a
    return table


def search_xy(tab, x_map, y_map):
    for j in range(y_map):
        for i in range(x_map):
            if tab[j][i] == 0:
                return i + 1, j + 1
    return x_map, y_map


def take_part(m, x, y, i, j):
    lst = []
    for j1 in range(y - 1, y + j - 1):
        st = m[j1][x - 1: x + i - 1]
        lst.append(st)
    return lst


def take_list(lists, tab, m, x_m, y_m, d, n_s, x_i, y_j, b):
    for i in d:
        y = i
        x = int(n_s / i)
        if x_i + x - 1 <= x_m and y_j + y - 1 <= y_m:
            part = take_part(m, x_i, y_j, x, y)
            if counting(part) == 1:
                make_table(tab, x_i, y_j, x, y, 1)
                lists.append(part)
                x_i_next, y_j_next = search_xy(tab, x_m, y_m)
                if x_i_next == x_m and y_j_next == y_m:
                    b = True
                    return lists, b
                else:
                    lists, b = take_list(lists, tab, m, x_m, y_m, d, n_s, x_i_next, y_j_next, b)
                    if b:
                        return lists, b
                    else:
                        lists.pop()
                        make_table(tab, x_i, y_j, x, y, 0)
        if b:
            return lists, b
    return lists, b


def main():
    with open('input.txt') as f:
        maps = []
        for line in f:
            maps.append(line.rstrip())
    f.close()
    y_map = len(maps)
    x_map = len(maps[0])
    size = x_map * y_map
    n = counting(maps)
    if size % n != 0:
        return
    else:
        n_size = int(size / n)
    div = search_div(n_size)
    table = []
    for i in range(y_map):
        table.append([])
        for j in range(x_map):
            table[i].append(0)
    search_i = 1
    search_j = 1
    lists = []
    b = False
    lists, b = take_list(lists, table, maps, x_map, y_map, div, n_size, search_i, search_j, b)
    with open('output.txt', 'w') as f:
        for i in lists:
            for j in i:
                f.write(j + '\n')
            f.write('\n')
    f.close()


main()
