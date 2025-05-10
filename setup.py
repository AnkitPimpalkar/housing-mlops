from setuptools import setup, find_packages

setup(
    name='housing_price_prediction',
    version='0.1',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'mlflow',
        'pytest'
    ],
    author='Ankit Pimpalkar',
    description='A modular housing price prediction project with MLOps practices.',
)
