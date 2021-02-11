import setuptools

setuptools.setup(
    name="deribit_ws",
    version="0.2",
    author="w3tech",
    author_email="ashitik@web3tech.ru",
    description="Player executors package",
    packages=["deribit_ws"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "ccxt",
    ],
    python_requires='>=3.7'
)
