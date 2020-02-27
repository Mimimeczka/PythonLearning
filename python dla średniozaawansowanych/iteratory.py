"wprowadzenie"
# import datetime as dt
# import sys
# start = dt.datetime.now()
# dates = [dt.date(200, 1, 1) + dt.timedelta(days=x) for x in range(40)]
# print("Size of dates = ", sys.getsizeof(dates))
# for x in dates:
#     print(x)
# end = dt.datetime.now()
# print("Total time", end - start)
#
# ''''''
#
# import datetime as dt
# import sys
# start = dt.datetime.now()
#
#
# class Foo:
#     def __init__(self, year, month, day, maxday):
#         self.data = dt.datetime(year, month, day)
#         self.maxday = maxday
#
#     def __next__(self):
#         ret = self.data
#         self.data += dt.timedelta(days=1)
#         return ret
#
#
# md = Foo(2000, 1, 1, 2500000)
#
# for x in range(40):
#     print(next(md))
# end = dt.datetime.now()
# print("Size of dates = ", sys.getsizeof(md))
# print("Total time", end - start)
#
# ''''''
#
# import datetime as dt
# import sys
# start = dt.datetime.now()
#
#
# class Foo:
#     def __init__(self, year, month, day, maxday):
#         self.data = dt.datetime(year, month, day)
#         self.maxday = maxday
#
#     def __next__(self):
#         if self.maxday <= 0:
#             raise StopIteration()
#         ret = self.data
#         self.data += dt.timedelta(days=1)
#         self.maxday -= 1
#         return ret
#
#     def __iter__(self):
#         return self
#
#
# md = Foo(2000, 1, 1, 2500000)
#
# for x in md:
#     pass
#
# end = dt.datetime.now()
# print("Size of dates = ", sys.getsizeof(md))
# print("Total time", end - start)

''''''

# import time
#
# products = ["Product {}".format(i) for i in range(1, 500)]
# print(products)
#
# promotions = ["Promotion {}".format(i) for i in range(1, 50)]
# print(promotions)
#
# customers = ['Customer {}'.format(i) for i in range(1, 500)]
# print(customers)
#
#
# class Combinations:
#     def __init__(self, products, promotions, customers):
#         self.products = products
#         self.promotions = promotions
#         self.customers = customers
#         self.current_product = 0
#         self.current_promotion = 0
#         self.current_customer = 0
#
#     def __next__(self):
#         if self.current_customer >= len(self.customers):
#             self.current_customer = 0
#             self.current_promotion += 1
#
#         if self.current_promotion >= len(self.promotions):
#             self.current_promotion = 0
#             self.current_product += 1
#
#         if self.current_product >= len(self.products):
#             self.current_product = 0
#             raise StopIteration
#
#         item_to_return = (self.products[self.current_product], self.promotions[self.current_promotion], self.customers[self.current_customer])
#         self.current_customer += 1
#         return item_to_return
#
#     def __iter__(self):
#         return self
#
#
# combinations = Combinations(products, promotions, customers)
#
# for c in combinations:
#     # here an analysis will be done - currently, just nothing happens :)
#     pass


'''metoda __getitem__'''

# import datetime as dt
#
#
# class Foo:
#     def __init__(self, year, month, day, maxday):
#         self.data = dt.datetime(year, month, day)
#         self.maxday = maxday
#
#     def __getitem__(self, item):
#         if item <= self.maxday:
#             return self.data + dt.timedelta(days=item)
#         else:
#             raise StopIteration
#
# md = Foo(2000, 1, 1, 2500000)
# print(md[0])
# print(md[1])
# print(md[10])
#
# it = iter(md)
# print(next(it))
# print(next(it))
# print(next(it))
#
# for d in md:
#     print(d)

''''''


# class Combinations:
#
#     def __init__(self, products, promotions, customers):
#         self.products = products
#         self.promotions = promotions
#         self.customers = customers
#
#     def __getitem__(self, item):
#         if item >= len(self.promotions) * len(self.customers) * len(self.products):
#             raise StopIteration
#         else:
#             pos_products = item // (len(self.promotions) * len(self.customers))
#             item = item % (len(self.promotions) * len(self.customers))
#             pos_promotions = item // len(self.customers)
#             item = item % len(self.customers)
#             pos_customers = item
#         return "{} {} {}".format(products[pos_products], promotions[pos_promotions], customers[pos_customers])
#
#
#
#
# products = ["Product {}".format(i) for i in range(1, 4)]
# promotions = ["Promotion {}".format(i) for i in range(1, 3)]
# customers = ['Customer {}'.format(i) for i in range(1, 6)]
#
# combinations = Combinations(products, promotions, customers)
#
# # for x in range(30):
# #     print(combinations[x])
#
# iter_combinations = iter(combinations)
#
# for x in iter_combinations:
#     print(x)


'''iteratory dla typów systemowych'''

# import csv
#
# with open('iteratory_dla_typow-systemowych.csv', newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     # for row in csvreader:
#     #     print('|'.join(row))
#     while True:
#         try:
#             print(next(csvreader))
#         except StopIteration:
#             break

'''klasa iterowalna bez iteratora'''
# import datetime as dt
#
#
# class FooIterator:
#     def __init__(self, data, maxday):
#         self.data = data
#         self.maxday = maxday
#
#     def __next__(self):
#         if self.maxday <= 0:
#             raise StopIteration
#         ret = self.data
#         self.maxday -= 1
#         self.data += dt.timedelta(days=1)
#         return ret
#
#
# class Foo:
#     def __init__(self, year, month, day, maxday):
#         self.data = dt.datetime(year, month, day)
#         self.maxday = maxday
#         self.iterator = FooIterator(self.data, self.maxday)
#
#     def __iter__(self):
#         return self.iterator
#
#
# md = Foo(2000, 1, 1, 3)
#
# for d in md:
#     print(d)

''''''

class CombinationsIterator:
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

    def __next__(self):

        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1

        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1

        if self.current_product >= len(self.products):
            self.current_product = 0
            raise StopIteration()

        item_to_return = "{} - {} -{}".format(self.products[self.current_product],
                                              self.promotions[self.current_promotion],
                                              self.customers[self.current_customer])

        self.current_customer += 1

        return item_to_return



class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.iterator = CombinationsIterator(products, promotions, customers)

    def __iter__(self):
        return self.iterator


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

combinations = Combinations(products, promotions, customers)

for c in combinations:
    print(c)