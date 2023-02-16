from setuptools import setup, find_packages

setup(
    name='miditoolkit_light',
    version='0.1.18',
    description='',
    author='TuneFlow',
    author_email='contact@info.tuneflow.com',
    url='https://github.com/tuneflow/miditoolkit',
    packages=find_packages(),
    package_data={'': ['examples_data/*']},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
    ],
    keywords='music midi mir',

    license='MIT',
    install_requires=[
        'numpy >= 1.7.0',
        'mido >= 1.1.16',
    ]
)


"""
python setup.py sdist
twine upload dist/*
"""