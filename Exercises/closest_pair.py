import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Closest:
    def __init__(self, one: Point, two: Point, distance: float):
        self.one = one
        self.two = two
        self.distance = distance

def distance(point1: Point, point2: Point) -> float: 
    x = abs(point1.x - point2.x) 
    y = abs(point1.y - point2.y)
    return math.sqrt((x**2) + (y**2))



#This shit blows and is not used
def sub_task_1(lst: list[Point]) -> Closest: 
    """ Consider the x-coordinate solely"""
    closest_pairs: list[Point] = []
    closest: Closest = Closest(Point(1000000.0, 1000000.0), Point(1000000.0,1000000.0), 1000000.0)

    for p in lst: 
        for m in lst: 
            if p == m:
                continue
            distance = p.x - m.x if m.x < p.x else m.x - p.x
            if distance < closest.distance:
                closest = Closest(p, m, distance)
    
    return closest


def recurse(lst: list[Point]) -> Closest: 
    if len(lst) == 2: 
        dist: float = distance(lst[0], lst[1])
        return Closest(lst[0], lst[1], dist)
    
    if len(lst) == 3: 
        dist1: float = distance(lst[0], lst[1])
        dist2: float = distance(lst[0], lst[2])
        dist3: float = distance(lst[1], lst[2])
        
        if dist1 <= dist2 and dist1 <= dist3: return Closest(lst[0], lst[1], dist1)
        elif dist2 <= dist3: return Closest(lst[0], lst[2], dist2)
        else: return Closest(lst[1], lst[2], dist3)


    #Splitting recursively
    
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    mid_point = lst[mid]


    left_side: Closest = recurse(left)
    right_side: Closest = recurse(right)

    best: Closest = left_side if left_side.distance < right_side.distance else right_side

    closest_points: list[Point] = []

    #building up lists for our split 
    for i in range(len(lst)): 
        curr_point: Point = lst[i]
        dist_to_mid: float = abs(mid_point.x - curr_point.x)
        if dist_to_mid <= best.distance:
            closest_points.append(lst[i])

    # sorting it: 
    closest_points.sort(key = lambda p: p.y)

    for i in range(len(closest_points)): 
        curr: Point = closest_points[i]
        for j in range(i + 1, len(closest_points)):
            comp: Point = closest_points[j]

            if (comp.y - curr.y) >= best.distance:
                break

            dista: float = distance(curr, comp)
            if dista < best.distance:
                best: Closest = Closest(curr, comp, dista)
    
    return best
    ## STRIP LOGIC
def sort_by_x(lst: list[Point]) -> Closest: 
    lst.sort(key=lambda p: p.x)

    closest = recurse(lst)
    return closest







def main():
    no_points = int(input())

    point_list: list[Point] = []
    for i in range(no_points):
        xx,yy = [float(i) for i in input().split()]
        
        point_list.append(Point(xx,yy))


    
    closest: Closest = sort_by_x(point_list)

    print(f"{closest.one.x} {closest.one.y}")
    print(f"{closest.two.x} {closest.two.y}")
    

if __name__=="__main__":
    main()