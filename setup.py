from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='docython',
    version='0.1.0',
    author='Fleep',
    author_email='veryfleep@gmail.com',
    description='Docython - auto docs for your classes/methods/functions',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/fleepy4/docython/',
    packages=find_packages(),
    install_requires=[],
    keywords='doc docs documentation docython',
    project_urls={
        'Documentation': 'https://github.com/fleepy4/docython/'
    },
)
