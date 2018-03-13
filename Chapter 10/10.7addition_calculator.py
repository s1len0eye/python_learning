while True:
    num1 = input("Enter number one('q' to exit): ")
    if num1 == 'q':
        break
    num2 = input("Enter number two('q' to exit): ")
    if num2 == 'q':
        break

    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:  #注意这里，题目说是TypeError,但是我运行的时候是ValueError
        msg = "You should enter number instead text.\n"
        print(msg)
    else:
        sum = num1 + num2
        print(str(sum))
