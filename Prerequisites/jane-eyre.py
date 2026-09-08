import re


class annas_pile_book(): 
    title: str
    no_pages: int 

class annas_gift_book(): 
    seconds_to_receive: int 
    title: str 
    no_pages: int 


def print_pile(lst: list[annas_pile_book]): 
    for i in lst: 
        print(f"{i.title}, {i.no_pages} pages. \n")
def print_gifts(lst: list[annas_gift_book]): 
    for i in lst:
        print(f"{i.seconds_to_receive}: {i.title}, {i.no_pages} pages. \n")

def main(): 
    print("Goofy Gooner")

    annas_pile: list[annas_pile_book] = []
    annas_gifts: list[annas_gift_book] = []

    n, m, k = [int(i) for i in input().split()]

    for i in range(n): 
        line = input()
        match = re.search(r'"(.*?)"\s+(\d+)', line)
        name = match.group(1)
        pages = match.group(2)

        book = annas_pile_book()
        book.title = name
        book.no_pages = int(pages)

        annas_pile.append(book)

    for i in range(m): 
        line = input()
        match = re.search(r'(\d+)\s+"(.*?)"\s+(\d+)', line)

        book = annas_gift_book()
        book.seconds_to_receive = match.group(1)
        book.title = match.group(2)
        book.no_pages = match.group(3)

        annas_gifts.append(book)
    print("***")
    print_pile(annas_pile)
    print("--")
    print_gifts(annas_gifts)
    
if __name__ == main():

    main()