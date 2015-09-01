from setuptools import setup, find_packages
import dbbackup


setup(
    name='django-dbbackup',
    version='1.80.2b',
    license='BSD',
    url='https://github.com/portobit/django-dbbackup',
    keywords=['django', 'database', 'backup'],
    packages=find_packages(exclude=['tests.runtests.main']),
    test_suite='tests.runtests.main',
    classifiers=[
        'Environment :: Web Environment',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)