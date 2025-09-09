import numpy as np
import matplotlib.pyplot as plt

def fDrawSector(dR, dCenter):
    # Calcula os vértices do hexágono
    vtHex = []
    for ie in range(6):
        angle = (ie) * np.pi / 3
        x = dR * np.cos(angle)
        y = dR * np.sin(angle)
        vtHex.append(x + 1j * y)  # número complexo, como no MATLAB

    vtHex = np.array(vtHex) + (dCenter[0] + 1j * dCenter[1])

    # Fecha o polígono
    vtHexp = np.append(vtHex, vtHex[0])

    # Plota
    plt.plot(vtHexp.real, vtHexp.imag, 'k')
    plt.axis('equal')
