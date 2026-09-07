

def print_dict(l: dict) -> str:
    for k, v in l.items():
        print(f"{k}: {v}")

def case_5_(lst: list[int]) -> str:
    new_list:list[int] = []
    for i in lst:
        if i > 99 and i < 1000: 
            new_list.append(i)
    new_list.sort()
    retval: str = " ".join(str(i) for i in new_list)
    print(retval)
    return retval

def case_4_(lst: list[int], n: int) -> str:
    n = len(lst) / 2
    lst.sort()

    if n % 2 == 0:
        val1: int = int(n-0.5)
        val2: int = int(n + 0.5)
        print(lst[val1], lst[val2])
        return (lst[val1], lst[val2])
        
    else: 
        print(lst[int(n)])
        return lst[int(n)]




def case_3_(lst: list[int], n: int) -> str:
    half = n / 2
    count = {}

    best: tuple[int, int] = (0,0)

    for i in lst: 
        count[i] = 0
    
    for i in lst: 
        if i in count.keys():
            count[i] += 1
        else:
            count[i] = 1
    
    for k, v in count.items(): 
        if best[1] < v: 
            best = k,v 
        else: 
            continue

    if best[1] > half:
        print(best[0])
        return best[0]
    else:
        print(-1)


    return ""
def case_2_(lst: list[int], t: int) -> str:
    "Check if a list contains unique elements or not"
    myset = set()
    for i in lst:
        myset.add(i)
    if len(myset) != len(lst): 
        print("Contains duplicates")
        return "Contains duplicates"
    else: 
        print("Unique")
        return "Unique"


def case_1_(lst: list[int], t: int) -> str: 
    "Check if there is num x,y such that x != y and x+y == 7777 "
    sorted_lst = sorted(lst)
    nest_lst = sorted_lst

    for i in sorted_lst:
        complement = 7777 - abs(i)
        for j in nest_lst: 
            if (i +  complement) == 7777 and i != complement:
                print("Yes")
                return "Yes"
            else: 
                continue
    print("No")
    return "No"
            

def handle_lst(lst: list[int], n: int, t: int): 
    match t:
        case 1: return case_1_(lst, t)
        case 2: return case_2_(lst, t)
        case 3: return case_3_(lst, n)
        case 4: return case_4_(lst, n)  
        case 5: return case_5_(lst)  

def main():
    ## HANDLE JUST INPUTS
    n, t = [int(x) for x in input().split()]
    lines: list[int] = [int(i) for i in input().split()]
    
    handle_lst(lines, n, t)


if __name__ == main():
    main()