def camelcase(s):
    # Complete this function
    count = 1
    for i in s:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            count += 1
    return count

if __name__ == "__main__":
    s = input()
    result = camelcase(s)
    print (result)
