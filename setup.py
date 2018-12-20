from distutils.core import setup

setup(
    name='pypistart',
    version='0.1.0',
    description='Starter kit for initializing a python pypi package',
    long_description=open('README.md').read(),
    author='Jack Workman',
    author_email='jworkman16@gmail.com',
    url='http://pypi.python.org/pypi/pypistart/',
    packages=['pypistart', 'pypistart.tests'],
    #scripts=[],  # TODO -- make script for creating pypi package skeleton
    license='MIT'
)
