from setuptools import setup, find_packages

setup(
    name='wiki_synonyms',
    version='0.5.0',
    description='Python package for Wiki synonyms',
    url='https://github.com/iis-research-team/wiki-synonyms',
    author='IIS Research Team',
    author_email='bruches@bk.ru',
    license='MIT',
    packages=find_packages(include=['wiki_synonyms', 'wiki_synonyms.*']),
    data_files=[('wiki_synonyms.data', [
        'wiki_synonyms/data/synonyms_1.json',
        'wiki_synonyms/data/synonyms_2.json',
        'wiki_synonyms/data/synonyms_3.json',
        'wiki_synonyms/data/synonyms_4.json'
    ])],
    include_package_data=True,
    install_requires=[
                      'numpy',
                      ],
)
