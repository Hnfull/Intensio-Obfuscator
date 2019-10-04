# Intensio-Obfuscator (Beta)

![](https://img.shields.io/badge/Python->=3.5-blue.svg)
![](https://img.shields.io/badge/Version-1.0.6-green.svg)
![](https://img.shields.io/badge/Licence-MIT-red.svg)

## What is this ?
- Intensio-Obfsucator tool takes a python source code and transform it into an obfuscated python code
  - **Replace** all names of `variables/classes/functions/files-name` to random strings with length defined and all `chars` to their hexadecimal value
  - **Remove** all `comments`, all `spaces lines`
  - **Padding** random `scripts` with an always differents values

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
| remove comment | Remove all comments (this feature is executed by default) |
| remove space line | Remove all spaces line (this feature is executed by default) |
| correction padding empty class/function | Add padding to empty classes and functions, if the class or function contains only comments, the default feature `remove comments` will leave a class or function empty, this will avoid generating an error (this feature is executed by default) |
| replace string to string mixed | Replace all names of variables/classes/functions to random strings with length defined|
| padding script | Add padding of random scripts after each line|
| replace file name | Replace all files name to random strings with length defined |
| replace string to hex | Replace all chars to their hexadecimal value |
| correction remove pyc file | Remove all pyc file in output directory (this feature is executed by default) |
| mixerlevel lower | Generate random strings of 32 chars when `-rts, --replacetostr` or `-ps, --paddingscripts` or `-rfn, --replacefilesname` or `-rth, --replacetohex` parameter are specified |
| mixerlevel medium | Generate random strings of 64 chars when `-rts, --replacetostr` or `-ps, --paddingscripts` or `-rfn, --replacefilesname` or `-rth, --replacetohex` parameter are specified |
| mixerlevel high | Generate random strings of 128 chars when `-rts, --replacetostr` or `-ps, --paddingscripts` or `-rfn, --replacefilesname` or `-rth, --replacetohex` parameter are specified |

- `replace string to string mixed` -> `-rts, --replacetostr`, `padding script` -> `-ps, --paddingscript`, `replace file name` -> `-rfn, --replacefilename`, `replace string to hex` -> `-rth, --replacetohex` features can be executed separatly

## Usages
- **Read these Documentations before to use Intensio-Obfuscator tool !**
    - [Steps of usage](docs/steps_usage/python_steps_usage.md)
    - [Required code format](docs/recommendations/python_code_recommendations.md)
    - [Malfunctions](docs/malfunctions/python_code_malfunctions.md)
    
| Parameters | Descriptions |
| ------ | ------ |
| -h, --help | show this help message and exit |
| -i, --input  | source directory - indicate a directory that contain your file |
| -o, --output | output directory that will be obfuscated - indicate a empty directory that will contain your file |
| -m, --mixerlevel | generate random strings of [ `lower:32` \| `medium:64` \| `high:128` ] chars when `--replacetostr` or `--paddingscripts` or `--replacetohex` features are specified, default value: [medium], possible values: [lower - medium - high]|
| -rts, --replacetostr | activate the `replace string to string mixed` obfuscation feature |
| -ps, --paddingscript | activate the `padding script` obfuscation feature |
| -rfn, --replacefilename | activate the `replace file name` obfuscation feature |
| -rth, --replacetohex | activate the `replace string to hex` obfuscation feature |
| -v, --verbose | improve verbosity |

## Obfuscation examples 
- [Python files obfuscated](docs/examples/python_code_examples.md)

## Todo
- Version 1.0.1-x:
    - Code optimization
    - Fix issues
    - Improved features already present
    
- Version 1.1.0-x:
    - Stable version

## License
- MIT

## Contact
- Hnfull **gitland@protonmail.com**

## Disclamer
- Intensio-Obfuscator is for education/research purposes only. The author takes NO responsibility ay for how you choose to use any of the tools provided
