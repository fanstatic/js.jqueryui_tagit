from setuptools import setup, find_packages
import os

# The version of the wrapped library is the starting point for the version number of the python package.
# In bugfix releases of the python package, add a '-' suffix and an incrementing integer.
# For example, a packaging bugfix release version 1.4.4 of the js.jquery package would be version 1.4.4-1 .

version = '2.0.24'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'jqueryui_tagit', 'test_tagit.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jqueryui_tagit',
    version=version,
    description="Fanstatic packaging of Tag-it!",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=[
        'fanstatic',
        'js.jquery',
        'js.jqueryui',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'tagit = js.jqueryui_tagit:library',
            ],
        },
    )
