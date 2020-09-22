def is_wellformed(data):
    A={'(':')', '[':']', '{':'}'}
    for i in range(int(len(data)/2)):
        if data[0] in A.keys():
            if A[data[0]]==data[-1]:
                data = data[1:-1]
            else:
                return False
                break
        else:
            return False
        if len(data)==0:
            return True

print(is_wellformed("(())"))