from setuptools import find_packages, setup

requirements = [
    "numpy",
    "pandas",
    "plotly",
    "jupyter",
    "jupytext",
]

dev_requirements = [
    "black==19.10b0",
    "bumpversion",
    "flake8",
    "isort",
    "pytest",
]

setup(
    name="PoePricePredictor",
    version="0.1.0",
    author="Kyle Harrison",
    author_email="kyleharrison94@hotmail.com",
    packages=find_packages(),
    license="LICENSE.md",
    description="A Python package for predicting currency prices in the game Path of Exile",
    long_description=open("README.md").read(),
    install_requires=requirements,
    extras_require={"dev": dev_requirements},
)
