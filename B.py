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


def mark_rectangle(main_map2, carriage_x, carriage_y, rect_width, rect_height, a):
    for i in range(carriage_y - 1, carriage_y + rect_height - 1):
        for j in range(carriage_x - 1, carriage_x + rect_width - 1):
            main_map2[i][j] = a


def find_new_carriage_pos(tab):
    for j in range(g_map_height):
        for i in range(g_map_width):
            if tab[j][i] == 0:
                return i + 1, j + 1
    return g_map_width + 1, g_map_height + 1


def get_region(carriage_x, carriage_y, rect_width, rect_height):
    lst = []
    for j1 in range(carriage_y - 1, carriage_y + rect_height - 1):
        st = g_main_map[j1][carriage_x - 1: carriage_x + rect_width - 1]
        lst.append(st)
    return lst

def take_list_recursive(
        answer_rects, main_map2, possible_rectangle_side_size,
        carriage_x, carriage_y, solution_is_found):

    # form loop
    for i in possible_rectangle_side_size:

        rect_height = i
        rect_width = int(rectangle_square / i)

        if carriage_x + rect_width - 1 > g_map_width or carriage_y + rect_height - 1 > g_map_height:
            continue

        part = get_region(carriage_x, carriage_y, rect_width, rect_height)

        if count_object_num(part) != 1:
            continue

        mark_rectangle(main_map2, carriage_x, carriage_y, rect_width, rect_height, 1)

        answer_rects.append(part)
        carriage_x_next, carriage_y_next = find_new_carriage_pos(main_map2)

        if carriage_x_next > g_map_width and carriage_y_next > g_map_height:
            solution_is_found = True
            return answer_rects, solution_is_found
        else:
            # go to next rectagnle
            answer_rects, solution_is_found = take_list_recursive(answer_rects, main_map2, possible_rectangle_side_size,
                    carriage_x_next, carriage_y_next, solution_is_found)
            if solution_is_found:
                return answer_rects, solution_is_found
            else:
                answer_rects.pop()
                mark_rectangle(main_map2, carriage_x, carriage_y, rect_width, rect_height, 0)

        if solution_is_found:
            return answer_rects, solution_is_found
    return answer_rects, solution_is_found

def take_list(possible_rectangle_side_size):
    solution_is_found = False
    answer_rects = []
    search_i = 1
    search_j = 1
    table = []
    for i in range(g_map_height):
        table.append([])
        for j in range(g_map_width):
            table[i].append(0)
    answer_rects, solution_is_found = take_list_recursive(answer_rects,
            table,
            possible_rectangle_side_size,
            search_i, search_j, solution_is_found)
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

    with open('output.txt', 'w') as f:
        g_map_height = len(g_main_map)
        if g_map_height == 0:
            return
        g_map_width = len(g_main_map[0])
        map_square = g_map_width * g_map_height
        rectangles_num = count_object_num(g_main_map)
        if rectangles_num > 10:
            return
        if rectangles_num == 0:
            return
        if map_square % rectangles_num != 0:
            return
        else:
            rectangle_square = int(map_square / rectangles_num)
        possible_rectangle_side_size = find_possible_rectangle_side_size(rectangle_square)
        answer_rects = take_list(possible_rectangle_side_size)
        for i in answer_rects:
            for j in i:
                f.write(j + '\n')
            f.write('\n')
        f.close()


main()
