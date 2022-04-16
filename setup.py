# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ntfsvc']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.27.1,<3.0.0', 'types-requests>=2.27.17,<3.0.0']

setup_kwargs = {
    'name': 'ntfsvc-client',
    'version': '0.1.0',
    'description': 'Notification Service client.',
    'long_description': None,
    'author': 'Nick Ng',
    'author_email': 'ngyewch@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

