
"""
This function does... well, it gives all subsets via bit shifting. This was provided in class
"""
def find_all_subsets(n):
    subsets = []
    for k in range(1 << n):
        subset = [i for i in range(n) if k >> i & 1]
        subsets.append(subset)

        
    return subsets

def perket(lst, all_subsets):

    best = 1000000000 #Want to go as low as posible, so we set it to a high number first, named in the hand-in to be one billy.
    
    for p in all_subsets: #iter over all subsets which is indexes
        t_sourness   = 1
        t_bitterness = 0

        for i in p: 
            # We must not use the empty set, as that would mess with our results
            if p == []:
                continue
            else: 
                s, b = lst[i] # fetch s,b from our list of pairs
                t_sourness = t_sourness * s #multiply it
                t_bitterness = t_bitterness + b
            
                difference = t_bitterness - t_sourness
                difference = abs(difference)
                if difference < best:
                    best = difference
    return best

def main():  
    list_of_ingredients = []
    lines = int(input()) #Ingredient amount

    ## Here, we just store the ingredients we get in a list of pairs.
    for i in range(lines):
        s, b = input().split(" ")
        s = int(s)
        b = int(b)
        list_of_ingredients.append(tuple((s,b)))
    
    ## The amount of subsets is determined by the amount of ingredients, thus we pass that in here as well.
    all_subsets = find_all_subsets(lines)

    best = perket(list_of_ingredients, all_subsets)
    print(best)
    

if __name__=="__main__":
    main()


"""
4
1 7
2 6
3 8
4 9
   
   30
"""