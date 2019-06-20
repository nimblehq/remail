from setuptools import find_packages
from setuptools import setup

config = {
    'name': 'remail',
    'version': '0.1',
    'author': 'Jean Tadebois',
    'author_email': 'jean@nimblehq.co',
    'maintainer': 'Jean Tadebois',
    'maintainer_email': 'jean@nimblehq.co',
    'packages': find_packages(),
    'scripts': ['bin/remail'],
    'platforms': ['Linux', 'MacOs', 'Windows'],
    'url': 'https://github.com/jean-t86/remail',
    'license': 'All rights reserved',
    'description': __doc__,
    'long_description': 'A python script to act as a stage in a Jenkins CI to draft a release email',
    'long_description_content_type': 'text/markdown',
    'install_requires': [
    ],
    'include_package_data': True,
    'keywords': ['Nimble', 'Mobile Apps', 'Release', 'Script'],
    'classifiers': ['Development Status :: 2 - Pre-Alpha',
                    'Environment :: Console',
                    'Intended Audience :: Developers',
                    'License :: Copyright (c) 2019 Nimble. All rights reserved.',
                    'Natural Language :: English',
                    'Programming Language :: Python :: 3.7',
                    'Topic :: Software Development',
                    'Topic :: Utilities'],
    'zip_safe': False,
}

setup(**config)
