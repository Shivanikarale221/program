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
import numpy as np

arr = np.array([[1,2], [3,4], [5,6]])

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
import numpy as np

arr = np.arange(1, 26).reshape(5, 5)

print(arr)
print("Second row:", arr[1])
print("Third column:", arr[:, 2])

# 20.Given [[10, 20, 30], [40, 50, 60], [70, 80, 90]], find the row sums, column sums, overall mean, and elements greater than 45.
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Row sums:", np.sum(arr, axis=1))
print("Column sums:", np.sum(arr, axis=0))
print("Overall mean:", np.mean(arr))
print("Elements > 45:", arr[arr > 45])


# 21.Create a NumPy array containing all even numbers from 2 to 20.
arr = np.arange(2, 21, 2)
print(arr)


# 22.Create a NumPy array containing 10 equally spaced values between 0 and 1.
arr = np.linspace(0, 1, 10)
print(arr)


# 23.Given arr = np.array([3, 7, 2, 9, 4, 8]), find the index of the maximum value.
arr = np.array([3, 7, 2, 9, 4, 8])

print(np.argmax(arr))


# 24.Given arr = np.array([10, 20, 30, 40, 50]), reverse the array.
arr = np.array([10, 20, 30, 40, 50])

print(arr[::-1])


# 25.Find the unique values in np.array([1, 2, 2, 3, 4, 4, 5]).
arr = np.array([1, 2, 2, 3, 4, 4, 5])

print(np.unique(arr))


# 26.Count how many elements are greater than 25 in np.array([10, 30, 15, 40, 25, 50]).
arr = np.array([10, 30, 15, 40, 25, 50])

print(np.sum(arr > 25))


# 27.Convert the following 1D array into a 3 × 3 array: np.array([1,2,3,4,5,6,7,8,9]).

arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr.reshape(3, 3))

# 28.Flatten the array [[1, 2], [3, 4], [5, 6]] into a 1D array.
arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(arr.flatten())


# 29.Concatenate np.array([1,2,3]) and np.array([4,5,6]).
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.concatenate((a, b)))


# 30.Split np.array([1,2,3,4,5,6]) into three equal parts.
arr = np.array([1,2,3,4,5,6])

print(np.split(arr, 3))


# 31.Find the standard deviation of np.array([10, 20, 30, 40, 50]).
arr = np.array([10, 20, 30, 40, 50])

print(np.std(arr))


# 32.Find the variance of np.array([2, 4, 6, 8, 10]).
arr = np.array([2, 4, 6, 8, 10])

print(np.var(arr))

# 33.Given arr = np.array([1, 2, 3, 4, 5]), calculate the cumulative sum.
arr = np.array([1, 2, 3, 4, 5])

print(np.cumsum(arr))


# 34.Given arr = np.array([1, 2, 3, 4, 5]), calculate the cumulative product.
arr = np.array([1, 2, 3, 4, 5])

print(np.cumprod(arr))


# 35.Replace all odd numbers with -1 in np.array([1,2,3,4,5,6,7]).
arr = np.array([1,2,3,4,5,6,7])

arr[arr % 2 != 0] = -1

print(arr)


# 36.Find the maximum value in each row of [[1,5,3],[8,2,6],[4,9,7]].
arr = np.array([
    [1,5,3],
    [8,2,6],
    [4,9,7]
])

print(np.max(arr, axis=1))


# 37.Find the minimum value in each column of [[5,2,8],[1,7,3],[6,4,9]].
arr = np.array([
    [5,2,8],
    [1,7,3],
    [6,4,9]
])

print(np.min(arr, axis=0))


# 38.Create a 4 × 4 identity matrix using NumPy.
arr = np.eye(4)

print(arr)


# 39.Generate a 3 × 3 matrix of random integers between 1 and 20.
arr = np.random.randint(1, 21, size=(3, 3))

print(arr)

# 40.Given two NumPy arrays, find the elements that are common to both arrays.
a = np.array([1,2,3,4,5])
b = np.array([3,4,5,6,7])

print(np.intersect1d(a, b))





# Exercises. 

# Get the shape of the matrix.
import numpy as np

students = np.array([
    [18, 85, 78],
    [19, 92, 88],
    [18, 76, 82],
    [20, 95, 91],
    [17, 68, 74]
])

# Columns: Age, Math, Science
print(students.shape)


# Find the average age of students.
print(np.mean(students[:, 0]))


# Extract the Math marks of all students.
print(students[:, 1])


# Find the highest Science mark.
print(np.max(students[:, 2]))


# Get the details of the student who scored more than 90 in Math.
print(students[students[:, 1] > 90])


# Increase the Math marks of all students by 5.
students[:, 1] += 5

print(students)


# Find how many students are younger than 19.
print(np.sum(students[:, 0] < 19))


# Calculate the average marks in each subject (column-wise mean).
print(np.mean(students[:, 1:], axis=0))


# Get the data of students who scored at least 80 in both subjects.
result = students[
    (students[:, 1] >= 80) &
    (students[:, 2] >= 80)
]

print(result)

# Science marks below 75 with 0
students[students[:, 2] < 75, 2] = 0

print(students)



