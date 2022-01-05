# Always prefer setuptools over distutils
from os import path

from setuptools import find_packages, setup

import perceiverio

_PATH_HERE = path.abspath(path.dirname(__file__))


def _load_requirements(fname='requirements.txt'):
    with open(path.join(_PATH_HERE, fname), encoding='utf-8') as fp:
        reqs = [rq.rstrip() for rq in fp.readlines()]
    reqs = [ln[:ln.index('#')] if '#' in ln else ln for ln in reqs]
    reqs = [ln for ln in reqs if ln]
    return reqs


# Get the long description from the README file
# with open(path.join(_PATH_HERE, 'README.md'), encoding='utf-8') as fp:
#     long_description = fp.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
setup(
    name='perceiver-io',
    version=perceiverio.__version__,
    url=perceiverio.__homepage__,
    author=perceiverio.__author__,
    author_email=perceiverio.__author_email__,
    license=perceiverio.__license__,
    description=perceiverio.__doc__,
    long_description=perceiverio.__long_doc__,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['tests', 'tests/*']),
    keywords='perceiver-io deep-learning',
    install_requires=_load_requirements('requirements.txt'),
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Natural Language :: English',
        # How mature is this project? Common values are
        #   3 - Alpha, 4 - Beta, 5 - Production/Stable
        'Development Status :: 4 - Beta',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish
        "License :: OSI Approved :: Apache Software License",
        'Operating System :: OS Independent',
        # Specify the Python versions you support here.
        'Programming Language :: Python :: 3',
    ]
)
