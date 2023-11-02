import galois

p = 3
GF = galois.GF(p)

f = galois.Poly([1, 2, 1, 0, -1, 0, 1], field=GF)
print(f)

for i in range(p):
    val = f(i)
    print(f"\nf({i}) = {val}")
    if val == 0:
        g = galois.Poly([1, -i], field=GF)
        div = f //g
        rem = f % g
        print(f"({g})({div}) + {rem}")
