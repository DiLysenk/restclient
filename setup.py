from distutils.core import setup

REQUIRES = [
    'requests',
    'structlog',
    'curlify',
    'allure-pytest'
]

setup(
    name='restclient',
    version='0.0.2',
    packages=['restclient'],
    url='https://github.com/ValeriyMenshikov/restclient.git',
    license='MIT',
    author='Valeriy Menshikov',
    author_email='-',
    install_requires=REQUIRES,
    description='restclient with allure and logger'
)
