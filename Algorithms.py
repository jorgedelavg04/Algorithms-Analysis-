import matplotlib.pyplot as plt
import numpy as np
import time
import random
import sys
sys.setrecursionlimit(1500)

"""Examen/Proyecto 1 de Algoritmos"""

__Nombre__      = "Jorge Constanzo De la Vega Carrasco"
__Matricula__   = "A01650285"

__Profesor__    = "Juan Velez Ballesteros"

### Algoritmos ###
	
# Insertion Sort(Ciclico)
def insertionSort(arr):
 
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        j = i-1
        
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

    return arr

# Merge Sort(Recursivo)
def mergeSort(arr):

   if len(arr)>1:
       mid = len(arr)//2
       lefthalf = arr[:mid]
       righthalf = arr[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               arr[k]=lefthalf[i]
               i=i+1
           else:
               arr[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           arr[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           arr[k]=righthalf[j]
           j=j+1
           k=k+1

   return arr

# Quicksort(Divide y Venceras)
def partition(arr, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if arr[i] <= arr[begin]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]
    arr[pivot], arr[begin] = arr[begin], arr[pivot]
    return pivot



def quicksort(arr, begin=0, end=None):
    if end is None:
        end = len(arr) - 1
    def _quicksort(arr, begin, end):
        if begin >= end:
            return
        pivot = partition(arr, begin, end)
        _quicksort(arr, begin, pivot-1)
        _quicksort(arr, pivot+1, end)
    return _quicksort(arr, begin, end)

### Tiempo de los Algoritmos ####

def timeInsertionSort(arr):

	start = time.clock()
	insertionSort(arr)
	final = time.clock()

	resultTime = final - start

	return resultTime

def timeMergeSort(arr):

	start = time.clock()
	mergeSort(arr)
	final = time.clock()

	resultTime = final - start

	return resultTime

def timeQuickSort(arr):

	start = time.clock()
	quicksort(arr)
	final = time.clock()

	resultTime = final - start 

	return resultTime

### Peor de los Casos ###
def worstInsertionSort(n):
	
	arr = []
	for x in range(0, n+1):
		arr.append(x)
	return arr

def worstQuickSort(n):
	
	arr = []
	for x in range(0, n+1):
		arr.append(x)
	return arr  

def worstMergeSort(n):
	arr = []
	for x in range(0, n+1):
		arr.append(x)
	return arr 

def plotWorstCase(x, y1,y2,y3):
	


	plt.plot(x, y1, label='Insertion Sort')
	plt.plot(x, y2, label='Quick Sort')
	plt.plot(x, y3, label='Merge Sort')
	plt.title("Worst Case")
	plt.legend()


### Caso Intermedio ###

def intermedio(n):
    arr = []
    for x in range (0,n):
        arr.append(random.randint(0, 500))
    return arr

def plotCasoIntermedio(x, y1,y2,y3):
	
	plt.plot(x, y1, label='Insertion Sort')
	plt.plot(x, y2, label='Quick Sort')
	plt.plot(x, y3, label='Merge Sort')
	plt.title("Caso Intermedio")
	plt.legend()

### Mejor Caso ###
def bestInsertionSort(n):
	
	arr = []
	for x in range(0, n):
		arr.append(x)
	return arr

def bestQuickSort(n):
	
	arr = []
	for x in range(0, n):
		arr.append(x)
	return arr 

def bestMergeSort(n): 

	arr = []
	for x in range(0, n):
		arr.append(x)
	return arr 


def plotBestCase(x, y1,y2,y3):
	
	plt.plot(x, y1, label='Insertion Sort')
	plt.plot(x, y2, label='Quick Sort')
	plt.plot(x, y3, label='Merge Sort')
	plt.title("Mejor Caso")
	plt.legend() 

def findPointsOfIntersection(a, b): 
	intersect = [val for val in a if val in b]
	return intersect

def numberOfArrays(m,n):
	y =m*n
	return y
   
def main():

	arrayNumber = 500
	m1 = [0]
	x = list(range(0, arrayNumber))
	
	y1 = numberOfArrays(m1,arrayNumber)
	y2 = numberOfArrays(m1,arrayNumber)
	y3 = numberOfArrays(m1,arrayNumber)


	print("Se debe cerrar cada ventana para abrir la siguiente, OJO, puede llegar a tardar en abrir")

### Plot Peor Caso
	for i in x:
		arr2 = worstInsertionSort(i)
		arr3 = worstQuickSort(i)
		arr4 = worstMergeSort(i)

		intersection1 = findPointsOfIntersection(arr2, arr3)
		intersection2 = findPointsOfIntersection(arr2, arr4)
		intersection3 = findPointsOfIntersection(arr3, arr4)
		
		y1[i] = timeInsertionSort(arr2)
		y2[i] = timeQuickSort(arr3)
		y3[i] = timeMergeSort(arr4)
	
	plotWorstCase(x,y1,y2,y3)
	plt.show()

### Plot Caso Intermedio
	for i in x:
		arr2 = intermedio(i)
		arr3 = intermedio(i)
		arr4 = intermedio(i)
		
		intersection1 = findPointsOfIntersection(arr2, arr3)
		intersection2 = findPointsOfIntersection(arr2, arr4)
		intersection3 = findPointsOfIntersection(arr3, arr4)

		y1[i] = timeInsertionSort(arr2)
		y2[i] = timeQuickSort(arr3)
		y3[i] = timeMergeSort(arr4)

	plotCasoIntermedio(x,y1,y2,y3)
	plt.show()

### Plot Mejor Caso 
	for i in x:
		arr2 = bestInsertionSort(i)
		arr3 = bestQuickSort(i)
		arr4 = bestMergeSort(i)

		intersection1 = findPointsOfIntersection(arr2, arr3)
		intersection2 = findPointsOfIntersection(arr2, arr4)
		intersection3 = findPointsOfIntersection(arr3, arr4)

		y1[i] = timeInsertionSort(arr2)
		y2[i] = timeQuickSort(arr3)
		y3[i] = timeMergeSort(arr4)

	plotBestCase(x,y1,y2,y3)
	plt.show()

if __name__ == '__main__':
    main()


