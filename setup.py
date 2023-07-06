#!/usr/bin/env python3
import subprocess

from pip._internal.req import parse_requirements
from setuptools import find_packages, setup

requirements = [str(req.requirement) for req in parse_requirements('requirements.txt', session=False)]

try:
    VERSION = subprocess.check_output(['git', 'describe', '--tags']).strip()
except subprocess.CalledProcessError:
    VERSION = '0.dev'

setup(
    name="craneSimulator",
    version=VERSION,
    description="Software which was developed in the context of a project course at the TU Darmstadt. "
                "You can design, simulate and optimize a simplified construction tower crane. "
                "Sourcecode is available on Github",
    long_description=open('README.md').read(),
    url="https://github.com/castn/ce-project",
    author="castn",
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'craneSimulator = __main__:main',
        ],
    },
    zip_safe=False
)
