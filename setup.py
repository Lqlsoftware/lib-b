import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lib-b", # Replace with your own username
    version="1.0.3",
    author="Robin Lu",
    author_email="robin@lqlsoftware.cn",
    description="A library contains implements of factorization supporting multiple methods and data types",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lqlsoftware/lib-b",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4.0',
    entry_points={
        'console_scripts': [
            'libb = main:main'
        ]
    },
    scripts=['libb/main.py'],
)
