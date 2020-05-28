import setuptools

with open("README.md", "r") as fd:
    long_description = fd.read()

setuptools.setup(
    name="mock-bidder",
    version="1.0.0",
    author="Aleksey Beregov",
    author_email="alekseyberegov@gmail.com",
    description="Mock Open RTB bidder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alekseyberegov/mock-bidder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
