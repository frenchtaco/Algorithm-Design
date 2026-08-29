def backspace(text: list) -> str:
    stack = []
    for i, val in enumerate(text):
        
        if val == "<":
                stack.pop()
        else: 
            stack.append(val)        

    stack = "".join(stack)
    print(stack)
    return stack
    
    

def main():  
    text: list = list(input())
    backspace(text)
    

if __name__=="__main__":
    main()
