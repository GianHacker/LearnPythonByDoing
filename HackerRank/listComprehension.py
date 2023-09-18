if __name__ == "__main__":    
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    i = [i for i in range(0,x+1)]
    j = [j for j in range(0,y+1)]
    k = [k for k in range(0,z+1)]
    
    nl = []
    [nl.append([a,b,c]) for a in i for b in j for c in k if (a+b+c) != n ]
    nl.sort()
    print(nl)