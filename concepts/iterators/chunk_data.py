def chunker (data,size):
    i=0
    while size<len(data):
        chunk= data[i:i+size]
        i=i+size
        yield chunk

if __name__=="__main__":
    data = [1, 2, 3, 4, 5, 6, 7]
    chu=chunker(data,3)
    print(next(chu))
    print(next(chu))
    print(next(chu))