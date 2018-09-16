#/usr/bin/python3
import math

rectangle_square = 0
g_main_map = []
g_map_width = 0
g_map_height = 0
g_main_map_copy = []


def count_object_num(lst):
    x = 0
    for i in range(len(lst)):
        x += lst[i].count('o', 0, len(lst[i]))
    return x


def find_possible_rectangle_side_size(n):
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
    return x_map + 1, y_map + 1


def take_parts(x, y, rect_width, rect_height):
    lst = []
    for j1 in range(y - 1, y + rect_height - 1):
        st = g_main_map[j1][x - 1: x + rect_width - 1]
        lst.append(st)
    return lst

def take_list_recursive(
        answer_rects, main_map2, possible_rectangle_side_size,
        x_i, y_j, b):

    for i in possible_rectangle_side_size:
        rect_height = i
        rect_width = int(rectangle_square / i)

        if x_i + rect_width - 1 <= g_map_width and y_j + rect_height - 1 <= g_map_height:

            part = take_parts(x_i, y_j, rect_width, rect_height)

            if count_object_num(part) == 1:

                make_table(main_map2, x_i, y_j, rect_width, rect_height, 1)
                answer_rects.append(part)
                x_i_next, y_j_next = search_xy(main_map2, g_map_width, g_map_height)
                if x_i_next > g_map_width and y_j_next > g_map_height:
                    b = True
                    return answer_rects, b
                else:
                    answer_rects, b = take_list_recursive(answer_rects, main_map2, possible_rectangle_side_size,
                            x_i_next, y_j_next, b)
                    if b:
                        return answer_rects, b
                    else:
                        answer_rects.pop()
                        make_table(main_map2, x_i, y_j, rect_width, rect_height, 0)
        if b:
            return answer_rects, b
    return answer_rects, b

def take_list(possible_rectangle_side_size):
    b = False
    answer_rects = []
    search_i = 1
    search_j = 1
    table = []
    for i in range(g_map_height):
        table.append([])
        for j in range(g_map_width):
            table[i].append(0)
    answer_rects, b = take_list_recursive(answer_rects,
            table,
            possible_rectangle_side_size,
            search_i, search_j, b)
    return answer_rects


def main():
    global rectangle_square
    global g_main_map
    global g_map_height
    global g_map_width
    with open('input.txt') as f:
        g_main_map = []
        for line in f:
            g_main_map.append(line.rstrip())
    f.close()
    g_map_height = len(g_main_map)
    if g_map_height == 0:
        return
    g_map_width = len(g_main_map[0])
    map_square = g_map_width * g_map_height
    rectangles_num = count_object_num(g_main_map)
    if rectangles_num == 0:
        return
    if map_square % rectangles_num != 0:
        return
    else:
        rectangle_square = int(map_square / rectangles_num)
    possible_rectangle_side_size = find_possible_rectangle_side_size(rectangle_square)
    answer_rects = take_list(possible_rectangle_side_size)
    with open('output.txt', 'w') as f:
        for i in answer_rects:
            for j in i:
                f.write(j + '\n')
            f.write('\n')
    f.close()


main()
