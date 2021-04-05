data = [-1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def inorder(idx):
    global result
    global size
    if idx < size:
        inorder(2*idx)

        inorder(2*idx+1)
        result += ' ' + str(data[idx])
        return

result = ''
size = len(data)
inorder(1)
print(f'{result}')