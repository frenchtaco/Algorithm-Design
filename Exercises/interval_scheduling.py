class Range: 
    def __init__(self, head: list[int], body: list[int], feet: list[int]):
        self.head = head
        self.body = body 
        self.feet = feet


def create_range(s: int, f: int) -> Range: 
    body = []
    for i in range((s+1),f): 
        body.append(i)
    
    r: Range = Range(
        [s],
        body,
        [f]
    )
    return r

def calculate_max_intervals(ranges: list[Range]) -> int: 
    ult_max: int = 1
    for i in ranges: 
        max:int = 0
        for j in ranges: 
            
            if i.feet >= j.head:
                max += 1
        if max > ult_max:
            ult_max = max + ult_max
    return ult_max

def main():
    n = int(input())
    ranges: list[Range] = []
    
    for i in range(n): 
        s, f = [int(i) for i in input().split()]
        r: Range = create_range(s,f)
        ranges.append(r)
    
    max = calculate_max_intervals(ranges)
    print(max)

if __name__=="__main__":
    main()