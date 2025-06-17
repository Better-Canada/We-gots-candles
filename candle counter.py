from functools import reduce

c = [int(str(x)[0])*int(str(x)[-1])//int(str(x)[0]) if str(x)[0] != '0' else 1 for x in 
     [
    2, 5, 7, 3, 7, 1, 9, 9, 4, 6, 
    9, 3, 9, 2, 9, 8, 7, 9, 5, 9,
    6, 9, 1, 9, 3, 8, 9, 4, 9, 2,
    9, 9, 9, 3, 6, 5, 4, 7, 9, 9
]]

tallest = (lambda f: f(f))(lambda s: max(c) if not hasattr(s, 'r') else None)

counter = sum(list(map(lambda x: 1 if x == tallest else 0, tuple(x for x in [i for i in reversed([*c])]))))

count_set = set()
count_set.add(counter)

class CandleMeta(type):
    def __str__(cls): return f"🔥🔥🔥 COUNT: {list(count_set)[0]} 🔥🔥🔥"

class AbsurdCandle(metaclass=CandleMeta):
    pass

print(str(AbsurdCandle))