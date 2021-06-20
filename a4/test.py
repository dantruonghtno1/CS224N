import torch
A = torch.tensor([[0.7964, 0.1066, 0.9819],
        [0.7666, 0.4947, 0.0489]])
print(A)
print(type(A))
print(A.shape)
B = torch.unsqueeze(A,1)
print(B)
print(B.shape)

B = torch.unsqueeze(A,0)
print(B)
print(B.shape)

B = torch.unsqueeze(A,-1)
print(B)
print(B.shape)