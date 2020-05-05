# Bubble Sort

## Instructions

* You are required to sort the data in the file Bubble_Sort.xslm using the Bubble Sort Algorithm. Below is an example,

![Bubble Sort Example](Images/bubble-sort.png)

* Take an array of numbers " 5 1 4 2 8", and sort the array from lowest number to greatest number using bubble sort. In each step, elements written in bold are being compared. Three passes will be required;

  1. First Pass
    * ( 5 1 4 2 8 ) → ( 1 5 4 2 8 ) 
    * Here, algorithm compares the first two elements, and swaps since 5 > 1
    * ( 1 5 4 2 8 ) → ( 1 4 5 2 8 )
    * Swap since 5 > 4
    * ( 1 4 5 2 8 ) → ( 1 4 2 5 8 )
    * Swap since 5 > 2
    * ( 1 4 2 5 8 ) → ( 1 4 2 5 8 )
    * Now, since these elements are already in order (8 > 5), algorithm does not swap them.

  2. Second Pass
    * ( 1 4 2 5 8 ) → ( 1 4 2 5 8 )
    * ( 1 4 2 5 8 ) → ( 1 2 4 5 8 )
    * Swap since 4 > 2
    * ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
    * ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
    * Now, the array is already sorted, but the algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

  3. Third Pass
    * ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
    * ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
    * ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )
    * ( 1 2 4 5 8 ) → ( 1 2 4 5 8 )

  