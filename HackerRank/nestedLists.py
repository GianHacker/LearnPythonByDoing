if __name__ == "__main__":
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])

    rd = dict(records)
    grades = []
    for key in rd:
        grades.append(rd[key])

    m = min(grades)
    print(m)
    print(grades)
    grades.sort()

    for i in grades:
        if m < i:
            m = i
            break
        else:
            continue
    print(m)
    ct = grades.count(m)
    print(ct)
    names = []
    for key in rd:
        if m == rd[key]:
            names.append(key)
        else:
            continue
    names.sort()
    for i in names:
        print(i)





    

