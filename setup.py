try:
    import setuptools as s
except ImportError:
    import distutils.core as s

import sys

config = {
    'name' : 'ServiceDeskAid',
    'include_package_data' : True,
    'zip_safe' : False,
    'packages' : s.find_packages(),
    'install_requires': [
        'flask',
        'flask-restful',
        'flask-mongoalchemy',
        'flask-login',
    ],
}

s.setup(**config)
