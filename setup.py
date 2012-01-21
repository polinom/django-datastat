from setuptools import setup, find_packages

setup(
    name='datastat',
    version='0.0.1',
    description='Django admin addon to display models statistic in charts.',
    long_description=open('README.rst').read(),
    author='Polynets Igor',
    author_email='polinom@gmail.com',
    url='https://github.com/polinom/django-admin-chart',
    packages=find_packages(exclude=[]),
    package_data = {'datastat': ['templates/*.html',]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
