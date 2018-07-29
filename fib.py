def produceFibsList(n):
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''
    fibs = [1,1]
    # TODO = fill in the code here, and return the correct result using the return keyword
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    for i in range(n-2):
       fibs.append(fibs[-1]+ fibs[-2])
    return (fibs)
'''
    if n == 2:
        return [1,1]
    if n == 3:
        return [1,1,2]
    if n == 5:
        return [1,1,2,3,5]
'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
