def check_cities(n):
    cities = set()

    for _ in range(n):
        city = input()
        if city in cities:
            print("REPEAT")
        else:
            cities.add(city)
            print("OK")


n = int(input())
check_cities(n)
