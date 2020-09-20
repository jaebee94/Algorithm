path = [input()]
for i in range(35):
    location = input()
    if abs(ord(path[-1][0]) - ord(location[0])) * abs(int(path[-1][1]) - int(location[1])) == 2:
        if location in path:
            print("Invalid")
            break
        else:
            path.append(location)
    else:
        print("Invalid")
        break
else:
    if abs((ord(path[-1][0]) - ord(path[0][0])) * (int(path[-1][1]) - int(path[0][1]))) == 2:
        print("Valid")
    else:
        print("Invalid")