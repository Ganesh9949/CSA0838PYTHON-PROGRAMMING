def findstep(n):
    if (n==5):
        return 1
    elif (n<0):
        return 0
    else:
        return findstep(n-3)+findstep(n-2)+findstep(n-1)
    n=4
    print("enter number",findstep(n))
