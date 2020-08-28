#!/usr/bin/env python
# -*- coding:utf-8 -*-

def heapSort(lst):
	def sift_down(start, end):
		root = start
		while True:
			child = 2 * root + 1
			if child > end:
				break
			if child + 1 <= end and lst[child] < lst[child + 1]:
				child += 1
			if lst[root] < lst[child]:
				lst[root], lst[child] = lst[child], lst[root]
				root = child
			else:
				break

	# Initialize heap.
	for start in range((len(lst)-2), -1, -1):
		sift_down(start, len(lst)-1)

	# Heap sort.
	for end in range(len(lst)-1, 0, -1):
		lst[0], lst[end] = lst[end], lst[0]
		sift_down(0, end - 1)
	return lst


if __name__ == "__main__":
    l = [9, 2, 1, 7, 6, 8, 5, 3, 4]
    heap_sort(l)
