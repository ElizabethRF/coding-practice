"""
https://leetcode.com/problems/pascals-triangle-ii/
"""
def get_row(row_index: int) -> list[int]:
    prev = [1]

    for x in range(1, row_index + 1):
        next_len = len(prev) + 1
        new = []
        for y in range(next_len):
            val = 0
            if y - 1 >= 0:
                val += prev[y - 1]
            if y < len(prev):
                val += prev[y]
            new.append(val)
        prev = new

    return prev


if __name__ == '__main__':
    tests = [
        3,
        0,
        15
    ]
    for level in tests:
        print(get_row(level))