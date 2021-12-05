from line import Line
from matrix import Matrix

def str_to_point(str):
    p = str.split(',')

    point = (int(p[0]),int(p[1]))
    return point


def process_file():
    lines = open('input','r').readlines()

    rects = []
    for line in lines:
        parts = line.split("->")
        p1 = str_to_point(parts[0])
        p2 = str_to_point(parts[1])

        rects.append(Line(p1,p2))

    return (rects)

lines = process_file()
matrix = Matrix()

#print(matrix)
#print(lines[0].calc_points())
for line in lines:
    matrix.add_line(line)

print(matrix.get_num_inter())