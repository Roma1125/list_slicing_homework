def main(list1,n):
    """
    A list of several elements is given. Return all items from end n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    x=list1[::-1]

    

    return x[::n]
print(main([1,2,3,4,5,6,7],-1))   