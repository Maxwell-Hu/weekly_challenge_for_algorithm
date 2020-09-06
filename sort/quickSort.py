def sort(arr, left, right):
	if left >= right: return
	pivot = arr[left]
	p, q = left, right
	while p < q:
		while arr[q] >= pivot and p<q:
			q -= 1
		arr[p] = arr[q]
		while  arr[p] <= pivot and p<q:
			p += 1
		arr[q] = arr[p]
	arr[p] = pivot
	sort(arr, left, p-1)
	sort(arr, p+1, right)
	return arr

if __name__ == '__main__':
	x = [12,4,2,8,3,1,9,5,-4,0,4]
	sort(x,0,len(x)-1)
	
