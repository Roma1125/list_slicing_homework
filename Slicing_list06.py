def main(list1):
    """A list of several elements is given. Return all items from the beginning in three steps.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    return list1[::3]
print(main([1,2,3,4,55,5,6,7,8],2,5))