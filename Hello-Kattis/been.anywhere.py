

def main():  
    test_cases: int = int(input())
    glob_lst = []
    for i in range(test_cases):
        lst = []
        city_amount: int = int(input())
        for i in range(city_amount):
            city = input()
            lst.append(city)
            #print(city)
        lst = set(lst)
        glob_lst.append(lst)
    #print(glob_lst)

    for i in glob_lst:
        print(len(i))
    

if __name__=="__main__":

    
    main()

"""
2
7
saskatoon
toronto
winnipeg
toronto
vancouver
saskatoon
toronto
3
edmonton
edmonton
edmonton

"""