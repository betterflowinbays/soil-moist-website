from setuptools import setup, find_packages
from soilmoisture import __version__

setup(
    name='soilmoisture',
    version=__version__,

    url='http://host/',
    author='Mike Morris',
    author_email='mike.morris@ecodev.vic.gov.au',

    packages=find_packages(),
    include_package_data=True,
    scripts=['scripts/manage.py'],

    install_requires=(
        'django',
    )
)

