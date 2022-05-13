from setuptools import setup, find_packages


setup(name='MMT',
      version='1.2.0',
      install_requires=[
          'numpy', 'torch', 'torchvision',
          'six', 'h5py', 'Pillow', 'scipy',
          'scikit-learn', 'metric-learn'],
      packages=find_packages(),
      )
