prime_list = []
def prime_finder(n):
    for i in range(2,n+1):
        prime = True
        for number in range(2, i):
            if i % number == 0:
                prime = False
                break
        if prime:
            prime_list.append(i)
    return prime_list

print(prime_finder(11))
