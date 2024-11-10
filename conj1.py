from heap import *


#Conjunto 1

valores = [10, 5, 20, 1, 15, 30, 25]

bh1 = Heap()

root = tk.Tk()
root.title("Heap Tree")
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()


#1. Construção do Heap

for valor in valores:
    bh1.insert(valor)
    bh1.display_heap(canvas)   

#2. Alteração de Prioridade

root.after(700)  
bh1.change_priority(3, 50)  
bh1.display_heap(canvas)  

root.after(700)  
bh1.change_priority(1, 8)
bh1.display_heap(canvas) 

#3. Remoções

root.after(700) 
bh1.remove()
canvas.delete("all") 
bh1.display_heap(canvas)
root.update()

bh1.remove()
canvas.delete("all") 
bh1.display_heap(canvas)
root.update()

bh1.remove()
canvas.delete("all") 
bh1.display_heap(canvas)
root.update()

#4. Heapsort

root.after(700) 
bh1.heap_sort(canvas,root)
bh1.display_heap(canvas)
root.update()

#5. Selecionar Alta Prioridade
print(bh1.get_high_priority())


root.mainloop()


