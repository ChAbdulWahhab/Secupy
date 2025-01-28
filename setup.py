from setuptools import setup, find_packages

setup(
    name="secupy",
    version="0.1.0",
    description="A Python library for secure encryption, robust hashing, reliable communication, and advanced asymmetric encryption.",
    author="Ch. Abdul Wahab",
    author_email="ch.abdul.wahab310@gmail.com",
    url="https://github.com/ChAbdulWahhab/Secupy",
    packages=find_packages(),
    install_requires=["cryptography", "bcrypt"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
