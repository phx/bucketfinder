import glob
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

binfiles = glob.glob('bin/*')

setuptools.setup(
    name='bucketfinder',
    version='1.2.1',
    scripts = binfiles,
    author='phx',
    author_email='phx@example.com',
    description='working version of bucket_finder.rb ruby script',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/phx/bucketfinder',
    classifiers=[
         "Programming Language :: Ruby",
         "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)
