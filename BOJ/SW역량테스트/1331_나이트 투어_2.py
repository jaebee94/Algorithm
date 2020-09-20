path = [input()]
for i in range(36):
    if i == 35:
        location = path[0]
    else:
        location = input()
        if location in path:
            print("Invalid")
            break
    if abs((ord(path[-1][0]) - ord(location[0])) * (int(path[-1][1]) - int(location[1]))) == 2:
        path.append(location)
    else:
        print("Invalid")
        break
else:
    print("Valid")