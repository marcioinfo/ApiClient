import setuptools


setuptools.setup(
    name="userede",
    version="0.1.0",
    description="A package to handle rede API",
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    install_requires=["requests", "related", "curlify"],
)
