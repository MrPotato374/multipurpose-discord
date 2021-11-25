from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="multipurpose-discord",
    author="MrPotato",
    url="",
    version='0.0.1',
    packages=['multipurposediscord'],
    license='MIT',
    description="A package made for multipurpose stuff!",
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=[],
    python_requires='>=3.5.3',
    include_package_data=True,
    keywords=[
        'discord.py', 
        'discord', 
        'discord-multipurpose'
    ]
)