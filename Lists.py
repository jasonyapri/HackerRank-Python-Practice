if __name__ == '__main__':
    N = int(input())
    commands = []
    arr = []
    for i in range(N):
        commands.append(input())
    
    for command in commands:
        if 'insert' in command:
            i = int(command.split(' ')[1])
            e = int(command.split(' ')[2])
            arr.insert(i, e)
        elif 'print' in command:
            print(arr)
        elif 'remove' in command:
            e = int(command.split(' ')[1])
            arr.remove(e)
        elif 'append' in command:
            e = int(command.split(' ')[1])
            arr.append(e)
        elif 'sort' in command:
            arr.sort()
        elif 'pop' in command:
            arr.pop()
        elif 'reverse' in command:
            arr.reverse()