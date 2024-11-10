class Heap:
    def __init__(self) -> None:
        self.vector = [None]
        self.size = 0


    def up(self,index):
        parentIndex = index // 2

        if parentIndex >= 1:
            if self.vector[index] > self.vector[parentIndex]:
                self.vector[index],self.vector[parentIndex] = self.vector[parentIndex],self.vector[index]
                self.up(parentIndex)

    def down(self,index):
        childIndex = 2 * index

        if childIndex <= self.size:
            if childIndex < self.size:
                if self.vector[childIndex + 1] > self.vector[childIndex] :
                    childIndex += 1
            if self.vector[index] < self.vector[childIndex]:
                self.vector[index],self.vector[childIndex] = self.vector[childIndex],self.vector[index]
                self.down(childIndex)
        
    def insert(self,new_priority):
        self.vector.append(new_priority)
        self.size += 1
        self.up(self.size)

    def remove(self):
        if self.size != 0:
            print(f'Item maior prioridade processado {self.vector[1]}')
            self.vector[1] = self.vector[-1]
            self.vector.pop()
            self.size -= 1
            self.down(1)
        else:
            raise IndexError("Heap vazia! Não há elementos para remover.")


    def change_priority(self,index, new_priority):
        old_priority = self.vector[index]
        self.vector[index] = new_priority
        
        if new_priority > old_priority:
            self.up(index)
        elif new_priority < old_priority:
            self.down(index)

    def get_high_priority(self):
        return self.vector[1]

    def heap_sort(self):
        for m in range(self.size, 1, -1):
            self.vector[1], self.vector[m] = self.vector[m], self.vector[1]
            self.size -= 1
            self.down(1)

        self.size = len(self.vector) - 1 

    def display_heap(self):
        return self.vector[1:]