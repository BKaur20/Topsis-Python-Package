from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(  
  name = 'Topsis-Bisman-102017051',
  packages = ['topsis'],
  version = '1.1.3',
  license='MIT',
  description = 'Multiple Criteria Decision Making using TOPSIS',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Bisman Kaur',
  author_email = 'k.bisman16@gmail.com',
  url = 'https://github.com/BKaur20/Topsis-Python-Package.git',
  download_url = 'https://github.com/BKaur20/Topsis-Python-Package/archive/refs/heads/main.zip',
  keywords = ['topsis', 'python', 'pypi', 'csv', 'xlsx', 'xls', 'cli'],
  install_requires=[
          'numpy',
          'pandas',
      ],
  entry_points={
    'console_scripts': [
      'topsis = topsis.topsis:main'
      ]
  },
)