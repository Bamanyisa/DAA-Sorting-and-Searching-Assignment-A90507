Quick Sort:

![Quick Sort Illustration](https://www.geeksforgeeks.org/wp-content/uploads/gq/2014/01/QuickSort2.png)

Quick Sort is a highly efficient sorting algorithm based on the divide-and-conquer strategy, where it recursively divides an array into smaller subarrays and then sorts them. 

Explanation:

Select a Pivot: The algorithm selects a pivot element from the input array. Common choices include the first, last, or a randomly chosen element.

Partitioning: The elements in the array are rearranged such that elements less than the pivot are moved to its left, and elements greater than the pivot are moved to its right. At this point, the pivot is in its final sorted position.

Recursion: Recursively apply Quick Sort to the sub-arrays to the left and right of the pivot.

Base Case: If the sub-array has only one element or is empty, it is considered sorted.

Quick sort recursively divides the array into smaller sub-arrays, sorting each of them. 

It does this by selecting a pivot element (usually the first element) and dividing the array into two sub-arrays: one containing elements less than or equal to the pivot and the other containing elements greater than the pivot.

The pivot is placed in its correct position within the array after partitioning.

The algorithm then proceeds to recursively sort the sub-arrays to the left and right of the pivot until the entire array is sorted.
  
Analysis:

Time Complexity
   - Average Case: O(n log n)
   - Worst Case: O(n^2) (When the pivot choice consistently results in unbalanced partitions)
   - Best Case: O(n log n) (When the pivot choice consistently results in balanced partitions)


Counting Sort:

![Counting Sort Illustration 01](https://media.geeksforgeeks.org/wp-content/uploads/20230920182425/1.png)
![Counting Sort Illustration 02](https://media.geeksforgeeks.org/wp-content/uploads/20230920182436/2.png)
![Counting Sort Illustration 03](https://media.geeksforgeeks.org/wp-content/uploads/20230922132754/3.png)
![Counting Sort Illustration 04](https://media.geeksforgeeks.org/wp-content/uploads/20230920182646/4.png)
![Counting Sort Illustration 05](https://media.geeksforgeeks.org/wp-content/uploads/20230920182656/5.png)
![Counting Sort Illustration 06](https://media.geeksforgeeks.org/wp-content/uploads/20230920182724/6.png)
![Counting Sort Illustration 07](https://media.geeksforgeeks.org/wp-content/uploads/20230920182741/7.png)
![Counting Sort Illustration 08](https://media.geeksforgeeks.org/wp-content/uploads/20230920182752/8.png)
![Counting Sort Illustration 09](https://media.geeksforgeeks.org/wp-content/uploads/20230920182807/9.png)
![Counting Sort Illustration 10](https://media.geeksforgeeks.org/wp-content/uploads/20230920182827/10.png)
![Counting Sort Illustration 11](https://media.geeksforgeeks.org/wp-content/uploads/20230920182855/11.png)
![Counting Sort Illustration 12](https://media.geeksforgeeks.org/wp-content/uploads/20230920182910/12.png)

Counting Sort is a non-comparative integer sorting algorithm. It works by counting the occurrences of each element in the input array and using this information to place elements in sorted order.

Explanation:

Counting Frequencies: First, the algorithm calculates the frequency of each element in the input array. It creates a count array to store these frequencies.

Cumulative Counts: The count array is modified to contain the cumulative counts of elements. This helps determine the final positions of each element in the sorted output.

Build the Sorted Array: Based on the cumulative counts, the algorithm constructs the sorted array by placing elements in their correct positions.

Counting Sort works by counting the occurrences of each element in the input array.

It calculates the range of input values to determine the size of the count array.

It counts the occurrences of each element and then calculates cumulative counts. The cumulative counts indicate the positions where elements should be placed in the sorted output.

The algorithm constructs the sorted array by placing elements in their correct positions based on the cumulative counts.

Analysis:

Time Complexity:
 -Average Case: O(n + k), where n is the number of elements to be sorted, and k is the range of input.
 - Worst Case: O(n + k)
 - Best Case: O(n + k)

Heap Sort:

![Heap Sort Illustration 01](https://media.geeksforgeeks.org/wp-content/uploads/20230530092618/1-(1).webp)
![Heap Sort Illustration 02](https://media.geeksforgeeks.org/wp-content/uploads/20230530092705/2-(1).webp)
![Heap Sort Illustration 03](https://media.geeksforgeeks.org/wp-content/uploads/20230530092725/3-(1).webp)
![Heap Sort Illustration 04](https://media.geeksforgeeks.org/wp-content/uploads/20230530092805/4-(1).webp)
![Heap Sort Illustration 05](https://media.geeksforgeeks.org/wp-content/uploads/20230530092841/6.webp)
![Heap Sort Illustration 06](https://media.geeksforgeeks.org/wp-content/uploads/20230530092858/7.webp)

Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure.

Explanation:

Heapify: The input array is transformed into a max-heap (or min-heap), where the maximum (or minimum) element is at the root.

Sorting: The root element (the maximum in max-heap or minimum in min-heap) is removed and appended to the sorted list. This process is repeated until the heap is empty.

Heap Sort begins by transforming the input array into a binary max-heap. A max-heap ensures that the largest element is at the root.

The root element is removed and appended to the sorted list. The heap is then reconstructed to maintain the max-heap property. This process is repeated until the heap is empty.

Analysis:

Time Complexity: 
   - Average Case: O(n log n)
   - Worst Case: O(n log n)
   - Best Case: O(n log n)
