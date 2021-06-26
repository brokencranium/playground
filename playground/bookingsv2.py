import os
import sys


def get_booked_start_end_hours(hour_sequence: list) -> list:
    booked_start_end_hours = []
    for start, end in ((hour_sequence[i], hour_sequence[i + 1])
                       for i in range(0, len(hour_sequence) - 1, 2)):
        booked_start_end_hours.append((start, end))

    return sorted(set(booked_start_end_hours))


def explode_booked_hours(booked_hours: list) -> list:
    exploded_hours = []
    for booked_hour in booked_hours:
        exploded_hours.extend(list(range(booked_hour[0], booked_hour[1])))

    return sorted(set(exploded_hours))


def next_meeting(now, length, schedules):
    """
    Determines the next available start time for a new meeting
    :param now: The current time as an integer
    :param length: The length of the new meeting to schedule as an integer
    :param schedules: The list of schedules, where each schedule is a list of integers that represent alternating start, end meeting times
    :return: The start of the next available meeting time
    :rtype: int 1 1 1 2 4 5 6 7 3 4 8 9 2 3 7 8 [[1,2,4,5,6,7], [3,4,8,9], [2,3,7,8]]
    """
    open_start_hours = set()
    booked_start_end_hours = []

    for schedule in schedules:
        booked_start_end_hours.extend(get_booked_start_end_hours(schedule))

    booked_hours = sorted(set(booked_start_end_hours))
    exploded_hours = explode_booked_hours(booked_hours)

    if now + length <= exploded_hours[0]:
        return now

    for index in range(len(exploded_hours) - 1):
        curr_start_hour = exploded_hours[index]
        next_start_hour = exploded_hours[index + 1]
        if curr_start_hour < now:
            continue

        if curr_start_hour + 1 + length <= next_start_hour:
            return curr_start_hour + 1
    else:
        return exploded_hours[-1] + 1


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
