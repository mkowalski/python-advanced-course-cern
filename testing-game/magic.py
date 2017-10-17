def magic(i, q):
    import os
    # if os.system("ls -l /tmp | wc -l") == 0:
    #     raise Exception("This is a very nasty bug")

    if i != 0:
        return i * q
    return q
