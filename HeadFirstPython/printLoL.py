"""递归处理列表的嵌套问题"""


def print_lol(the_list):
    for itemInList in the_list:
        if isinstance(itemInList, list):
            print_lol(itemInList)
        else:
            print(itemInList)


"""使用递归处理列表，同时根据传入的层数，决定缩进"""
"""level=0，表明了level是一个可选参数，如果不传则使用缺省值0，否则使用传入的值"""


def print_lol2(the_list, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol2(each_item, level + 1)
        else:
            for tab_stop in range(level):
                print('\t', end='')
            print(each_item)


"""使用递归处理列表，根据indent=False或True控制是否缩进，根据传入的层数，决定缩进"""
"""level=0，表明了level是一个可选参数，如果不传则使用缺省值0，否则使用传入的值"""


def print_lol3(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol3(each_item, indent, level + 1)
        else:
            if indent:
                for tab_stop in range(level):
                    print('\t', end='')
            print(each_item)
