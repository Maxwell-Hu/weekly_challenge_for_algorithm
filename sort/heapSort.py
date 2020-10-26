#!/usr/bin/env python
# -*- coding:utf-8 -*-


def heapify(arr, n, i):
	l = i*2 + 1
	r = i*2 + 2
	largest = i

	if l < n and arr[l] > arr[largest]:
		largest = l

	if r < n and arr[r] > arr[largest]:
		largest = r
	
	if largest != i:
		arr[largest], arr[i] = arr[i], arr[largest]
		heapify(arr, n, largest)

def heapSort(arr):
	n = len(arr)

	for i in range(n, -1, -1):
		heapify(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)

if __name__ == "__main__":
	# l = [9, 2, 1, 7, 6, 8, 5, 3, 4]
	l = [2,1]
	heapSort(l)
	print(l)
