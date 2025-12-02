def main():
    with open('input.txt') as f:
    #with open('example.txt') as f:
        lines = f.readlines()

    global count
    count = 0

    def next(location:int, step:str) -> int:
        global count
        direction = step[0]
        steps = int(step[1:])

        location = location + steps if direction == 'R' else location - steps
        #print("location", location, direction, steps)

        location %=100

        if location >= 100:
            location -= 100
        elif location < 0:
            location += 100

        if location == 0:
            count += 1

        return location

    location = 50
    for line in lines:
        #print(f"{line.strip()}", location)
        location = next(location, line)

    print(count)


if __name__ == '__main__':
    main()
