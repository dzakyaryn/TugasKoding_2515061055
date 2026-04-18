import torch
x_q = torch.tensor([[8, 7, 6], [5, 4, 3], [2, 1, 0]]) #membuat matriks 3x3
print(x_q) #Menampilkan matriks 3x3
y_q = torch.tensor([[-1, -2,], [-4, -5,], [-3, -6]]) #membuat matriks 3x2
print(y_q)  #menampilkan matriks 3x2
print(torch.matmul(x_q, y_q)) #menampilkan perhitungan matriks x_q dan y_q