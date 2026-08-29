
def smaller_bigger_equal(first, second) -> str:
    if first > second: 
        return "Bigger"
    elif first < second:
        return "Smaller"
    else: 
        return "Equal"

def find_median(my_arr) -> int:
    my_arr = my_arr[:3]
    median = int(sorted(my_arr)[1])
    return median

def add_arr(my_arr) -> str:
    ctr = 0
    for i in my_arr:
        ctr = ctr + int(i)
    return str(ctr)

def add_even(my_arr) -> str:
    newlist = []
    for i in my_arr:
        if int(i) % 2 == 0:
            newlist.append(i)
    return add_arr(newlist)

def map_stuff(my_arr) -> str:
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    word = []
    for idx, val in enumerate(my_arr):
        index = int(val) % 26
        word.append(alphabet[index])
    word = "".join(word)
    return word

def cyclic(my_arr) -> str:
    for idx, (val) in enumerate(my_arr):
        if int(val) > len(my_arr):
            return "Out" 
        else: 
            newVal = my_arr[int(val)]
            if int(newVal) < int(val):
                return "Cyclic"
            else: 
                return "Done"


def handle_instruction(my_arr, cmd): 
    match cmd: 
        case 1:
            print("7")
        case 2: 
            first = int(my_arr[0])
            second = int(my_arr[1])
            print(smaller_bigger_equal(first, second))
        case 3: 
            print(find_median(my_arr))
        case 4:
            print(add_arr(my_arr))
        case 5:
            print(add_even(my_arr))
        case 6:
            print(map_stuff(my_arr))
        case 7: 
            print(cyclic(my_arr))

def main():  
    arr_size, cmd = input().split(" ")
    arr_size: int = int(arr_size)
    cmd: int = int(cmd)


    my_arr:list = list(input().split())
    handle_instruction(my_arr, cmd)

if __name__=="__main__":

    
    main()
