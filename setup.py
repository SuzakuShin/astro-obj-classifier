from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='"El objetivo es desarrollar un modelo de clasificación que pueda predecir la clase de un objeto astronómico en tres grandes categorías: Estrellas, Galaxias y Cuásares en función de sus características espectrales y fotométricas. El modelo debera aprende a reconocer patrones en los datos como magnitudes en distintas bandas, redshift, patrones en el Espectro de Luz, Características Fotométricas, entre otras y luego pueda predecir la clase de un nuevo objeto que no haya visto antes."',
    author='Suzaku-Shin',
    license='',
)
