#Day 55 - Helper
class EmptyListError(Exception):
    pass

def get_first(lst):
    if not lst:
        raise EmptyListError("List is empty")
    return lst[0]

try:
    print(get_first([]))
except EmptyListError as e:
    print(e)