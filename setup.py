import setuptools

import util.preprocessor

setuptools.setup(
    name='build.py',
    version='1.0.0',
    author='Ma_124',
    author_email='ma_124@outlook.com',
    description='A build system',
    long_description=util.preprocessor.include('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/Ma124/build.py',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    )
)
