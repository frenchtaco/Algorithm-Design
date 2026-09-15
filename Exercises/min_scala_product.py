import sys


def calc_scalar_product(v1: list[int], v2: list[int]) -> int: 
    scalar_product: int = sys.maxsize
    #permutations_v2 = list(itertools.permutations(v2))
    #permutations_v1 = list(itertools.permutations(v1))
    
    # or did your very first hand-worked example (sort one ascending, the other descending, pair them up)
    v1.sort()
    v2.sort(reverse=True)

    scal_prod: int = 0 
    for n, m in zip(v1,v2): 
        scal_prod += n * m 

        
        
        
    if scal_prod < scalar_product:
        scalar_product = scal_prod



    """
    This works but is too slow

    for tup in permutations_v2: 
        scal_prod: int = 0 
        for i, val in enumerate(v1):
            scal_prod += tup[i] * val
        if scal_prod < scalar_product:
            scalar_product = scal_prod
    """



    return scalar_product

def main():
    no_test_cases = int(input())

    min_scala_prod: int = sys.maxsize
    curr_case = 1
    for i in range(no_test_cases):    
        no_ints = int(input())
        v1: list[int] = [int(i) for i in input().split()]
        v2: list[int] = [int(x) for x in input().split()]

        scalar_product: int = calc_scalar_product(v1, v2)
 
        min_scala_prod = calc_scalar_product(v1, v2)
        print(f"Case #{curr_case}: {min_scala_prod}")
        curr_case += 1    

if __name__=="__main__":
    main()


"""
1 3 -5
-2 4 1

1 2 3 4 5
1 0 1 0 1
"""