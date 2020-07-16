from pathlib import Path
import setuptools

project_dir = Path(__file__).parent

with open("pypi_README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
                name="intensio_obfuscator",
                version="1.0.10.5",
                author="hnfull",
                author_email="gitland@protonmail.com",
                keywords=["python"],
                description="Obfuscate a python code 2.x and 3.x ",
                long_description=long_description,
                long_description_content_type="text/markdown",
                url="https://github.com/Hnfull/Intensio-Obfuscator",
                packages=setuptools.find_packages("src"),
                package_dir={"": "src"},
                include_package_data=True,
                install_requires=project_dir.joinpath("requirements.txt").read_text().split("\n"),
                license="MIT",
                license_files=["LICENSE.txt"],
                zip_safe=False,
                classifiers=[
                            "Programming Language :: Python :: 3",
                            "License :: OSI Approved :: MIT License",
                            "Operating System :: OS Independent"
                ],
                python_requires=">=3.5",
                entry_points={"console_scripts": ["intensio_obfuscator=intensio_obfuscator.intensio_obfuscator:main"]}
)
