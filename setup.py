
from setuptools import setup, find_packages

VERSION = '0.1'

REQUIREMENTS = (
    'django>=1.4',
    'diazo==1.0',
    'webob==1.2.3',
    'repoze.xmliter==0.5',
)
TEST_REQUIREMENTS = (
)


setup(
    name="django-diazo",
    version=VERSION,
    author="Jelle Gerbrandy",
    description="Easy deployment of Diazo theming in django",
#     long_description=open('README', 'r').read(),
    url="",
    packages=find_packages(exclude=["example*"]),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
#     test_suite='runtests.runtests',
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
