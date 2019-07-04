# Intensio-Obfuscator (Beta)

![](https://img.shields.io/badge/Python->=3.5-blue.svg)
![](https://img.shields.io/badge/Version-1.0.4-green.svg)
![](https://img.shields.io/badge/Licence-MIT-red.svg)

## What is this ?
- Intensio-Obfsucator tool takes a python source code and transform it into an obfuscated python code
  - **Replace** name of variables/classes/functions to random chars and defined length
  - **Remove** commentaries, all lines breaks, all print functions
  - **Add** to each line a random script with an always differents values

## Requirements
- Python >= 3.5
- requirements.txt

## Files supported
- Files written in python 2.x and 3.x 

## Installation
`git clone https://github.com/Hnfull/Intensio-Obfuscator.git`

`pip3 install -r Intensio-Obfuscator/requirements.txt`

`cd Intensio-Obfuscator/intensio/`

`python3.x intensio_obfuscator.py --help`

## Features
| Features | Descriptions |
| ------ | ------ |
| Replace | Replace all names of variables/classes/functions defined and remove all line breaks |
| Padding | Add random scripts after each line and remove all line breaks |
| Rcommentaries | Remove all commentaries and all line breaks (this feature is executed by default) |
| Rprint | Remove all print functions and all line breaks |
| Mixerlevel lower | Generate words with 32 chars that replace variables/classes/functions defined in source code and in random scripts if 'replace' or 'padding' features are specified |
| Mixerlevel medium | Generate words with 64 chars that replace variables/classes/functions defined in source code and in random scripts if 'replace' or 'padding' features are specified|
| Mixerlevel high | Generate words with 128 chars that replace variables/classes/functions defined in source code and in random scripts if 'replace' or 'padding' features are specified |

- `Replace`, `Padding`, `Rprint` features can be executed separatly

## Usages
| Parameters | Descriptions |
| ------ | ------ |
| -h, --help | show this help message and exit |
| -i, --input  | source directory - indicate a directory that contain your file(s) |
| -c, --code | language used in input directory, default value: [python], possible value: [python] |
| -o, --output | output directory that will be obfuscated - indicate a empty directory that will contain your file(s) |
| -m, --mixerlevel | length levels of the number of characters for output variables /classes/functions, default value: [medium], possible values: [lower, medium, high] |
| -r, --replace | activate the 'replace' obfuscation feature |
| -p, --padding | activate the 'padding' obfuscation feature |
| -rc, --rcommentaries | activate the 'rcommentaries' obfuscation feature (this feature is executed by default) |
| -rp, --rprint | activate the 'rprint' obfuscation feature |
| -v, --verbose | improve verbosity |

- **Read these Documentations before to use Intensio-Obfuscator tool**
    - [Steps of usage](https://github.com/Hnfull/Intensio-Obfuscator/blob/master/docs/steps_usage/python_steps_usage.md)
    - [Recommendations](https://github.com/Hnfull/Intensio-Obfuscator/blob/master/docs/recommendations/python_code_recommendations.md)
    - [Malfunctions](https://github.com/Hnfull/Intensio-Obfuscator/blob/master/docs/malfunctions/python_code_malfunctions.md)

## Examples
- [Python target files](https://github.com/Hnfull/Intensio-Obfuscator/blob/master/docs/examples/python_code_examples.md)

## Demo
![Python target files demo](https://github.com/Hnfull/Intensio-Obfuscator/blob/master/docs/demo/intensio_obfuscator_python_files_demo.gif)

## Todo
- Version 1.0.1-x:
    - Code optimization
    - Fix bugs and problems
    - Improved features already present

- Version 1.1.x
    - Stable version for files written in python 2.x and 3.x
    - Supported files written in C

- Version 1.1.x
    - Stable version for file written in C
    - Supported files written in C++

## License
- MIT

## Disclamer
- Intensio-Obfuscator is for education/research purposes only. The author takes NO responsibility ay for how you choose to use any of the tools provided
