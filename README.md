Quick Sort:
Quick Sort is a widely used comparison-based sorting algorithm. It follows the divide-and-conquer approach, dividing the array into smaller sub-arrays and sorting them recursively. Quick Sort works by selecting a pivot element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. It then recursively sorts the sub-arrays. This process continues until the entire array is sorted.

Analysis: 
   - Average Case: O(n log n)
   - Worst Case: O(n^2) (When the pivot choice consistently results in unbalanced partitions)
   - Best Case: O(n log n) (When the pivot choice consistently results in balanced partitions)

Counting Sort:
Counting Sort is a non-comparative integer sorting algorithm. It counts the occurrences of each element in the input and uses this information to place elements in sorted order. Counting Sort creates a counting array to store the frequency of each element. It then modifies the counting array to accumulate the counts. Finally, it uses the counting array to place each element in its sorted position.

Analysis: 
   -Average Case: O(n + k), where n is the number of elements to be sorted, and k is the range of input.
 - Worst Case: O(n + k)
 - Best Case: O(n + k)

Heap Sort:
Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. It sorts the array by repeatedly removing the maximum or minimum element from the heap and adding it to the sorted portion. Heap Sort first converts the input array into a max-heap (or min-heap). It repeatedly extracts the maximum or minimum element from the heap and places it at the end of the array until the array is sorted.

Analysis: 
   - Average Case: O(n log n)
   - Worst Case: O(n log n)
   - Best Case: O(n log n)
