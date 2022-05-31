import time
from copy import deepcopy

import numpy as np
from numpy import infty
from HistoryTable import HistoryTable
from ChessBoard import *


class Evaluate(object):
    # 棋子棋力得分
    single_chess_point = {
        'c': 989,   # 车
        'm': 439,   # 马
        'p': 442,   # 炮
        's': 226,   # 士
        'x': 210,   # 象
        'z': 55,    # 卒
        'j': 65536  # 将
    }
    # 红兵（卒）位置得分
    red_bin_pos_point = [
        [1, 3, 9, 10, 12, 10, 9, 3, 1],
        [18, 36, 56, 95, 118, 95, 56, 36, 18],
        [15, 28, 42, 73, 80, 73, 42, 28, 15],
        [13, 22, 30, 42, 52, 42, 30, 22, 13],
        [8, 17, 18, 21, 26, 21, 18, 17, 8],
        [3, 0, 7, 0, 8, 0, 7, 0, 3],
        [-1, 0, -3, 0, 3, 0, -3, 0, -1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    # 红车位置得分
    red_che_pos_point = [
        [185, 195, 190, 210, 220, 210, 190, 195, 185],
        [185, 203, 198, 230, 245, 230, 198, 203, 185],
        [180, 198, 190, 215, 225, 215, 190, 198, 180],
        [180, 200, 195, 220, 230, 220, 195, 200, 180],
        [180, 190, 180, 205, 225, 205, 180, 190, 180],
        [155, 185, 172, 215, 215, 215, 172, 185, 155],
        [110, 148, 135, 185, 190, 185, 135, 148, 110],
        [100, 115, 105, 140, 135, 140, 105, 115, 110],
        [115, 95, 100, 155, 115, 155, 100, 95, 115],
        [20, 120, 105, 140, 115, 150, 105, 120, 20]
    ]
    # 红马位置得分
    red_ma_pos_point = [
        [80, 105, 135, 120, 80, 120, 135, 105, 80],
        [80, 115, 200, 135, 105, 135, 200, 115, 80],
        [120, 125, 135, 150, 145, 150, 135, 125, 120],
        [105, 175, 145, 175, 150, 175, 145, 175, 105],
        [90, 135, 125, 145, 135, 145, 125, 135, 90],
        [80, 120, 135, 125, 120, 125, 135, 120, 80],
        [45, 90, 105, 190, 110, 90, 105, 90, 45],
        [80, 45, 105, 105, 80, 105, 105, 45, 80],
        [20, 45, 80, 80, -10, 80, 80, 45, 20],
        [20, -20, 20, 20, 20, 20, 20, -20, 20]
    ]
    # 红炮位置得分
    red_pao_pos_point = [
        [190, 180, 190, 70, 10, 70, 190, 180, 190],
        [70, 120, 100, 90, 150, 90, 100, 120, 70],
        [70, 90, 80, 90, 200, 90, 80, 90, 70],
        [60, 80, 60, 50, 210, 50, 60, 80, 60],
        [90, 50, 90, 70, 220, 70, 90, 50, 90],
        [120, 70, 100, 60, 230, 60, 100, 70, 120],
        [10, 30, 10, 30, 120, 30, 10, 30, 10],
        [30, -20, 30, 20, 200, 20, 30, -20, 30],
        [30, 10, 30, 30, -10, 30, 30, 10, 30],
        [20, 20, 20, 20, -10, 20, 20, 20, 20]
    ]
    # 红将位置得分
    red_jiang_pos_point = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9750, 9800, 9750, 0, 0, 0],
        [0, 0, 0, 9900, 9900, 9900, 0, 0, 0],
        [0, 0, 0, 10000, 10000, 10000, 0, 0, 0],
    ]
    # 红相或士位置得分
    red_xiang_shi_pos_point = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 60, 0, 0, 0, 60, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [80, 0, 0, 80, 90, 80, 0, 0, 80],
        [0, 0, 0, 0, 0, 120, 0, 0, 0],
        [0, 0, 70, 100, 0, 100, 70, 0, 0],
    ]

    red_pos_point = {
        'z': red_bin_pos_point,
        'm': red_ma_pos_point,
        'c': red_che_pos_point,
        'j': red_jiang_pos_point,
        'p': red_pao_pos_point,
        'x': red_xiang_shi_pos_point,
        's': red_xiang_shi_pos_point
    }

    def __init__(self, team):
        self.team = team

    def get_single_chess_point(self, chessmap, src):
        chess = chessmap[src[0]][src[1]]
        if chess[0] == self.team:
            return self.single_chess_point[chess[1]]
        else:
            return -1 * self.single_chess_point[chess[1]]

    def get_chess_pos_point(self, chessmap, src):
        row, col = src
        chess = chessmap[row][col]
        red_pos_point_table = self.red_pos_point[chess[1]]
        if chess[0] == 'r':
            pos_point = red_pos_point_table[row][col]
        else:
            pos_point = red_pos_point_table[9 - row][col]
        if chess[0] != self.team:
            pos_point *= -1
        return pos_point

    def evaluate(self, chessmap):
        point = 0
        for chess in fetch_any_chess(chessmap):
            point += self.get_single_chess_point(chessmap, chess)
            point += self.get_chess_pos_point(chessmap, chess)
        return point


