import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xiangshi",
    version="3.0.0",
    author="kiwirafe",
    author_email="kiwirafe@gmail.com",
    description="中文文本相似度计算器 - 相识",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kiwirafe/xiangshi",
    packages=["xiangshi", "xiangshi.fast"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "jieba",
    ],
    package_data = {
        # If any package contains *.txt files, include them:
        "xiangshi": ["*.txt", "*.md", "xiangshi/*",],
        "xiangshi.fast": ["*.txt", "*.md",],
    },
    python_requires=">=3.4",
)
