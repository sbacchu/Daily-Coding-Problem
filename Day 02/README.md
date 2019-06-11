Problem 2
=========

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]

Bonus: what if you can't use division?

Asked by: Uber<br>
Difficulty Level: Hard

###### Solution Steps
- [x] Create var product<br>
- [x] Loop through the array multiplying each element into product<br>
- [x] Loop through the array another time replacing each element with the division of the product and the element<br>
- [ ] Do it in one pass
