import numpy as np
import matplotlib.pyplot as plt


def dibujar_divisiones(features, thresholds, indice, x_min, x_max, y_min, y_max):
    feature = features[indice]
    umbral = thresholds[indice]

    if feature == -2:
        return 1

    if feature == 0:
        plt.axvline(x=umbral, ymin=y_min / 10, ymax=y_max / 10, color='red', linestyle='--')

        izquierda = (x_min, umbral, y_min, y_max)
        derecha   = (umbral, x_max, y_min, y_max)

    else:
        plt.axhline(y=umbral, xmin=x_min / 10, xmax=x_max / 10, color='blue', linestyle='--')

        izquierda = (x_min, x_max, y_min, umbral)
        derecha   = (x_min, x_max, umbral, y_max)

    offset_izq = dibujar_divisiones(features, thresholds, indice + 1, *izquierda)
    offset_der = dibujar_divisiones(features, thresholds, indice + offset_izq + 1, *derecha)

    return offset_izq + offset_der + 1
