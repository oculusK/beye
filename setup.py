from setuptools import setup, find_packages

setup(
    name='BEye',
    version='0.0.1',
    description='PYPI tutorial package creation written by BEye',
    author='oculus',
    author_email='kay5990@naver.com',
    url='https://github.com/oculusK/beye',
    install_requires=['tqdm', 'pandas', 'scikit-learn',],
    packages=find_packages(exclude=[]),
    keywords=['teddynote', 'teddylee777', 'python datasets', 'python tutorial', 'pypi'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)