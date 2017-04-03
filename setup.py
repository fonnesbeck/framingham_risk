from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='frs',
      version='0.0.1',
      description=u"Framingham risk score calculation",
      long_description="""""",
      classifiers=[],
      keywords='',
      author=u"Chris Fonnesbeck",
      author_email='chris.fonnesbeck@vanderbilt.edu',
      url='https://github.com/fonnesbeck/framingham_risk',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'numpy'
      ],
      extras_require={
          'test': ['pytest'],
      }
      )
