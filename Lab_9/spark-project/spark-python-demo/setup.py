from setuptools import setup, find_packages

setup(
    name='spark_demo',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyspark'
    ],
    entry_points={
        'console_scripts': [
            'spark-demo=spark_job:main',
        ],
    }
)
