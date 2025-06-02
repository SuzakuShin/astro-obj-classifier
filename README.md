# Clasificación de Objetos Astronómicos con Machine Learning

Este proyecto implementa un modelo de Machine Learning en Python con scikit-learn para clasificar objetos astronómicos utilizando datos del sondeo SDSS. El modelo aplica preprocesamiento, reducción de dimensionalidad y clasificación supervisada, complementado con un análisis no supervisado mediante K-Means.

---

## Dataset

* **Instancias:** Aproximadamente 10.000 objetos celestes.

* **Columnas (características):**

  * `objid`: identificador único del objeto
  * `ra`, `dec`: coordenadas celestes
  * `u`, `g`, `r`, `i`, `z`: magnitudes fotométricas en 5 bandas
  * `redshift`: corrimiento al rojo
  * `class`: clase del objeto (`STAR`, `GALAXY`, `QSO`)
  * `u-g`, `g-r`, `r-i`, `i-z`: colores derivados

* **Tipos de datos:**

  * Números flotantes para magnitudes y redshift
  * Categórico para la clase

---
* **Diccionario de Datos:**
  
| **Nombre de la columna** | **Tipo de dato** | **Descripción**                                           |
| ------------------------ | ---------------- | --------------------------------------------------------- |
| `objid`                  | Entero / ID      | Identificador único del objeto astronómico                |
| `ra`                     | Float64          | Ascensión recta: coordenada celeste en grados             |
| `dec`                    | Float64          | Declinación: coordenada celeste en grados                 |
| `u`                      | Float64          | Magnitud aparente en la banda ultravioleta `u`            |
| `g`                      | Float64          | Magnitud aparente en la banda verde `g`                   |
| `r`                      | Float64          | Magnitud aparente en la banda roja `r`                    |
| `i`                      | Float64          | Magnitud aparente en la banda infrarroja cercana `i`      |
| `z`                      | Float64          | Magnitud aparente en la banda infrarroja `z`              |
| `redshift`               | Float64          | Corrimiento al rojo, indica distancia relativa del objeto |
| `class`                  | Categórico       | Clase real del objeto: `STAR`, `GALAXY`, `QSO`            |
| `u-g`                    | Float64          | Diferencia de magnitudes entre bandas `u` y `g` (color)   |
| `g-r`                    | Float64          | Diferencia de magnitudes entre bandas `g` y `r` (color)   |
| `r-i`                    | Float64          | Diferencia de magnitudes entre bandas `r` y `i` (color)   |
| `i-z`                    | Float64          | Diferencia de magnitudes entre bandas `i` y `z` (color)   |
| `kmeans_labels`          | Entero (0-2)     | Etiqueta asignada por K-Means (no supervisada)            |
| `pca_1`, `pca_2`         | Float64          | Componentes principales del análisis PCA                  |


## Origen del Dataset

* **Fuente:** Sloan Digital Sky Survey
* **Sitio oficial:** [https://skyserver.sdss.org/dr18/en/tools/search/sql.aspx](https://skyserver.sdss.org/dr18/en/tools/search/sql.aspx)
* **Adquisición:** Los datos se obtuvieron mediante una consulta SQL personalizada a la base de datos pública de SDSS.

```sql
SELECT TOP 10000
    p.objid,
    p.ra,
    p.dec,
    p.u,
    p.g,
    p.r,
    p.i,
    p.z,
    s.run,
    s.rerun,
    s.camcol,
    s.specobjid,
    s.class
FROM
    PhotoObj AS p
JOIN
    SpecObj AS s ON p.objid = s.bestobjid
WHERE
    s.class IN ('STAR', 'GALAXY', 'QSO')
    AND p.u BETWEEN 0 AND 40
    AND p.g BETWEEN 0 AND 40
    AND p.r BETWEEN 0 AND 40
    AND p.i BETWEEN 0 AND 40
    AND p.z BETWEEN 0 AND 40
```

* **Preprocesamiento:**

  * Se eliminó la primera fila (metadatos)
  * Se calcularon colores fotométricos (`u-g`, `g-r`, etc.)
  * Se normalizaron los datos con `StandardScaler`
  * Se codificaron las clases con `LabelEncoder`

---

## Tecnologías utilizadas

* Python 3.10+
* Jupyter Notebook
* Pandas, NumPy
* Scikit-learn (Random Forest, PCA, KMeans, métricas)
* Matplotlib, Seaborn

---



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
