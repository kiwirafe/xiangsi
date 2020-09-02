import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xiangshi",
    version="2.1.0",
    author="kiwirafe",
    author_email="kiwirafe@gmail.com",
    description="中文文本相似度计算器 - 相识",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://kiwirafe.github.io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'jieba',
    ],
    python_requires='>=3.4',
)
