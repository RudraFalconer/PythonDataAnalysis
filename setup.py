from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Python Text Analysis',
    version='1.0.0',
    author='Daniel Sohm',
    author_email='daniel.sohm06.com',
    description='Twitter text analysis',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RudraFalconer/PythonDataAnalysis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires= [req.strip() for req in requirements],
)
