from material import material

ap = material(G = 14190.0, lame = 5700.95) #real
print(ap.display)
ap = material(E = 32447.0 / 10, Poisson = 0.1433)
print(ap.display)
ap = material(K = 15160.95 / 10, Poisson = 0.1433)
print(ap.display)

htpb = material(G = 0.8003, lame = 710.85) #real
print(htpb.display)
htpb = material(E = 1000 * 2.4, Poisson = 0.4994)
print(htpb.display)
htpb = material(K = 2000 * 10, G = 8)
print(htpb.display)