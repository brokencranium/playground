import os
import sys

MIN_HOUR = 0
MAX_HOUR = None


def get_max_hour(schedules: list) -> int:
    if len(schedules):
        return (max(map(max, schedules)))
    return 0


def get_booked_start_end_hours(hour_sequence: list) -> list:
    booked_start_end_hours = []
    for start, end in ((hour_sequence[i], hour_sequence[i + 1])
                       for i in range(0, len(hour_sequence) - 1, 2)):
        booked_start_end_hours.append((start, end))

    booked_start_end_hours.append((MIN_HOUR, MIN_HOUR))
    booked_start_end_hours.append((MAX_HOUR, MAX_HOUR))
    return sorted(set(booked_start_end_hours))


def get_start_hours(start_hour: int, end_hour: int, duration: int) -> list:
    start_hours = [hour for hour in range(start_hour, end_hour) if hour + duration <= end_hour]
    return start_hours


def get_open_start_hours(booked_start_end_hours: list, duration: int) -> set:
    open_start_hours = set()
    for start, end in ((booked_start_end_hours[i][1], booked_start_end_hours[i + 1][0])
                       for i in range(len(booked_start_end_hours) - 1)):
        print("Open Hour Block", start, end)

        if end - start >= duration:
            open_start_hours.update(get_start_hours(start, end, duration))

    print("Open Start Hours: ", open_start_hours)
    return open_start_hours


def next_meeting(now, length, schedules):
    """
    Determines the next available start time for a new meeting
    :param now: The current time as an integer
    :param length: The length of the new meeting to schedule as an integer
    :param schedules: The list of schedules, where each schedule is a list of integers that represent alternating start, end meeting times
    :return: The start of the next available meeting time
    :rtype: int 1 1 1 2 4 5 6 7 3 4 8 9 2 3 7 8 [[1,2,4,5,6,7], [3,4,8,9], [2,3,7,8]]
    """
    global MAX_HOUR

    open_start_hours = set()
    MAX_HOUR = get_max_hour(schedules) + length

    for schedule in schedules:
        booked_start_end_hours = get_booked_start_end_hours(schedule)
        print("Booked Start Hours", booked_start_end_hours)

        if not len(open_start_hours):
            open_start_hours = get_open_start_hours(booked_start_end_hours, length)
        else:
            open_start_hours = open_start_hours & get_open_start_hours(booked_start_end_hours, length)

        print("Hours intersection", open_start_hours)

    open_hours = sorted(open_start_hours)
    if len(open_hours):
        return next(x for x in open_hours if x >= now)
    else:
        return -1


def main():
    now = int(input().strip())
    length = int(input().strip())

    schedules = []
    while True:
        schedule = sys.stdin.readline()
        if not schedule:
            break
        schedules.append([int(v) for v in schedule.strip().split()])

    return schedules
    # with open(os.environ['OUTPUT_PATH'], 'w') as output:
    #     print(next_meeting(now, length, schedules), file=output)


if __name__ == '__main__':
    # schedules = main()

    schedules = [[1, 2, 4, 5, 6, 7], [3, 4, 8, 9], [2, 3, 7, 8]]
    assert 5 == next_meeting(1, 1, schedules)

    schedules = [[4, 5], [2, 3]]
    assert 1 == next_meeting(1, 1, schedules)

    schedules = [[0, 2, 2, 3, 4, 5]]
    assert 3 == next_meeting(1, 1, schedules)

    schedules = [[0, 3, 4, 6], [2, 5, 7, 8]]
    assert 6 == next_meeting(0, 1, schedules)

    schedules = [[7, 8, 1, 2, 3, 4, 2, 3], [5, 6, 4, 5]]
    assert 6 == next_meeting(1, 1, schedules)

    schedules = [[1, 2, 7, 10], [3, 4, 8, 9], [5, 6]]
    assert 10 == next_meeting(1, 2, schedules)

    schedules = [[1, 2], [6, 7]]
    assert 2 == next_meeting(1, 2, schedules)

    schedules = [[2, 3], [1, 2], [3, 4], [7, 8], [4, 5], [1, 2]]
    assert 5 == next_meeting(1, 1, schedules)

    schedules = [[1, 4, 8, 9], [2, 3, 5, 6], [2, 3, 7, 8]]
    result = next_meeting(0, 2, schedules)
