'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность
алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.


Сравним два алгоритма по скорости и сложности.
Без использования «Решета Эратосфена» сложность O(n*n/2)
Используя алгоритм «Решето Эратосфена» сложность O(n*log(n))

Выполним сравнение скоростей.
При размере массива 100 элементов
0.008647796999999957
0.00575852500000007
Отношение скоростей: 1,5

При размере массива 200 элементов
5.001410503000001
2.657330043999999
Отношение скоростей: 1,88

При размере массива 300 элементов
8.817983084
4.138150188999999
Отношение скоростей: 2,13

Выводы:
1. Алгоритм «Решето Эратосфена» быстрее, чем алгоритм без решета Эратосфена.
2. С ростом количества искомых простых чисел разница (отношение) скоростей двух алгоритмов становится все более заметным.


'''
import timeit


def non_eratosthenes():
    a=[]
    # начинаем с 3-го элемента
    for i in range(2,n+1):
        f=True
        for j in range(2,i//2+1):
            if i%j==0:
                f=False
                break
        if f:
            a.append(i)
    #print(a)


def eratosthenes():
    # список заполняется значениями от 0 до n
    a = []
    for i in range(n + 1):
        a.append(i)

    # Вторым элементом является единица,
    # которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    # начинаем с 3-го элемента
    i = 2
    while i <= n:
        # Если значение ячейки до этого не было обнулено,
        # в этой ячейке содержится простое число.
        if a[i] != 0:
            # первое кратное ему будет в два раза больше
            j = i + i
            while j <= n:
                # это число составное, поэтому заменяем его нулем
                a[j] = 0
                # переходим к следующему числу, которое кратно i (оно на i больше)
                j = j + i
        i += 1

    # Превращая список во множество,
    # избавляемся от всех нулей кроме одного.
    a = set(a)
    # удаляем ноль
    a.remove(0)
    #print(a)


n=100
#non_eratosthenes()
#eratosthenes()
print(timeit.timeit("non_eratosthenes()", setup="from __main__ import non_eratosthenes", number=10000))
print(timeit.timeit("eratosthenes()", setup="from __main__ import eratosthenes", number=10000))


