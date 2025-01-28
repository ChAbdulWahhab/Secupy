from setuptools import setup, find_packages

setup(
    name="secupy",
    version="0.1.0",
    description="A comprehensive Python library for secure encryption, hashing, communication, and asymmetric encryption.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ch. Abdul Wahhab",
    author_email="ch.abdul.wahab310@gmail.com",
    url="https://github.com/ChAbdulWahhab/Secupy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "cryptography>=3.4",
        "bcrypt>=3.2"
    ],
)
