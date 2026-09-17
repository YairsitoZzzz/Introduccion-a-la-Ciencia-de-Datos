# Resumen para continuar la clase de Ciencia de Datos

## Contexto general
Estoy trabajando una práctica de Ciencia de Datos con el conjunto **Global Land Temperature (GLT)**.

Archivo usado:
- `GLT_filtrado.csv`

Quiero que las explicaciones sean detalladas, paso a paso, explicando:
- qué pide cada ejercicio;
- a qué tema de Ciencia de Datos corresponde;
- qué hace cada línea de código;
- por qué se usa cada función;
- qué representa el resultado.

## Datos del archivo
El archivo `GLT_filtrado.csv` tiene:

- **219,575 filas**
- **7 columnas originales**
- **100 ciudades distintas**
- **49 países distintos**
- Fechas desde **1817-01-01** hasta **2012-12-01**

Columnas originales:

1. `Date`
   - Fecha de la medición.
   - Originalmente Pandas la lee como texto (`object`).

2. `AverageTemperature`
   - Temperatura media.
   - Variable numérica continua (`float64`).

3. `AverageTemperatureUncertainty`
   - Incertidumbre de la temperatura media.
   - Variable numérica continua (`float64`).

4. `City`
   - Ciudad.
   - Variable categórica/texto (`object`).

5. `Country`
   - País.
   - Variable categórica/texto (`object`).

6. `Latitude`
   - Latitud.
   - Conceptualmente numérica, pero viene como texto porque contiene `N` o `S`.

7. `Longitude`
   - Longitud.
   - Conceptualmente numérica, pero viene como texto porque contiene `E` o `W`.

Valores faltantes:
- `AverageTemperature`: **27,581 NaN**
- `AverageTemperatureUncertainty`: **27,581 NaN**

Las demás columnas no tienen valores faltantes.

---

# Lo que se ha visto hasta ahora

## 1. Cargar el archivo con Pandas

```python
import pandas as pd

df = pd.read_csv('/content/GLT_filtrado.csv', encoding='utf-8')
```

### Conceptos
- `pandas` es una biblioteca para trabajar con datos tabulares.
- `pd` es el alias habitual para Pandas.
- `pd.read_csv()` lee un archivo CSV.
- `df` significa normalmente **DataFrame**, la tabla principal con los datos.

Para inspeccionar los datos se pueden usar:

```python
df.head()
df.info()
df.dtypes
df.shape
```

### Resultados importantes

```python
df.shape
```

da:

```python
(219575, 7)
```

Es decir:
- 219,575 entradas o filas.
- 7 atributos o columnas.

Para saber cuántas ciudades distintas hay:

```python
df['City'].nunique()
```

Resultado:

```python
100
```

---

# 2. Convertir `Date` a fecha y crear `Year`

Código:

```python
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
```

## Explicación

### Primera línea

```python
df['Date'] = pd.to_datetime(df['Date'])
```

Convierte la columna `Date` de texto a un tipo de fecha (`datetime`).

Antes:
- `Date` era `object`.

Después:
- pasa a ser `datetime64[ns]`.

Esto permite trabajar con:
- años;
- meses;
- días;
- orden cronológico;
- filtros por fecha.

### Segunda línea

```python
df['Year'] = df['Date'].dt.year
```

Extrae solamente el año de cada fecha y crea una nueva columna llamada `Year`.

Ejemplo:

```text
Date        Year
1849-01-01  1849
1849-02-01  1849
1850-01-01  1850
```

Después de crear `Year`, el DataFrame tiene **8 columnas**.

---

# 3. Filtrar una ciudad

En la práctica se usa México:

```python
ciudad = 'Mexico'
d = df[df['City'] == ciudad]
print("Filas:", len(d))
```

## Explicación

```python
ciudad = 'Mexico'
```

Guarda el texto `"Mexico"` en la variable `ciudad`.

```python
df['City'] == ciudad
```

Compara fila por fila si la ciudad es igual a `"Mexico"`.

La comparación produce valores booleanos:

```text
True
False
True
...
```

Después:

```python
df[df['City'] == ciudad]
```

conserva solamente las filas donde la condición es `True`.

El resultado se guarda en:

```python
d
```

Por tanto:
- `df` sigue conteniendo todas las ciudades.
- `d` contiene solamente la ciudad seleccionada.

Para México:

```python
len(d)
```

da:

```python
2136
```

Por tanto, hay:

**2,136 registros de la ciudad `Mexico`.**

Importante:
- `=` es asignación.
- `==` es comparación de igualdad.

---

# 4. Calcular la temperatura media anual

Código:

```python
media_anual = d.groupby('Year')['AverageTemperature'].mean()
print(media_anual.head())
```

## Conceptos
Este ejercicio corresponde a:
- agrupación de datos;
- estadística descriptiva;
- media aritmética.

