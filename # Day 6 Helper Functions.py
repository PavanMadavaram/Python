# Day 6 Helper Functions
def list_info(my_list):
    print("Length:", len(my_list))
    print("First:", my_list[0] if my_list else "Empty")
    return len(my_list)

def add_item(lst, item):
    lst.append(item)
    return lst

shopping = ["rice", "dal"]
print("Shopping before:", shopping)
add_item(shopping, "oil")
print("Shopping after:", shopping)
