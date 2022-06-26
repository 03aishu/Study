
def check(x):
    x = int(input("enter a no: "))
    if x == 2:
        raise Exception('I know Python!')
    if x == 3:
        raise ValueError("the number is 3")

if __name__ == '__main__':
    try:
        check(3)
    except Exception as e:
        print(e) 
