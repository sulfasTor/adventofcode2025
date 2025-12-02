def main():
    with open('one/python/input.txt') as f:
    #with open('one/python/example.txt') as f:
        lines = f.readlines()

    global count
    count = 0

    def next(location:int, step:str) -> int:
        global count
        direction = 1 if step[0] == 'R' else -1
        steps = int(step[1:])

        start = location
        end = start + direction*steps

        low = min(start, end)
        high = max(start, end)

        count += high//100 - (low-1)//100
        if start % 100 == 0:
            count -= 1

        return end%100

    location = 50
    for line in lines:
        #print(f"{line.strip()}", location)
        location = next(location, line)

    print(count)


if __name__ == '__main__':
    main()
