'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

'''


def make_readable(num):
    hours = str(int(num / 3600));
    minutes = str(int((num % 3600) / 60));
    seconds = str(int((num % 3600) % 60));

    if len(seconds) == 1:
        seconds = "0" + seconds


    if len(minutes) == 1:
        minutes = "0" + minutes


    if len(hours) == 1:
        hours = "0" + hours

    return hours + ":" + minutes + ":" + seconds;


def main():
    print(make_readable(34))

if __name__ == '__main__': main()