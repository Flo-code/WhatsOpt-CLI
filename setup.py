'''
Author: Remi Lafage <remi.lafage@onera.fr>

This package is distributed under Apache 2 license.
'''

from setuptools import setup, Extension
from whatsopt import __version__

CLASSIFIERS = """
Development Status :: 4 - Beta
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: Apache Software License
Programming Language :: Python
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.6
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: Microsoft :: Windows
Operating System :: Unix
Operating System :: MacOS
"""

metadata = dict(
    name='wop',
    version=__version__,
    description='WhatsOpt web application command line client',
    author='Rémi Lafage',
    author_email='remi.lafage@onera.fr',
    license='Apache License, Version 2.0',
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
    packages=[
        'whatsopt'
    ],
    install_requires=[
        'openmdao', 'openmdao_extensions'
    ],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*',
    zip_safe=True,
    url = 'https://github.com/OneraHub/wop',
    download_url = 'https://github.com/OneraHub/wop/releases',
)

setup(**metadata)
