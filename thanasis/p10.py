import sys

def parse_input():
    with open(sys.argv[1], 'r') as file:
        readings = file.read().splitlines()
        return readings

def ex1(readings):
    ans = 0
    openings = ['(', '[', '{', '<']
    closings = [')', ']', '}', '>']
    scores = [3, 57, 1197, 25137]
    pairs = {openings[i] : closings[i] for i in range(len(openings))}
    scores = {closings[i] : scores[i] for i in range(len(closings))}
    incomplete_lines = []
    for reading in readings:
        expected_closings = []
        incomplete_line_flag = True
        for char in reading:
            if char in openings:
                expected_closings.append(pairs[char])
            else:
                expected_closing = expected_closings.pop()
                if expected_closing != char:
                    ans += scores[char]
                    incomplete_line_flag = False
                    break
        if incomplete_line_flag:
            incomplete_lines.append(expected_closings[::-1])
    return ans, incomplete_lines

def ex2(lines):
    scores = [1, 2, 3, 4]
    closings = [')', ']', '}', '>']
    scores = {closings[i] : scores[i] for i in range(len(closings))}
    final_scores = []
    for line in lines:
        line_score = 0
        for char in line:
            line_score *= 5
            line_score += scores[char]
        final_scores.append(line_score)
    return sorted(final_scores)[len(final_scores)//2]

if __name__ == "__main__":
    readings = parse_input()
    ans, incomplete_lines = ex1(readings)
    print(ans)
    print(ex2(incomplete_lines))