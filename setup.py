from setuptools import setup, find_packages

setup(name='census_income',
      version= '0.0.0',
      author='Abhishek',
      author_email='abhishekwankhade4670@gmail.com',
      packages=find_packages(),
      install_requires = ['pandas', 'numpy', 'flask'])