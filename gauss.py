matrix = [
  [30.1, -1.4, 10, -1.5],
  [-17.5, 11.1, 1.3, -7.5],
  [1.7, -21.1, 7.1, -17.1],
  [2.1, 2.1, 3.5, 3.3]
]
originMatrix = [
  [30.1, -1.4, 10, -1.5],
  [-17.5, 11.1, 1.3, -7.5],
  [1.7, -21.1, 7.1, -17.1],
  [2.1, 2.1, 3.5, 3.3]
]
accuracy = 0.001
f = [10, 1.3, 10, 1.7]
originF = [10, 1.3, 10, 1.7]
errorMessage = ""

def delArray(arr, num):
  res = []
  for i in range(len(arr)):
    res.append(arr[i] / num)
  return res

def multiArray(arr, num):
  res = []
  for i in range(len(arr)):
    res.append(arr[i] * num)
  return res

def minusArray(left, right):
  if(len(left) != len(right)):
    return 0
  for i in range(len(left)):
    left[i] -= right[i]
  return left

class Matrix:
  def __init__(self, matrix, f, accuracy, errorMessage):
    self.matrix = matrix
    self.f = f
    self.accuracy = accuracy
    self.errorMessage = errorMessage

  def Forward(self, errorMessage):
    for i in range(len(self.matrix)):
      self.matrix[i].append(self.f[i])
    for i in range(len(self.matrix)):
      self.matrix[i] = delArray(self.matrix[i], self.matrix[i][i])
      for j in range(i+1, len(self.matrix)):
        coef = self.matrix[j][i]
        right = multiArray(self.matrix[i], coef)
        self.matrix[j] = minusArray(self.matrix[j], right)
    print(self.matrix)

  def Reverse(self, errorMessage):
    for i in range(len(self.matrix), 0, -1):
      for j in range(i - 1, 0, -1):
        coef = self.matrix[j][i]
        right = multiArray(self.matrix[i], coef)
        self.matrix[j] = minusArray(self.matrix[j], right)
    print(self.matrix)





m = Matrix(matrix, f, accuracy, errorMessage)
m.Forward(errorMessage)
m.Reverse(errorMessage)
