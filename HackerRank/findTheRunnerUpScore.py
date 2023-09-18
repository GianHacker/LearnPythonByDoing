if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list(arr)
    l.sort()
    l.reverse()
    for i in l:
        if i < max(l):
            print(i)
            break
        else:
            continue