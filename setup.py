import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xiangsi",
    version="4.2.3",
    author="kiwirafe",
    author_email="kiwirafe@gmail.com",
    description="中文文本相似度计算器",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kiwirafe/xiangsi",
    project_urls={"Github": "https://github.com/kiwirafe/xiangsi"},
    packages=["xiangsi"],
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
        "xiangsi": ["*.txt", "*.md", "xiangsi/*",],
    },
    python_requires=">=3.4",
)
