def delta(iterable, level):
    def diff(it):
        it = iter(it)
        prev = next(it)
        for x in it:
            yield x - prev
            prev = x

    result = iterable
    for _ in range(level):
        result = diff(result)
    return result

if __name__=="__main__":
    l=[1,2,3,4,5,6]
    print(l)
    it=iter(l)
    print(it)
    prev=next(it)
    print(prev)
    print(next(it))
    print(next(it))