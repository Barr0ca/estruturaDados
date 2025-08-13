def euclides(a, b):
    if b == 0:
        return a
    return euclides(b, a % b)


print(euclides(48, 18))
