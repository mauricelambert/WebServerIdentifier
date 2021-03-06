from setuptools import setup

setup(
    name="WebServerIdentifier",
    version="1.1.0",
    py_modules=["WebServerIdentifier"],
    install_requires=["PythonToolsKit"],
    author="Maurice Lambert",
    author_email="mauricelambert434@gmail.com",
    maintainer="Maurice Lambert",
    maintainer_email="mauricelambert434@gmail.com",
    description="This package identifies Web servers using an aggressive technique based on the maximum size of the URI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mauricelambert/WebServerIdentifier",
    project_urls={
        "Documentation": "https://mauricelambert.github.io/info/python/security/WebServerIdentifier.html",
        "Executable": "https://mauricelambert.github.io/info/python/security/WebServerIdentifier.pyz",
        "Presentation": "https://www.slideshare.net/MauriceLambert1/webmaxuriidentifierpdf",
    },
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Console",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.9",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["WebIdentify = WebServerIdentifier:main"],
    },
    keywords=[
        "ARP",
        "arpcachepoisonning",
        "arpcachepoison",
        "network",
        "ManInTheMiddle",
        "MIM",
        "Security",
        "DoS",
        "DenialOfService",
    ],
    platforms=["Windows", "Linux", "MacOS"],
    license="GPL-3.0 License",
)
