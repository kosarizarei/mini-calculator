print('Mini Calculation')
print('Enter "=" to see finall result\n')
x = float(input('Number: '))
while True:
    op = input("Operation (+ - * /) or = : ")
    if op == '=':
        print(f"\nResult: {x}")
        break
    elif op not in ['+', '-', '*', '/']:
        print("Invalid operation!")
        continue
    
    y = float(input('Number: '))
    if op == '+':
        x += y
    
    elif op == '-':
        x -= y

    elif op == '*':
        x *= y

    elif op == '/':
        if y == 0:
            print("Division by zero!")
            continue
        x /= y