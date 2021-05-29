import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def read_file(fname):
    with open(fname, "r") as f:
        return f.read()

setuptools.setup(
    name="commoncorrections",
    version="1.0.0",
    author="Rob Smith",
    author_email="robmsmt@gmail.com",
    description="A small python implementation of common ASR/Spelling corrections",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robmsmt/CommonCorrections",
    packages=setuptools.find_packages(exclude="tests",),
    package_data={'commoncorrections': ['data/cap_data.txt']},
    python_requires=">=3.6",
    test_suite="tests",
    install_requires=[
        elem.strip()
        for elem in read_file("requirements.txt").splitlines()
        if elem.strip()
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache2 License",
        "Operating System :: OS Independent",
    ],
)

#python3 -m pip install --upgrade setuptools wheel
#python3 setup.py sdist bdist_wheel
#sudo apt install twine -y
#twine upload dist/*