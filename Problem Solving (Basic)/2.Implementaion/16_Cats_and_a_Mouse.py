def catAndMouse(x, y, z):
    d_cat_a = abs(x - z)
    d_cat_b = abs(y - z)
    
    if d_cat_a > d_cat_b:
        return "Cat B"
    elif d_cat_a < d_cat_b:
        return "Cat A"
    else:
        return "Mouse C"
        
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        print(result)