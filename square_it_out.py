def square_it_out():
    start=int(input("Enter the start of the range: "))
    end=int(input("Enter the end of the range: "))
    square_values=[]
    for num in range(start, end+1):
        square_values.append(num**2)
    even_squares=[]
    odd_squares=[]
    for value in square_values:
        if value%2==0:
            even_squares.append(value)
        else:
            odd_squares.append(value)

    print("All Square Values:", square_values)
    print("Even Square Values:", even_squares)
    print("Odd Square Values:", odd_squares)

square_it_out()