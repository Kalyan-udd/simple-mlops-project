from setuptools import setup, find_packages


setup(

    name="Simple_mlOps_project",
    version="0.0.1",
    author="Kalyan",
    description="simple project to implement MLOps.",
    author_email="kalyansaiuddagiri22@gmail.com",
    url="https://github.com/Kalyan-udd/simple-mlops-project",
    package_dir={"":"src"},
    packages=find_packages(where="src")
)