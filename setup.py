import setuptools
from setuptools import setup , find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="anime_recommend_mlops",
    version="0.0.1",
    author="Your Name",
    author_email="[EMAIL_ADDRESS]",
    description="Anime Recommendation System",
    packages=setuptools.find_packages(),
    
)
