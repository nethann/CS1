interstate_num = int(input("Please enter a interstate number: "))

if interstate_num > 0: 
    if 1 <= interstate_num <= 99: 
        if interstate_num % 2 == 0: 
            print(f"I-{interstate_num} is primary, going east/west")
        else: 
            print(f"I-{interstate_num} is primary, going north/south")
    elif 100 <= interstate_num <= 999: 
        primary_num = interstate_num % 100
        if primary_num != 0: 
            if interstate_num % 2 == 0: 
                print(f'I-{interstate_num} is auxilitary, serving I-{primary_num}, going east/west')
            else: 
                print(f'I-{interstate_num} is auxilitary, serving I-{primary_num}, going north/south')
        else:
            print(f'{interstate_num} is not a valid highway number')
    else: 
            print(f'{interstate_num} is not a valid highway number')



