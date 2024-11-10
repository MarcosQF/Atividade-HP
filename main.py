from heap import *

#Conjunto 1

valores = [10, 5, 20, 1, 15, 30, 25]
valores2 = [10, 5, 20, 1, 15, 30, 25, 200, 2, 9]

bh1 = Heap()
bh2 = Heap()


print(bh2.display_heap())
for valor in valores2:
    bh2.insert(valor)

print(bh1.display_heap())
for valor in valores:
    bh1.insert(valor)
    print(bh1.display_heap())

print("-------2--------")
bh1.change_priority(3, 50)
print(bh1.display_heap())
print("----------------")
bh1.change_priority(1, 8)
print(bh1.display_heap())

print("-------3--------")
bh1.remove()
print(bh1.display_heap())
print("-------3--------")
bh1.remove()
print(bh1.display_heap())
print("-------3--------")
bh1.remove()
print(bh1.display_heap())
print("-------4--------")
print("Maior proridade",bh1.get_high_priority())
print("-------5--------")
print("-------ANTES--------")
print(bh2.display_heap())
bh2.heap_sort()
print("-------DEPOIS--------")
print(bh2.display_heap())