class ChessMap(object):
    def __init__(self, chessboard: ChessBoard):
        self.chess_map = copy.deepcopy(chessboard.chessboard_map)


class ChessAI(object):
    def __init__(self, computer_team):
        self.team = computer_team
        self.max_depth = 3
        self.old_pos = [0, 0]
        self.new_pos = [0, 0]
        self.evaluate_class = Evaluate(self.team)
        self.history = HistoryTable()


    def get_next_step(self, chessboard: ChessBoard) -> (int, int, int, int):
        print()
        c_map = [[transfer(s) for s in line] for line in chessboard.get_chessboard_str_map()]
        value, result = self.alpha_beta(c_map, -infty, infty, True, self.max_depth)
        return result[0][0], result[0][1], result[1][0], result[1][1]


    @staticmethod
    def get_nxt_player(player):
        if player == 'r':
            return 'b'
        else:
            return 'r'

    def weight_red(self, move):
        return self.history.get(False, move)

    def weight_black(self, move):
        return self.history.get(True, move)

    def alpha_beta(self, state, alpha, beta, is_max, depth):
        if depth == 0:
            return self.evaluate_class.evaluate(state), None

        steps = generate_possbile_steps(state, 'b') if is_max else generate_possbile_steps(state, 'r')
        steps.sort(key=self.weight_black if is_max else self.weight_red)
        next_states = [make_nxt_state(state, src, dst) for src, dst in steps]

        target = None
        for i, chessboard in enumerate(next_states):
            temp, step = self.alpha_beta(chessboard, alpha, beta, not is_max, depth - 1)
            if is_max and temp > alpha:
                alpha = temp
                target = steps[i]
            elif not is_max and temp < beta:
                beta = temp
                target = steps[i]
            if alpha >= beta:
                break

        if target is not None:
            self.history.renew(is_max, target, depth)
        return (alpha, target) if is_max else (beta, target)


def transfer(string: str):
    if string != "":
        li = string.split('_')
        return li[0], li[1]
    else:
        return None, None

def fetch_any_chess(chessmap):
    result = []
    for i in range(10):
        for j in range(9):
            if chessmap[i][j][0] is not None:
                result.append((i, j))
    return result

def fetch_camp_chess(chessmap, camp: str):
    result = []
    for i in range(10):
        for j in range(9):
            if chessmap[i][j][0] == camp:
                result.append((i, j))
    return result

