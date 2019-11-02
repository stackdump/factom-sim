from setuptools import setup, find_packages

setup(
    name="factom-sim",
    version="0.1.1",
    author="Matthew York",
    author_email="matt.york@factom.com",
    description="",
    license='MIT',
    keywords='factom factomd factom-walletd',
    packages=find_packages(),
    include_package_data=True,
    # install_requires=requirements,
    long_description="""
    Python wrapper useful for testing
    runs Factomd simulator and factom-walletd

    uses w/ 15 sec block time & in-memory DB
    """,
    url="",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License"],
)
