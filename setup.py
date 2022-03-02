from setuptools import setup, find_packages

setup(
  name='h5datacreator',
  version='1.0.0',
  description='`http://git-docker.tasakilab:5050/shikishima/h5datacreator`',
  long_description='`http://git-docker.tasakilab:5050/shikishima/h5datacreator`',
  author='Junya Shikishima',
  author_email='160442065@ccalumni.meijo-u.ac.jp',
  url='http://git-docker.tasakilab:5050/shikishima/h5datacreator',
  license='',
  packages=find_packages(),
  install_requires=[
    'numpy', 'h5py', 'opencv-python-headless'
  ],
  python_requires='>=3.6'
)
