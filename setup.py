import setuptools

long_description = open("README.md").read()

setuptools.setup(
    name="example-pkg-maximafinder-dschirde",
    version="0.0.1",
    author="D Schirde",
    author_email="dschirde@uni-potsdam.de",
    description="A small example package with a routine to find the index of the local maxima of a list",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/potsdam-python-workshop/git",
    packages=['maxima'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    install_requires = ['numpy >= 20', 'scipy < 15.3'],

    tests_require = ['pytest']
)
