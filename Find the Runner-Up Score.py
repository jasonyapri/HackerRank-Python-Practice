if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    second_highest = min(arr)
    
    for i in range(n):
        if arr[i] != max(arr) and second_highest < arr[i]:
            second_highest = arr[i]
    
    print(second_highest)
