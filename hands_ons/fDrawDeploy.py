import numpy as np
import matplotlib.pyplot as plt

fDrawDeploy(dR, vtBs):
    """
    Desenha setores hexagonais em torno das BSs
    dR   : raio do hexágono
    vtBs : lista/array de posições das BSs (números complexos ou tuplas (x,y))
    """
    # NÃO usar plt.figure() aqui -> assim desenha na mesma figura

    # Desenha hexágonos para cada BS
    for bs in vtBs:
        if isinstance(bs, (tuple, list)):
            fDrawSector(dR, (bs[0], bs[1]))
        else:
            fDrawSector(dR, (bs.real, bs.imag))

    # Plota posição das BSs como quadrados pretos
    x = [bs[0] if isinstance(bs, (tuple, list)) else bs.real for bs in vtBs]
    y = [bs[1] if isinstance(bs, (tuple, list)) else bs.imag for bs in vtBs]
    plt.plot(x, y, 'sk')
    plt.axis('equal')
