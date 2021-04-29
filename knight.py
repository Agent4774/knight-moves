#!/usr/bin/env python3
from typing import List, Tuple
import string


def get_parents(tree):
    reversed_keys = [key for key in tree][::-1]
    new_tree = {}
    parents = []
    for key in reversed_keys:
        new_tree[key] = tree[key]
    for key in new_tree:
        if not parents:
            parents.extend([new_tree[key][-1], key])
            continue
        if parents[-1] in new_tree[key]:
            parents.append(key)
    return parents[::-1]

def get_available_moves(cell, axis_Y, width):
    all_possible_moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    available_moves = []
    for move in all_possible_moves:
        if 0 < cell[1] + move[0] <= width \
        and 0 < (axis_Y.index(cell[0]) + 1) + move[1] <= width:
            available_moves.append(move)
    return available_moves

def shortest_path(start: tuple = ('a', 1), target: tuple = ('h', 8), board_width: int = 8, board_height: int = 8) -> List[Tuple[str, int]]:
    if start == target:
        return start
    if any([board_width > 26, board_width != board_height]):
        return '1) The board is not of square shape\n2) 26 is a max value for both width and height'
    queue = [start]
    axis_Y = list(string.ascii_lowercase)
    visited_cells = []
    moves_tree = {}

    while queue:
        current_cell = queue.pop(0)
        available_moves = get_available_moves(current_cell, axis_Y, board_width)
        for move in available_moves:
            chess_board_cell = (axis_Y[axis_Y.index(current_cell[0]) + move[1]], move[0] + current_cell[1])
            if chess_board_cell in visited_cells:
                continue
            if current_cell not in moves_tree:
                moves_tree[current_cell] = []
            moves_tree[current_cell].append(chess_board_cell)
            if chess_board_cell == target:
                return get_parents(moves_tree)
            visited_cells.append(chess_board_cell)
            queue.append(chess_board_cell)


if __name__ == '__main__':
    path = shortest_path()
    print(path)
