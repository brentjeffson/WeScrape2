import setuptools

with open("README.md", "rt") as f:
    long_description = f.read()

setuptools.setup(
    name="WebScrape2",
    version="1.0.0",
    author="Brent Jeffson Florendo",
    author_email="brentjeffson@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brentjeffson/WeScrape",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License ",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)