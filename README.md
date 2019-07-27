# Intensio-Obfuscator (Beta)

![](https://img.shields.io/badge/Python->=3.5-blue.svg)
![](https://img.shields.io/badge/Version-1.0.5-green.svg)
![](https://img.shields.io/badge/Licence-MIT-red.svg)

## What is this ?
- Intensio-Obfsucator tool takes a python source code and transform it into an obfuscated python code
  - **Replace** name of variables/classes/functions to random strings and defined length and all chars to their hexadecimal value
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
| Replace strings to strings mixed | Replace all names of variables/classes/functions defined and remove all line breaks |
| Paddings scripts | Add random scripts after each line and remove all line breaks |
| Remove commentaries | Remove all commentaries and all line breaks (this feature is executed by default) |
| Remove print | Remove all print functions and all line breaks |
| Replace strings to hex | Replace all chars to their hexadecimal value |
| Mixerlevel lower | Generate random strings of 32 chars when `replacetostr` and `paddingscripts` and `replacetohex` features are specified |
| Mixerlevel medium | Generate random strings of 64 chars when `replacetostr` and `paddingscripts` and `replacetohex` features are specified|
| Mixerlevel high | Generate random strings of 128 chars when `replacetostr`, `paddingscripts` and `replacetohex` features are specified |

- `Replace strings to strings mixed`, `Padding scripts`, `Remove print` and `Replace strings to hex` features can be executed separatly

## Usages
| Parameters | Descriptions |
| ------ | ------ |
| -h, --help | show this help message and exit |
| -i, --input  | source directory - indicate a directory that contain your file(s) |
| -c, --code | language used in input directory, default value: [python], possible value: [python] |
| -o, --output | output directory that will be obfuscated - indicate a empty directory that will contain your file(s) |
| -m, --mixerlevel |generate random strings of [lower:32|medium:64|high:128] chars when `replacetostr` and `paddingscripts` and `replacetohex` features are specified, default value: [medium], possible values: [lower, medium, high]|
| -rts, --replacetostr | activate the `replace strings to strings mixed` obfuscation feature |
| -ps, --paddingscripts | activate the `padding scripts` obfuscation feature |
| -rc, --removecommentaries | activate the `remove commentaries` obfuscation feature (this feature is executed by default) |
| -rp, --removeprint | activate the `remove print` obfuscation feature |
| -rth, --replacetohex | activate the `replace strings to hex` obfuscation feature |
| -v, --verbose | improve verbosity |

- **Read these Documentations before to use Intensio-Obfuscator tool**
    - [Steps of usage](docs/steps_usage/python_steps_usage.md)
    - [Recommendations](docs/recommendations/python_code_recommendations.md)
    - [Malfunctions](docs/malfunctions/python_code_malfunctions.md)

## Examples
- [Python target files](docs/examples/python_code_examples.md)

## Demo
![Python target files demo](docs/demo/intensio_obfuscator_python_files_demo.gif)

## Todo
- Version 1.0.1-x:
    - Code optimization
    - Fix bugs and problems
    - Improved features already present
    - See the enchancement in the section issue
    
- Version 1.1.0
    - Stable version

## License
- MIT

## Disclamer
- Intensio-Obfuscator is for education/research purposes only. The author takes NO responsibility ay for how you choose to use any of the tools provided
