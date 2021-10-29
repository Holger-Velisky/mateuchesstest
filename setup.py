import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mateuchesstest-KATRONKA",
    version="0.0.1",
    author="Albert Mateu Carrasco",
    author_email="albertmateucarrasco@gmail.com",
    description="A test package for chess engine creation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Holger-Velisky/mateuchesstest",
    project_urls={
        "Repository": "https://github.com/Holger-Velisky/mateuchesstest",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)