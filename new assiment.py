# 1.How do you create a NumPy array from the list [1, 2, 3, 4, 5]?

import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

# 2.What is the output of np.array([10, 20, 30, 40])[2]?

import numpy as np
print(np.array([10,20,30,40]) [2])


# 3.Create a NumPy array containing integers from 1 to 10.

arr = np.arange(1, 11)
print(arr)

# 4.Create a NumPy array containing five zeros.
arr = np.zeros(5)
print(arr)

#5. Create a 3 × 3 NumPy array containing only ones.
arr=np.ones((3,3))
print(arr)

#6. What is the shape of np.array([[1, 2, 3], [4, 5, 6]])?
arr=np.array([1,2,3],[4,5,6])
print(arr.shape)

#7. What is the number of dimensions of np.array([[1, 2], [3, 4], [5, 6]])?
arr=np.array([[1,2],[3,4],[5,6]])
print(arr.ndim)

# 8.Given arr = np.array([10, 20, 30, 40, 50]), extract the elements from index 1 to index 3.
arr=np.array([10,20,30,40,50])
print(arr[1:4])

# 9.Given arr = np.array([1, 2, 3, 4, 5]), multiply every element by 10.
arr=np.array([1,2,3,4,5])
print(arr*10)

# 10.Find the sum, mean, maximum, and minimum of np.array([12, 5, 8, 20, 15]).
arr=np.array([12,5,8,20,15])
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 11.Given arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), extract only the even numbers.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr[arr % 2 == 0])

# 12.Sort np.array([5, 2, 8, 1, 9, 3]) in ascending order.
import numpy as np

arr = np.array([5, 2, 8, 1, 9, 3])
print(np.sort(arr))

# 13.Find the indices of elements greater than 50 in np.array([10, 60, 30, 80, 45, 90]).
arr = np.array([10, 60, 30, 80, 45, 90])

print(np.where(arr > 50))

# 14.Reshape np.array([1, 2, 3, 4, 5, 6]) into a 2 × 3 array.
arr = np.array([1, 2, 3, 4, 5, 6])

print(arr.reshape(2, 3))

# 15.Given two arrays [1, 2, 3] and [4, 5, 6], perform element-wise addition, subtraction, multiplication, and division.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)


# 16.Perform matrix multiplication on [[1, 2], [3, 4]] and [[5, 6], [7, 8]].
arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])

print(np.matmul(arr1, arr2))

# 17.Find the transpose of [[1, 2, 3], [4, 5, 6]].
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.T)

# 18.Replace all values greater than 3 with 100 in np.array([1, 2, 3, 4, 5]).
arr = np.array([1, 2, 3, 4, 5])

arr[arr > 3] = 100

print(arr)


# 19.Create a 5 × 5 array containing numbers from 1 to 25 and extract the second row and third column.


# 20.Given [[10, 20, 30], [40, 50, 60], [70, 80, 90]], find the row sums, column sums, overall mean, and elements greater than 45.

# 21.Create a NumPy array containing all even numbers from 2 to 20.


# 22.Create a NumPy array containing 10 equally spaced values between 0 and 1.


# 23.Given arr = np.array([3, 7, 2, 9, 4, 8]), find the index of the maximum value.


# 24.Given arr = np.array([10, 20, 30, 40, 50]), reverse the array.


# 25.Find the unique values in np.array([1, 2, 2, 3, 4, 4, 5]).


# 26.Count how many elements are greater than 25 in np.array([10, 30, 15, 40, 25, 50]).


# 27.Convert the following 1D array into a 3 × 3 array: np.array([1,2,3,4,5,6,7,8,9]).

