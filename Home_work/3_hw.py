def print_max(a,b)->None:
    if a>b:
        print(a)
    elif a<b:
        print(b)
    else:
        print('Числа равны')
print_max(10,5)


def print_yes_no(a,b)->None:
    if a-b==135:
        print('yes')
    elif b-a==135:
        print('yes')
    else:
        print('no')
print_yes_no(1,136)

def print_season(month:int)->None:
    if month<1:
        print('неверно задан месяц')
    elif month<=2 or month==12:
        print('зима')
    elif month<=5:
        print('весна')
    elif month<=8:
        print('лето')
    elif month<=11:
        print('oceнь')
    else:
        print('неверно задан месяц')
print_season(5)


def print_yes_no_3(a,b,c)->None:
    if a>10 and b>10 and c>10:
        print('yes')
    else:
        print('no')
print_yes_no_3(11,12,50)


def print_count_positive(list)->None:
    c=0
    if list[0]>0:           c=c+1
    if list[1] > 0:         c = c + 1
    if list[2] > 0:         c = c + 1
    if list[3] > 0:         c = c + 1
    if list[4] > 0:         c = c + 1
    print(c)
print_count_positive([2,8,9,-5,-10])

def print_count_days(year:int, month:int)->None:
    print((year*12+month)*29)
print_count_days(1,2)