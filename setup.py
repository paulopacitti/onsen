from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='onsen',
    packages=['onsen'],
    version='0.1.0',
    license='MIT',
    author='Paulo Pacitti',
    author_email='ppacitti@outlook.com',
    url='https://github.com/paulopacitti/onsen',
    description='rain sounds straight to your terminal!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={'console_scripts': ['onsen= onsen.__main__:main']},
    include_package_data=True,
    install_requires=['pygame', 'rich'],
    keywords=['rain', 'cli', 'onsen', 'rain', 'focus', 'water', 'sounds', 'white noise'],
)