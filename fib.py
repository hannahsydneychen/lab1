#function that returns fibonacci list up to n elements 
def produceFibsList(n):
    fibs = [1,1]
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    for i in range(n-2):
       fibs.append(fibs[-1]+ fibs[-2])
    return (fibs)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
