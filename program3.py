if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    m=max(arr)
    while max(arr)==m:
        arr.remove(max(arr))
    print(max(arr))