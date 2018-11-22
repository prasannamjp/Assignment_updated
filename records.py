import re

# f = open("customerdata.txt", "r")
# data = f.read()
# f.close()

with open("customerdata.txt", 'r') as data:
    data = data.read()


class Restaurant:
    regx_1 = r'\w[a-z A-z]{2,20}'
    regx_2 = r'\d{1,9}\s'
    regx_3 = r'\w[a-z A-z]{2,20}'

    def total_orders(self):
        orders = re.findall(self.regx_1, data)
        count = len(orders)
        return count

    def total_order_amount(self):
            Amount = re.findall(self.regx_2, data)
            total = 0
            for i in Amount:
                total += (int(i))
            return total

    def customers_count(self):
        names = re.findall(self.regx_3, data)
        wordcount = {}
        for word in names:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
        return wordcount

    def once_ordered(self):
        wordcount = self.customers_count()
        count = 0
        names = []
        for key, value in wordcount.items():
            if wordcount[key] == 1:
                count += 1
                names.append(key)
        return count, names

    def customer_report(self):
        orders = {}
        wordcount = self.customers_count()
        order_count = [1, 2, 3, 4, 5, 6, 7, 31]
        for i in order_count:
            count = 0
            for key, value in wordcount.items():
                if wordcount[key] == i:
                    count += 1
            orders[i] = count
        return orders


if __name__ == "__main__":
    customers = Restaurant()
    print()
    print("this site recived", customers.total_orders(), "orders")
    print('-'* 40)
    print()

    print("total order amount =", customers.total_order_amount())
    print('-'* 40)
    print()

    count, names = customers.once_ordered()
    print(count, "Customers ordered only once.")
    print("-" * 40)
    for i in names:
        print(i)
        print()
    print('-'* 40)
    print()

    print("orders   |  count of customer")
    print("-" * 40)
    order = customers.customer_report()
    print("1        |  %s  " % order[1])
    print("2        |  %s  " % order[2])
    print("3        |  %s  " % order[3])
    print("4        |  %s  " % order[4])
    print("5+       |  %s  " % (order[5] + order[6] + order[7] + order[31]))
    print()
