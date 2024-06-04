def process_purchases(n):
    purchase_dict = {}

    for _ in range(n):
        record = input("Введите запись о покупке (id product quantity): ").split()
        customer_id = int(record[0])
        product = record[1]
        quantity = int(record[2])

        if customer_id not in purchase_dict:
            purchase_dict[customer_id] = []

        purchase_dict[customer_id].append((product, quantity))

    for customer_id, purchases in purchase_dict.items():
        print(f"Покупатель с ID {customer_id} купил:")
        for purchase in purchases:
            print(f"{purchase[0]} в количестве {purchase[1]}")

n = int(input("Введите количество записей о покупках: "))
process_purchases(n)

#253 Карандаш 3