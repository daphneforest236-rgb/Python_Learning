# def get_formatted_name(first, last): 
#     """Generate a neatly formatted full name.""" 
#     full_name = first + ' ' + last 
#     return full_name.title()


# #不能通过的测试
# def get_formatted_name(first, last): 
#     full_name = first + ' ' + middle + ' ' + last 
#     return full_name.title()


#将中间名设置为可选的
def get_formatted_name(first, last): 
    if middle:
        full_name = first + ' ' + middle + ' ' + last 
    else:
        full_name = first + ' ' + last 
    return full_name.title()