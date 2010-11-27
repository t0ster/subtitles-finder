import os
from setuptools import setup, find_packages

import subtitles_finder


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="subtitles-finder",
    version=subtitles_finder.__version__,
    author="Roman Dolgiy",
    author_email="roman@bravetstudio.com",
    description=("Utitlity that scans your filesystem for TV Shows, "
                 "than tries to find subtitles"),
    license= "BSD",
    keywords="media subtitles srt",
    url="http://github.com/t0ster/subtitles-finder",
    packages=find_packages(),
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    scripts=['subtitles_finder/commands/find_subtitles.py'],
    install_requires=['mechanize'],
)
