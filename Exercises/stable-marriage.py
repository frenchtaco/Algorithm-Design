"""
4 3
A a
B a b
a A B
b B
"""
def find_stable_match(p, r): 
    print("")
def split(lst: list):
    half: int = len(lst) // 2
    return lst[:half], lst[half:]




def main():
    print(" ")
    n_and_m = input()
    n, m = n_and_m.split(" ")

    p_and_preferences = ("", [])
    r_and_preferences = ("", [])

    full_list = []    
    for i in range(int(n)):
        line = input().split()
        lst = list(line)
        x_and_pref: tuple[str, list[str]] = (lst[0], lst[1:])
        print(x_and_pref)
        full_list.append(x_and_pref)

    p, r = split(full_list)
    
    result = find_stable_match(p, r)
        
        

 
    #p, r = split(full_list)

        

if __name__=="__main__":
    main()

