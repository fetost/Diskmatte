from itertools import permutations

# This function generates all possible paths that could be taken from the starting position to the ending position. 
# This takes into account the number of moves up and down that need to be made though parameters.
def generate_paths_up_down(moves_up, moves_down):
    moves = ['U'] * moves_up + ['L'] * moves_down
    return set(permutations(moves))

# Task a
moves_up_a = 3
moves_down_a = 4
paths_a = generate_paths_up_down(moves_up_a, moves_down_a)

# Number of paths
print(f"Number of paths (Part a): {len(paths_a)}")
for path in paths_a: # Print each path
    print(''.join(path))


# This function checks if a path crosses or touches the x-axis.
def touches_x_axis(path, start_y):
    y = start_y
    for move in path:
        if move == 'U':
            y += 1
        else:
            y -= 1
        if y == 0:
            return True
    return False

# Task b
paths_cross_b = [path for path in paths_a if touches_x_axis(path, 3)]

# Number of paths that touch/cross the x-axis
print(f"Number of paths that touch/cross the x-axis: {len(paths_cross_b)}")
for path in paths_cross_b:
    print(''.join(path))


# This function checks if a path never touches the x-axis
def never_x_axis(path, start_y):
    y = start_y
    for move in path:
        if move == 'U':
            y += 1
        else:
            y -= 1
        if y <= 0:  # LEss than or equal to 0, as we want to check if it touches the x-axis
            return False
    return True

# Task c
paths_never_cross_c = [path for path in paths_a if never_x_axis(path, 3)]

# Number of paths that never touch/cross the x-axis
print(f"Number of paths that never touch/cross the x-axis: {len(paths_never_cross_c)}")
for path in paths_never_cross_c:
    print(''.join(path))


# Task d
moves_up_d = 6
moves_down_d = 7
paths_d = generate_paths_up_down(moves_up_d, moves_down_d)

# This filters paths that never touch or cross the x-axis
paths_never_cross_d = [path for path in paths_d if never_x_axis(path, 6)]

# Number of paths that never touch/cross the x-axis
print(f"Total paths for this part: {len(paths_d)}")
print(f"Number of paths that never touch/cross the x-axis: {len(paths_never_cross_d)}")