def generate_possbile_dest(chessmap, src):
    result = []
    row, col = src
    camp = chessmap[src[0]][src[1]][0]
    name = chessmap[src[0]][src[1]][1]

    if name == "z":  # 卒
        if camp == "r":  # 红方
            if row - 1 >= 0:  # 只能向上移动
                if chessmap[row - 1][col][0] != camp:
                    result.append((row - 1, col))
        else:  # 黑方
            if row + 1 <= 9:  # 只能向下移动
                if chessmap[row + 1][col][0] != camp:
                    result.append((row + 1, col))
        # 左右判断
        if (camp == "r" and 0 <= row <= 4) or (camp == "b" and 5 <= row <= 9):  # 左、右一步
            # 左
            if col - 1 >= 0 and chessmap[row][col - 1][0] != camp:
                result.append((row, col - 1))
            # 右
            if col + 1 <= 8 and chessmap[row][col + 1][0] != camp:
                result.append((row, col + 1))
    elif name == "j":  # 将
        # 因为"将"是不能过河的，所以要计算出它们可以移动的行的范围
        row_start, row_stop = (0, 2) if camp == "b" else (7, 9)
        # 有4个方向的判断
        if row - 1 >= row_start and chessmap[row - 1][col][0] != camp:
            result.append((row - 1, col))
        if row + 1 <= row_stop and chessmap[row + 1][col][0] != camp:
            result.append((row + 1, col))
        if col - 1 >= 3 and chessmap[row][col - 1][0] != camp:
            result.append((row, col - 1))
        if col + 1 <= 5 and chessmap[row][col + 1][0] != camp:
            result.append((row, col + 1))
    elif name == "s":  # 士
        # 因为士是不能过河的，所以要计算出它们可以移动的行的范围
        row_start, row_stop = (0, 2) if camp == "b" else (7, 9)
        if row - 1 >= row_start and col - 1 >= 3 and chessmap[row - 1][col - 1][0] != camp:
            result.append((row - 1, col - 1))
        if row - 1 >= row_start and col + 1 <= 5 and chessmap[row - 1][col + 1][0] != camp:
            result.append((row - 1, col + 1))
        if row + 1 <= row_stop and col - 1 >= 3 and chessmap[row + 1][col - 1][0] != camp:
            result.append((row + 1, col - 1))
        if row + 1 <= row_stop and col + 1 <= 5 and chessmap[row + 1][col + 1][0] != camp:
            result.append((row + 1, col + 1))
    elif name == "x":  # 象
        # 因为象是不能过河的，所以要计算出它们可以移动的行的范围
        row_start, row_stop = (0, 4) if camp == "b" else (5, 9)
        # 有4个方向的判断(没有越界，且没有蹩象腿)
        if row - 2 >= row_start and col - 2 >= 0 and chessmap[row - 1][col - 1][0] is None \
            and chessmap[row - 2][col - 2][0] != camp:
                result.append((row - 2, col - 2))
        if row - 2 >= row_start and col + 2 <= 8 and chessmap[row - 1][col + 1][0] is None \
            and chessmap[row - 2][col + 2][0] != camp:
                result.append((row - 2, col + 2))
        if row + 2 <= row_stop and col - 2 >= 0 and chessmap[row + 1][col - 1][0] is None \
            and chessmap[row + 2][col - 2][0] != camp:
                result.append((row + 2, col - 2))
        if row + 2 <= row_stop and col + 2 <= 8 and chessmap[row + 1][col + 1][0] is None \
            and chessmap[row + 2][col + 2][0] != camp:
                result.append((row + 2, col + 2))
    elif name == "m":  # 马
        # 需要判断的是4个方向，每个方向对应2个位置
        # 上方
        if row - 1 >= 0 and chessmap[row - 1][col][0] is None:  # 如果当前棋子没有被蹩马腿，那么再对这个方向的2个位置进行判断
            # 左上
            if row - 2 >= 0 and col - 1 >= 0 and chessmap[row - 2][col - 1][0] != camp:
                result.append((row - 2, col - 1))
            # 右上
            if row - 2 >= 0 and col + 1 <= 8 and chessmap[row - 2][col + 1][0] != camp:
                result.append((row - 2, col + 1))
        # 下方
        if row + 1 <= 9 and chessmap[row + 1][col][0] is None:  # 如果当前棋子没有被蹩马腿，那么再对这个方向的2个位置进行判断
            # 左下
            if row + 2 <= 9 and col - 1 >= 0 and chessmap[row + 2][col - 1][0] != camp:
                result.append((row + 2, col - 1))
            # 右下
            if row + 2 <= 9 and col + 1 <= 8 and chessmap[row + 2][col + 1][0] != camp:
                result.append((row + 2, col + 1))
        # 左方
        if col - 1 >= 0 and not chessmap[row][col - 1]:  # 如果当前棋子没有被蹩马腿，那么再对这个方向的2个位置进行判断
            # 左上2（因为有左上了，暂且称为左上2吧）
            if row - 1 >= 0 and col - 2 >= 0 and chessmap[row - 1][col - 2][0] != camp:
                result.append((row - 1, col - 2))
            # 左下2
            if row + 1 <= 9 and col - 2 >= 0 and chessmap[row + 1][col - 2][0] != camp:
                result.append((row + 1, col - 2))
        # 右方
        if col + 1 <= 8 and not chessmap[row][col + 1]:  # 如果当前棋子没有被蹩马腿，那么再对这个方向的2个位置进行判断
            # 右上2（因为有右上了，暂且称为右上2吧）
            if row - 1 >= 0 and col + 2 <= 8 and chessmap[row - 1][col + 2][0] != camp:
                result.append((row - 1, col + 2))
            # 右下2
            if row + 1 <= 9 and col + 2 <= 8 and chessmap[row + 1][col + 2][0] != camp:
                result.append((row + 1, col + 2))
    elif name == "c":  # 车
        # 一行
        left_stop = False
        right_stop = False
        for i in range(1, 9):
            # 左边位置没有越界且没有遇到任何一个棋子
            if not left_stop and col - i >= 0:
                if chessmap[row][col - i][0] is None:
                    # 如果没有棋子,则将当前位置组成一个元组，添加到列表
                    result.append((row, col - i))
                else:
                    left_stop = True
                    if chessmap[row][col - i][0] != camp:
                        # 如果当前位置有棋子，那么就判断是否能够吃掉它
                        result.append((row, col - i))
            # 右边位置没有越界且没有遇到任何一个棋子
            if not right_stop and col + i <= 8:
                if chessmap[row][col + i][0] is None:
                    # 如果没有棋子,则将当前位置组成一个元组，添加到列表
                    result.append((row, col + i))
                else:
                    right_stop = True
                    if chessmap[row][col + i][0] != camp:
                        # 如果当前位置有棋子，那么就判断是否能够吃掉它
                        result.append((row, col + i))

        # 一列
        up_stop = False
        down_stoop = False
        for i in range(1, 10):
            # 上边位置没有越界且没有遇到任何一个棋子
            if not up_stop and row - i >= 0:
                if chessmap[row - i][col][0] is None:
                    # 如果没有棋子,则将当前位置组成一个元组，添加到列表
                    result.append((row - i, col))
                else:
                    up_stop = True
                    if chessmap[row - i][col][0] != camp:
                        # 如果当前位置有棋子，那么就判断是否能够吃掉它
                        result.append((row - i, col))
            # 下边位置没有越界且没有遇到任何一个棋子
            if not down_stoop and row + i <= 9:
                if chessmap[row + i][col][0] is None:
                    # 如果没有棋子,则将当前位置组成一个元组，添加到列表
                    result.append((row + i, col))
                else:
                    down_stoop = True
                    if chessmap[row + i][col][0] != camp:
                        # 如果当前位置有棋子，那么就判断是否能够吃掉它
                        result.append((row + i, col))
    elif name == "p":  # 炮
        # 一行
        direction_left_chess_num = 0
        direction_right_chess_num = 0
        for i in range(1, 9):
            # 计算当前行中，棋子左边与右边可以落子的位置
            # 左边位置没有越界
            if direction_left_chess_num >= 0 and col - i >= 0:
                if chessmap[row][col - i][0] is None and direction_left_chess_num == 0:
                    # 如果没有棋子,则将当前位置组成一个元组，添加到列表
                    result.append((row, col - i))
                elif chessmap[row][col - i][0] is not None:
                    # 如果当前位置有棋子，那么就判断是否能够吃掉它
                    direction_left_chess_num += 1
                    if direction_left_chess_num == 2 and chessmap[row][col - i][0] != camp:
                        result.append((row, col - i))
                        direction_left_chess_num = -1  # 让其不能够在下次for循环时再次判断
            # 右边位置没有越界
            if direction_right_chess_num >= 0 and col + i <= 8:
                if chessmap[row][col + i][0] is None and direction_right_chess_num == 0:
                    # 如果没有棋子,则将当前位置组成一个元组，添加到列表
                    result.append((row, col + i))
                elif chessmap[row][col + i][0] is not None:
                    # 如果当前位置有棋子，那么就判断是否能够吃掉它
                    direction_right_chess_num += 1
                    if direction_right_chess_num == 2 and chessmap[row][col + i][0] != camp:
                        result.append((row, col + i))
                        direction_right_chess_num = -1
        # 一列
        direction_up_chess_num = 0
        direction_down_chess_num = 0
        for i in range(1, 10):  # 这样就让i从1开始，而不是从0
            # 计算当前列中，棋子上边与下边可以落子的位置
            # 上边位置没有越界
            if direction_up_chess_num >= 0 and row - i >= 0:
                if chessmap[row - i][col][0] is None and direction_up_chess_num == 0:
                    # 如果没有棋子,则将当前位置组成一个元组，添加到列表
                    result.append((row - i, col))
                elif chessmap[row - i][col][0] is not None:
                    # 如果当前位置有棋子，那么就判断是否能够吃掉它
                    direction_up_chess_num += 1
                    if direction_up_chess_num == 2 and chessmap[row - i][col][0] != camp:
                        result.append((row - i, col))
                        direction_up_chess_num = -1

            # 下边位置没有越界
            if direction_down_chess_num >= 0 and row + i <= 9:
                if chessmap[row + i][col][0] is None and direction_down_chess_num == 0:
                    # 如果没有棋子,则将当前位置组成一个元组，添加到列表
                    result.append((row + i, col))
                elif chessmap[row + i][col][0] is not None:
                    # 如果当前位置有棋子，那么就判断是否能够吃掉它
                    direction_down_chess_num += 1
                    if direction_down_chess_num == 2 and chessmap[row + i][col][0] != camp:
                        result.append((row + i, col))
                        direction_down_chess_num = -1

    return result

