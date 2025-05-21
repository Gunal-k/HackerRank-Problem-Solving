def queensAttack(n, k, r_q, c_q, obstacles):
    """
    Calculates the number of squares a queen can attack on an n x n chessboard, given her position and obstacles.
    Args:
        n (int): The size of the chessboard (n x n).
        k (int): The number of obstacles on the board.
        r_q (int): The row position of the queen (1-indexed).
        c_q (int): The column position of the queen (1-indexed).
        obstacles (List[List[int]]): A list of obstacles, each represented as [row, column].
    Returns:
        int: The total number of squares the queen can attack.
    The function considers all 8 possible directions the queen can move (horizontal, vertical, and diagonal)
    and counts the number of squares she can attack, stopping at obstacles or the edge of the board.
    """
    blocked = set(tuple(obstacle) for obstacle in obstacles)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    attackable = 0

    for dr, dc in directions:
        r, c = r_q + dr, c_q + dc
        while 1 <= r <= n and 1 <= c <= n:
            if (r, c) in blocked:
                break
            attackable += 1
            r += dr
            c += dc

    return attackable

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])

    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
