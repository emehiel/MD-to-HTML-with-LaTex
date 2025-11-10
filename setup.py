from setuptools import setup

setup(
    name='mdx_latex',
    version='0.1',
    packages=['mdx_latex'],
    install_requires=['markdown>=3.0'],
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python-Markdown extension for LaTeX math equations',
    license='MIT',
    keywords='markdown latex math equations',
    url='http://example.com/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Markup',
    ],
)