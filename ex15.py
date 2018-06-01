'''
More generally: given two speeds v1 (A's speed, integer > 0) and v2 (B's speed, integer > 0) and a lead g (integer > 0)
how long will it take B to catch A?

The result will be an array [hour, min, sec] which is the time needed in hours, minutes and seconds (round down to the
nearest second) or a string in some languages.

If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for C++, C, Go, Nim, [] for Kotlin or "-1 -1 -1".
'''


def race(v1, v2, g):
    # Sucky Exercise
    out = []
    if v1 >= v2:
        return None
    else:
        t = g / (v2 - v1)
        hour = str(t).split('.')

        f = float('.' + hour[1])
        m = f * 60
        minute = str(m).split('.')

        f = float('0.' + minute[1])
        s = f * 60
        sec = str(s).split('.')

        out.append(int(hour[0]))
        out.append(int(minute[0]))
        out.append(int(sec[0]))

        return out


def main():
    print(race(720, 850, 70))

if __name__ == '__main__': main()