def generate_possbile_steps(chessmap, camp: str):
    result = []
    src_pos_li = fetch_camp_chess(chessmap, camp)
    for src_pos in src_pos_li:
        for dst_pos in generate_possbile_dest(chessmap, src_pos):
            result.append((src_pos, dst_pos))
    return result

def make_nxt_state(chessmap, src, dst):
    new_map = deepcopy(chessmap)
    new_map[dst[0]][dst[1]] = chessmap[src[0]][src[1]]
    new_map[src[0]][src[1]] = (None, None)
    return new_map

def show(chessmap):
    result = ""
    for line in chessmap:
        for chess in line:
            if chess[0] is None:
                result += "空"
            else:
                if chess[0] == 'r':
                    result += "\x1b[33m"
                else:
                    result += "\x1b[36m"
                match chess:
                    case ('r', 'z'): result += "兵"
                    case ('b', 'z'): result += "卒"
                    case ('r', 'j'): result += "帅"
                    case ('b', 'j'): result += "将"
                    case ('r', 's'): result += "仕"
                    case ('b', 's'): result += "士"
                    case ('r', 'x'): result += "相"
                    case ('b', 'x'): result += "象"
                    case ('r', 'p'): result += "炮"
                    case ('b', 'p'): result += "砲"
                    case (_, 'm'): result += "马"
                    case (_, 'c'): result += "车"
            result += "\x1b[0m"
        result += '\n'
    print(result)
