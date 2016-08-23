#!/usr/bin/python

import sys
import random
import math
from random import randint

# author: Daniel Eynis for Daniel Leblanc's CS350 class

# heap sort ####################
def compareElem(elem1, elem2):
	if elem1 < elem2:
		return -1
	elif elem1 > elem2:
		return 1
	return 0

def heapSort(listA):
	lenA = len(listA)
	buildMaxHeap(listA, lenA)
	while lenA > 1:
		lenA -= 1
		listA[0], listA[lenA] = listA[lenA], listA[0]
		heapifyList(listA, lenA, 0)
	return listA

def heapifyList(listA, lenA, i):
	left = (i * 2) + 1
	right = (i * 2) + 2
	largest = i
	if left < lenA and compareElem(listA[left], listA[largest]) > 0:
		largest = left
	if right < lenA and compareElem(listA[right], listA[largest]) > 0:
		largest = right
	if largest != i:
		listA[i], listA[largest] = listA[largest], listA[i]
		heapifyList(listA, lenA, largest)

def buildMaxHeap(listA, lenA):
	for i in range(int(math.floor(lenA/2)), -1, -1):
		heapifyList(listA, lenA, i)
#################################

# quicksort ###############
def quickSort(listA, lowA, highA):
	if lowA >= highA:
		return
	pivot = listA[randint(lowA, highA)]
	i = lowA
	j = highA
	while i <= j:
		while listA[i] < pivot:
			i += 1
		while listA[j] > pivot:
			j -= 1
		if i <= j:
			listA[i], listA[j] = listA[j], listA[i]
			i += 1
			j -= 1

	quickSort(listA, lowA, j)
	quickSort(listA, i, highA)
##############################

# merge sort ################
def mergeSort(listA):
	lenA = len(listA)
	if lenA <= 1:
		return listA
	mid = lenA/2
	listB = mergeSort(listA[:mid])
	listC = mergeSort(listA[mid:])
	return mergeLists(listB, listC)

def mergeLists(listB, listC):
	listD = []
	lenB, lenC = len(listB), len(listC) 
	i, j = 0, 0
	while i < lenB and j < lenC:
		if listB[i] <= listC[j]:
			listD.append(listB[i])
			i += 1
		else:
			listD.append(listC[j])
			j += 1
	if i == lenB:
		listD.extend(listC[j:])
	else:
		listD.extend(listB[i:])
	return listD
##############################


# bucket sort ######################
def bucketSort(listA, bucketSize = 10000):
	lenA = len(listA)
	minA = min(listA)
	maxA = max(listA)
	rangeA = maxA - minA
	finalList = []
	numBuckets = (rangeA/bucketSize) + 1
	table = [[] for x in xrange(0, numBuckets)]

	for i in range(0 , lenA):
		table[int(math.floor((listA[i]-minA)/bucketSize))].append(listA[i])
	
	for i in range(0, numBuckets):
		table[i].sort()
		finalList.extend(table[i])
	
	return finalList
#####################################