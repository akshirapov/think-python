
def draw_sep(column):
    print('+ - - - - ' * column, end='')
    print('+')


def draw_row(column):
    draw_sep(column)
    print('/         ' * column, end='')
    print('/')
    print('/         ' * column, end='')
    print('/')
    print('/         ' * column, end='')
    print('/')
    print('/         ' * column, end='')
    print('/')


def draw_grid_2x2():
    draw_row(2)
    draw_row(2)
    draw_sep(2)


def draw_grid_4x4():
    draw_row(4)
    draw_row(4)
    draw_row(4)
    draw_row(4)
    draw_sep(4)


draw_grid_2x2()
draw_grid_4x4()
