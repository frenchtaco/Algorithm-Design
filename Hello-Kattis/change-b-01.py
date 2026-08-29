def b_to01(text: list) -> str:
    ctr = 1
    retlist = []
    for i in text:
        if i == "b" and ctr % 2  == 0:
            i = str(1)
            ctr += 1
        elif i == "b" and ctr % 2 == 1:
            i = str(0)
            ctr += 1
        
        retlist.append(i)
    return "".join(retlist)

def main():  
    text: list = list(input())
    lst = b_to01(text)
    print(lst)
    

if __name__=="__main__":

    
    main()
