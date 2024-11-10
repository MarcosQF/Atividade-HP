import tkinter as tk

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
        return f'Item de maior prioridade {self.vector[1]}'


    def heap_sort(self,canvas,root):
        
        for m in range(self.size, 1, -1):
            self.vector[1], self.vector[m] = self.vector[m], self.vector[1]
        
            self.display_heap(canvas)
            root.update()
            root.after(700)

            self.size -= 1
            self.down(1)

        self.size = len(self.vector) - 1 

    

    def display_heap(self, canvas):
        
        def draw_tree(index, x, y, level):
            if index > self.size:
                return
            
            node_value = self.vector[index]
            radius = 20  
            node_x = x
            node_y = y


            color = "lightblue"
            canvas.create_oval(node_x - radius, node_y - radius, node_x + radius, node_y + radius, fill=color)
            canvas.create_text(node_x, node_y, text=str(node_value), font=("Arial", 12))

            
            left_child_index = 2 * index
            right_child_index = 2 * index + 1

            
            horizontal_spacing = 150 // (level + 1)  
            vertical_spacing = 80 

            if left_child_index <= self.size:
               
                canvas.create_line(node_x, node_y + radius, x - horizontal_spacing, y + vertical_spacing, arrow=tk.LAST)
                draw_tree(left_child_index, x - horizontal_spacing, y + vertical_spacing, level + 1)

            if right_child_index <= self.size:
                
                canvas.create_line(node_x, node_y + radius, x + horizontal_spacing, y + vertical_spacing, arrow=tk.LAST)
                draw_tree(right_child_index, x + horizontal_spacing, y + vertical_spacing, level + 1)



        draw_tree(1, 400, 40, 0)
       
        canvas.update()
        canvas.after(500)
    