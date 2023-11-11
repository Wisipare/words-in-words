from setuptools import setup

setup(
    name='words-in-words',
    version='0.1',
    packages=['mi_app'],
    install_requires=[
        'python == 3.6',
        'flask == 2.0.1',      
        'jinja2 == 3.0.1'
        # Otras dependencias aquí
    ],
    entry_points={
        'console_scripts': [
            'mi_app = mi_app:main',  # Reemplaza 'mi_app' con el nombre de tu módulo principal
        ],
    },
)