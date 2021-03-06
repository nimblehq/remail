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
        'cachetools>=3.1.1',
        'certifi>=2019.6.16',
        'chardet>=3.0.4',
        'google-api-python-client>=1.7.9',
        'google-auth>=1.6.3',
        'google-auth-httplib2>=0.0.3',
        'google-auth-oauthlib>=0.4.0',
        'httplib2>=0.13.0',
        'idna>=2.8',
        'oauthlib>=3.0.1',
        'pyasn1>=0.4.5',
        'pyasn1-modules>=0.2.5',
        'requests>=2.22.0',
        'requests-oauthlib>=1.2.0',
        'rsa>=4.0',
        'six>=1.12.0',
        'uritemplate>=3.0.0',
        'urllib3>=1.25.3'
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
