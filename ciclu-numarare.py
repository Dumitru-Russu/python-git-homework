
start_n= int(input("Introduceti primul numar: "))
end_n= int(input("Introduceti al doilea numar: "))


if start_n < end_n:
    while start_n <= end_n:
        print(start_n)
        start_n += 1
else:
    while start_n >= end_n:
        print(start_n)
        start_n -= 1