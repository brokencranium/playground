def runner_up():
    """
    Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
    You are given  scores. Store them in a list and find the score of the runner-up.
    Input Format
    The first line contains n . The second line contains an array  A[] of n integers each separated by a space.
    5
    2 3 6 6 5
    Constraints
    2<=n<=10
    100<=A[i]<=100
    Output
    5
    """
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr), reverse=True)[1])


def point_range_3d():
    """
    You are given three integers  x, y and z  representing the dimensions of a cuboid along with an integer .
    Print a list of all possible coordinates given by  (i, j, k )on a 3D grid where the sum of i+j+k is not equal to n .
    Here, 0<=i<=x; 0<=j<=y; 0<=k<=z. Please use list comprehensions rather than multiple loops, as a learning exercise.
    """
    x, y, z, n = (int(input()) for _ in range(4))

    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if x + y + z != n]
    print(result)


def second_lowest_grade():
    """
    Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s)
    of any student(s) having the second lowest grade.
    Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name
    on a new line.
    Example
    The ordered list of scores is , so the second lowest score is . There are two students with that score: .
    Ordered alphabetically, the names are printed as:
    alpha
    beta

    Input Format
    The first line contains an integer, N, the number of students.
    The 2N subsequent lines describe each student over 2 lines.
    - The first line contains a student's name.
    - The second line contains their grade.

    Constraints
    . 2<=N<=5
    .There will always be one or more students having the second lowest grade.

    Output Format
    Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students,
    order their names alphabetically and print each one on a new line.

    Sample Input 0
    2
    Harry
    37.21
    Berry
    37.21

    Sample Output 0
    Berry
    Harry
    """
    # records = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 37.21]]
    # scores = (37.21, 37.2, 41, 44, 45)
    records = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.add(score)

    second_lowest = sorted(scores)[1]
    records.sort(key=lambda record: [record[1], record[0]])
    [print(record[0]) for record in filter(lambda x: x[1] == second_lowest, records)]


def run_list_commands():
    """
    insert 0 5
    append 1 1
    pop
    print
    :return:
    """
    N = int(input())
    result = []
    for _ in range(N):
        command, *data = input().split()
        args = tuple(map(int, data))

        if "print" in command:
            print(result)
        else:
            eval(f'result.{command}{args}')
