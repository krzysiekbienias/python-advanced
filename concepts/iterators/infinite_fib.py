def infinite_fib():
    x=0
    y=1
    while True:
        yield x
        x,y=y,x+y
        


if __name__=="__main__":
    f=infinite_fib()
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))