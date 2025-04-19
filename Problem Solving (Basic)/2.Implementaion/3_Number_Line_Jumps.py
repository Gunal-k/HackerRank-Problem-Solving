def kangaroo(x1, v1, x2, v2):
    # If velocities are equal, they will never meet unless they start at the same position
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"
    
    # Calculate time t at which both positions become equal
    t = (x2 - x1) / (v1 - v2)
    
    # They meet only if t is a positive whole number
    return "YES" if t >= 0 and t.is_integer() else "NO"

if __name__ == '__main__':
    x1, v1, x2, v2 = map(int, input().split())
    print(kangaroo(x1, v1, x2, v2))