def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x < 0:
        x = -x
        res = -int(cal_reserve(x))
        return res
    elif x == 0:
        return 0
    else:
        res = int(cal_reserve(x))
        return res
        # mystr = str(x)
        # # print(mystr)
        # mylist = list(mystr)
        # # print(mylist)
        # mylist.reverse()
        # print(mylist)
        #
        # res_str = ''
        # flag = False
        # for i in mylist:
        #     if int(i) != 0 or flag:
        #         flag = True
        #         res_str += i

def cal_reserve(x):

    mystr = str(x)
    # print(mystr)
    mylist = list(mystr)
    # print(mylist)
    mylist.reverse()

    res_str = ''
    flag = False
    for i in mylist:
        if int(i) != 0 or flag:
            flag = True
            res_str += i
    return res_str



print(reverse(0))