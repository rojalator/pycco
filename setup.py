from setuptools import setup, find_packages

description = (
    "A Python port of Docco: the original quick-and-dirty, "
    "hundred-line-long, literate-programming-style documentation "
    "generator."
)

setup(
    name="Pycco",
    version="0.8.0",
    description=description,
    author="Zach Smith",
    author_email="subsetpark@gmail.com",
    url="https://pycco-docs.github.io/pycco/",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pycco = pycco.main:main',
        ]
    },
    install_requires=['markdown', 'pygments', 'pystache', 'smartypants', 'dycco'],
    extras_require={'monitoring': 'watchdog'},
)
