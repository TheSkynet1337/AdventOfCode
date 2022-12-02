from aocd import get_data
import numpy as np


def part1(data):
    matches = data.splitlines()
    matches = [match.split(' ') for match in matches]
    enemy_moves = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
    my_moves = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
    move_scores = {'rock': 1, 'paper': 2, 'scissors': 3}
    score = 0
    for match in matches:
        enemy_move = enemy_moves[match[0]]
        my_move = my_moves[match[1]]
        if enemy_move == my_move:
            score += 3 + move_scores[my_move]
        elif enemy_move == 'rock' and my_move == 'paper':
            score += 6 + move_scores[my_move]
        elif enemy_move == 'rock' and my_move == 'scissors':
            score += 0 + move_scores[my_move]
        elif enemy_move == 'paper' and my_move == 'rock':
            score += 0 + move_scores[my_move]
        elif enemy_move == 'paper' and my_move == 'scissors':
            score += 6 + move_scores[my_move]
        elif enemy_move == 'scissors' and my_move == 'rock':
            score += 6 + move_scores[my_move]
        elif enemy_move == 'scissors' and my_move == 'paper':
            score += 0 + move_scores[my_move]

    print(score)
    return data


def part2(data):
    matches = data.splitlines()
    matches = [match.split(' ') for match in matches]
    enemy_moves = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
    desired_outcome = {'X': 'loss', 'Y': 'draw', 'Z': 'win'}
    move_scores = {'rock': 1, 'paper': 2, 'scissors': 3}
    score = 0
    for match in matches:
        enemy_move = enemy_moves[match[0]]
        my_move = match[1]
        if desired_outcome[my_move] == 'win':
            if enemy_move == 'rock':
                score += 6 + move_scores['paper']
            elif enemy_move == 'paper':
                score += 6 + move_scores['scissors']
            elif enemy_move == 'scissors':
                score += 6 + move_scores['rock']
        elif desired_outcome[my_move] == 'loss':
            if enemy_move == 'rock':
                score += 0 + move_scores['scissors']
            elif enemy_move == 'paper':
                score += 0 + move_scores['rock']
            elif enemy_move == 'scissors':
                score += 0 + move_scores['paper']
        elif desired_outcome[my_move] == 'draw':
            if enemy_move == 'rock':
                score += 3 + move_scores['rock']
            elif enemy_move == 'paper':
                score += 3 + move_scores['paper']
            elif enemy_move == 'scissors':
                score += 3 + move_scores['scissors']
    print(score)
    return data


data = get_data(day=2, year=2022)
part1(data)

part2(data)
