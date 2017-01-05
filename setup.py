from setuptools import setup

VERSION = '1.0'
REQUIREMENTS = ['digrss>=1.0.0', 'python-telegram-bot>=5.2.0']
MODULES = []

setup(
    name='telegrss',
    version=VERSION,
    py_modules=['telegrss'],
    install_requires=REQUIREMENTS,
    url='https://github.com/cauebs/telegrss',
    download_url=('https://github.com/cauebs/telegrss/archive/master.zip'),
    keywords=['feed', 'atom', 'rss', 'telegram', 'bot'],
    maintainer='Cauê Baasch de Souza',
    maintainer_email='cauebaasch+pypi@gmail.com',
    description='telegram bot for managing feeds'
)