import numpy as np
x_sym = np.array([[0, 6, 1], [6, 5, 2], [1, 2, 7]]) #Membuat matrix simetris
print(x_sym) #Menampilakan matrix simetris
x_sym_t = x_sym.T #membuktikan matrix simetris dengan men-transpose
print(x_sym_t) #Menampilkan tranpose  matrix simetris
print(x_sym.T == x_sym) #membuktikan apakah setiap posisi sama 

import torch
I = torch.tensor([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) #Membuat matriks identitas 4x4 menggunakan pytorch
print(I) #menampilkan matriks idenitas
b_pt = torch.tensor([25, 5, 61, 55]) #Membuat vektor 4x1 
print(b_pt) #Menampilkan vektor 4x1
print(torch.matmul(I, b_pt)) #menampilkan perkalian matriks identitas dengan vektor b

