import numpy as np
def dibujar_frontera_decision(clf, X, y, x_min, x_max, y_min, y_max):
    puntos_x = np.linspace(x_min, x_max, 300)
    puntos_y = np.linspace(y_min, y_max, 300)
    malla_x, malla_y = np.meshgrid(puntos_x, puntos_y)

    rejilla = np.c_[malla_x.ravel(), malla_y.ravel()]

    predicciones = clf.predict(rejilla).reshape(malla_x.shape)

    plt.contourf(malla_x, malla_y, predicciones, alpha=0.1)

    plt.scatter(X[:, 0], X[:, 1], c=y)
