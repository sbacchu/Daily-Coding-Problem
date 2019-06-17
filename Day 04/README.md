Problem 4
=========

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give `3`.

You can modify the input array in-place

Asked by: Stripe<br>
Difficulty Level: Hard

##### Solution Steps
> Uses `O(n)` Space
- [ ] Create another array that acts as a hash<br>
- [ ] Place each element in the new array based on its value (we can disregard negative numbers) <br>
- [ ] loop through the second array to check if there is an element at the location<br>
- [ ] if it is empty, return the current value of the index

>Using `O(1)` space
- [ ] First loop throught the array to remove all the negative numbers
- [ ] For hashing in place, By looping through the array another time, we can negate the value of the index element
- [ ] In the next loop if the value at the index in not negative we can conclude that number was not in the originar array and we can return the value