La media se define como:

\[
\bar{T} = \frac{T_1 + T_2 + \cdots + T_n}{n}
\]

## Explicación del código

```python
d.groupby('Year')
```

Agrupa todas las filas de `d` según su año.

Después:

```python
['AverageTemperature']
```

selecciona únicamente la columna de temperaturas.

Finalmente:

```python
.mean()
```

calcula el promedio de las temperaturas disponibles para cada año.

Por tanto:

```python
d.groupby('Year')['AverageTemperature'].mean()
```

significa:

> Agrupa los datos de la ciudad por año, selecciona la temperatura media y calcula el promedio de cada año.

Los valores `NaN` son ignorados automáticamente por `.mean()`.

El resultado `media_anual` es una Serie donde:
- el índice son los años;
- los valores son las temperaturas medias anuales.

Ejemplo conceptual:

```text
Year
1835    ...
1836    ...
1837    ...
...
2012    ...
```

---

# 5. Graficar la temperatura media anual

Código:

```python
import matplotlib.pyplot as plt

plt.figure()
plt.plot(media_anual.index, media_anual.values, marker='o')
plt.title('Temperatura media anual en Mexico')
plt.xlabel('Año')
plt.ylabel('Temperatura')
plt.show()
```

## Concepto
Este punto corresponde a **visualización de datos**.

## Explicación

```python
import matplotlib.pyplot as plt
```

Importa el módulo `pyplot` de Matplotlib y usa el alias `plt`.

```python
plt.figure()
```

Crea una nueva figura.

```python
plt.plot(media_anual.index, media_anual.values, marker='o')
```

Dibuja la gráfica.

- `media_anual.index` contiene los años.
- `media_anual.values` contiene las temperaturas medias.
- `marker='o'` dibuja un círculo en cada punto.

Así:

\[
x = \text{Año}
\]

\[
y = \text{Temperatura media anual}
\]

Cada punto representa la temperatura promedio de un año, no una medición mensual individual.

```python
plt.title('Temperatura media anual en Mexico')
```

Agrega el título.

```python
plt.xlabel('Año')
```

Etiqueta el eje horizontal.

```python
plt.ylabel('Temperatura')
```

Etiqueta el eje vertical.

```python
plt.show()
```

Muestra la gráfica.

Una mejora opcional es usar la variable `ciudad` en el título:

```python
plt.title(f'Temperatura media anual en {ciudad}')
```

Así, si se cambia la ciudad, el título también cambia automáticamente.

---

# Código completo trabajado hasta ahora

```python
import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo
df = pd.read_csv('/content/GLT_filtrado.csv', encoding='utf-8')

# Convertir Date a fecha
df['Date'] = pd.to_datetime(df['Date'])

# Crear columna Year
df['Year'] = df['Date'].dt.year

# Filtrar una ciudad
ciudad = 'Mexico'
d = df[df['City'] == ciudad]

print("Filas:", len(d))

# Calcular temperatura media anual
media_anual = d.groupby('Year')['AverageTemperature'].mean()

print(media_anual.head())

# Graficar
plt.figure()

plt.plot(
    media_anual.index,
    media_anual.values,
    marker='o'
)

plt.title(f'Temperatura media anual en {ciudad}')
plt.xlabel('Año')
plt.ylabel('Temperatura')

plt.show()
```

---

# Flujo lógico completo de la práctica hasta ahora

```text
GLT_filtrado.csv
        ↓
leer con Pandas
        ↓
DataFrame df
        ↓
convertir Date a datetime
        ↓
crear Year
        ↓
filtrar una ciudad
        ↓
DataFrame d
        ↓
agrupar por Year
        ↓
calcular media de AverageTemperature
        ↓
media_anual
        ↓
graficar Año vs Temperatura media anual
```

---

# Para continuar en otro chat

Si continúo esta práctica en otro chat, debo adjuntar nuevamente el archivo:

`GLT_filtrado.csv`

y pegar este resumen.

El siguiente chat debe asumir que ya entiendo de manera básica:

- `pd.read_csv()`
- DataFrames
- `df.head()`
- `df.info()`
- `df.dtypes`
- `df.shape`
- `nunique()`
- `pd.to_datetime()`
- `.dt.year`
- filtros booleanos con `df[...]`
- diferencia entre `=` y `==`
- `groupby()`
- selección de columnas con `['columna']`
- `.mean()`
- `media_anual.index`
- `media_anual.values`
- conceptos básicos de Matplotlib:
  - `plt.figure()`
  - `plt.plot()`
  - `plt.title()`
  - `plt.xlabel()`
  - `plt.ylabel()`
  - `plt.show()`

Quiero seguir resolviendo ejercicios relacionados con este mismo archivo y estos conceptos, manteniendo explicaciones detalladas, especialmente cuando aparezca código nuevo.
