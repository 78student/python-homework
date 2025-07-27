def task_1()->None:
    a=2
    print(a, "относится к типу", type(a))

    b=10.002
    print(b, "относится к типу", type(b))

    s="Это строка"
    print(s, type(s))

    d=[1,2,3,4,5]
    print(d, "относится к типу", type(d))

    print(2>1)
    print(2==1)
    print(2<1)

    e=True
    print(e, "относится к типу", type(e))
    if e:
        print('e=True')
    else:
        print('e!=True')

task_1()


def task_2()->None:
    a = [1, 2, 3, 5, 8, 13, 21] #натуральные числа
    print(a[0:3])
task_2()


def task_3(a:int)->int:
    return a*a
print(task_3(5))#вызываем функцию и печатаем результат







