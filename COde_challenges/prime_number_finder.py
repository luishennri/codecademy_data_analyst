def prime_finder(n):

    prime_list = []
    for number in range(2, n+1):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            prime_list.append(number)
    return prime_list


print(prime_finder(11))
