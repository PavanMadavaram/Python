# Day 7 Helper
def tuple_info(tup):
    print(f"Tuple length: {len(tup)}")
    print(f"First: {tup[0]}")
    return len(tup)

def get_movies():
    return ("Bahubali", "RRR", "Pushpa")

movies = get_movies()
tuple_info(movies)
