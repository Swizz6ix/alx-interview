# **Some facts about pascal triangle**
 - The value at each position of the pascal triangle is the direct sum \
 of the two values above it.

## **Formula**
```
    C(n, k) = C(n,k-1)*(n+1-K)/k
    where: n = current row,
            k = current column
```

## **for example**:

<sup>3</sup>C<sub>2</sub> = C(3, 2-1)*(3+1 - 2)/2 \
    = C(3, 1) * (2)/2 \
    = 3 * 2 / 2 \
    = 3


## **Complexity**
> BigO(n2) time \
> BigO(1) extra space

## **Algorithm**
- [x] The pascal_triangle function is called with the n parameter
- [x] Create an empty list to hold the numbers to build out the triangle.
- [x] If the parameter n is less than or equal to 0 return an empty list.
- [x] Iterates through each row in the range of the parameter n.
    - Initialize each new row to [1], since the first element of each row must be 1
    - in an inner loop, iterate through each column in a row, from the range of 1 to row+1
    - > [!NOTE] We chose to start the loop at index 1 because starting from index 0 \
will lead to ZeroDivisionError while dividing in the formula as already provided.
        - Implement the formula discussed above, give the value of each cell
        - Append each cell to the new row
    - Append each new row to the empty list created earlier 
- [x] and return the list