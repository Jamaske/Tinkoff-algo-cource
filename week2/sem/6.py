


def main():
    src = map(int, input().split())
    try:
        result = [next(src)]
    except:
        return

    for val in src:
        if result[-1] != val:
            result.append(val)
        else:
            result.pop()


    print(*result)

main()

#case
# 1 2 3 3 3 4 5 5 6

#result
# 1 2 3 4 6