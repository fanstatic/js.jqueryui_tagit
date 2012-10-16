from setuptools import setup, find_packages
import os

# The version of the wrapped library is the starting point for the version number of the python package.
# In bugfix releases of the python package, add a '-' suffix and an incrementing integer.
# For example, a packaging bugfix release version 1.4.4 of the js.jquery package would be version 1.4.4-1 .

version = '2.0.24-2'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

try:
    README = read('README.rst')
    TEST = read('js', 'jqueryui_tagit', 'test_tagit.txt')
    CHANGES = read('CHANGES.txt')
except IOError:
    README = TEST = CHANGES = ''

long_description = (
    README
    + '\n' +
    TEST
    + '\n' +
    CHANGES)

setup(
    name='js.jqueryui_tagit',
    version=version,
    description="Fanstatic packaging of Tag-it!",
    long_description=long_description,
    classifiers=[],
    keywords='',
    url='https://github.com/disko/js.jqueryui_tagit',
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
