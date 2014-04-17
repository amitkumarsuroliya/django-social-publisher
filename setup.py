from distutils.core import setup

setup(
    name='DjangoSocialPublisher',
    version='0.0.1dev',
    packages=['social_publisher',],
    license='MIT',
    long_description=open('README.txt').read(),
    install_requires=[
        'vkontakte=1.3.2',
        'requests=2.2.1',
    ],
)