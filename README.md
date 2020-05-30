# Intensio-Obfuscator

![](https://img.shields.io/badge/Python->=3.5-blue.svg)
![](https://img.shields.io/badge/Version-1.0.9.2-green.svg)
![](https://img.shields.io/badge/Licence-MIT-red.svg)

## What is this ?
- Intensio-Obfsucator tool takes a python source code and transform it into an obfuscated python code
  - **Replace** all names of `variables/classes/functions/files-name` to random strings with length defined then all `chars` to their hexadecimal value
  - **Delete** all `comments`, all `spaces lines`
  - **Padding** random `snippets code/functions/classes` with an always differents values
  
## What purpose ?
- Provides a high level obfuscation layer to prevent or delay the reading and understanding of your python program

## Level of obfuscation
- Weak obfuscation if used alone, can be used with other types of obfuscation

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
| Features | Descriptions | Purpose of obfuscation | Compatibility with all types of python codes/syntaxes |
| ------ | ------ | ------ | ------ |
| Delete comments | Delete all comments (this feature is executed by default) | Delete potential behavioral informations | high `python files 2 & 3`|
| Delete line spaces | Delete all spaces line (this feature is executed by default) | Reduce the code visibility in clear | high `python files 2 & 3`|
| Correction padding empty classes/functions | Add padding to empty classes and functions, if the class or function contains comments only, the default feature `Delete comments` can potentially let a class or function empty, this will avoid to generate an error (this feature is executed by default) | None, only to avoid to generate errors | high `python files 2 & 3`|
| Replace string to string mixed | Replace all names of variables/classes/functions to random strings with length defined| Reduce the code visibility in clear - Delay the deduction of the behavior of variables/classes/functions | low - high (depends of number of names that must exclude or not) `python files 2 & 3`
| Padding script | Add padding of random scripts after each line| Reduce the code visibility in clear - add dead snippets code/classes/functions to blur and delay behavior analysis of program | high `python file 2 & 3`|
| Replace file name | Replace all files name to random strings with length defined | Reduce the code visibility in clear - Reduce the deduction of functionnalities of files | low `python files 2 & 3`|
| Replace string to hex | Replace all chars to their hexadecimal value | Reduce the code visibility in clear / avoid to be detected by the \'grep\' commands per example| medium `python files 2 only` |
| Correction delete pyc file | Delete all pyc file in output directory (this feature is executed by default) | Delete files already compiled without having been obfuscated before | high `python files 2 & 3`|
| Mixer length lower | Define random strings length of `32` chars when `-rts, --replacetostr` or `-ps, --paddingscripts` or `-rfn, --replacefilesname` or `-rth, --replacetohex` parameters are specified | The longer the length is used, the more difficult the visibility of the code | Information not required |
| Mixer length medium | Define random strings length of `64` chars when `-rts, --replacetostr` or `-ps, --paddingscripts` or `-rfn, --replacefilesname` or `-rth, --replacetohex` parameters are specified | The longer the length is used, the more difficult the visibility of the code | Information not required |
| Mixer length high | Define random strings length of `128` chars when `-rts, --replacetostr` or `-ps, --paddingscripts` or `-rfn, --replacefilesname` or `-rth, --replacetohex` parameters are specified | The longer the length is used, the more difficult the visibility of the code | Information not required |
- Features can be executed separatly:
    - `replace string to string mixed` -> `-rts, --replacetostr`
    - `padding script` -> `-ps, --paddingscript`
    - `replace file name` -> `-rfn, --replacefilename`
    - `replace string to hex` -> `-rth, --replacetohex`

## Usages
- **Read these Documentations before to use Intensio-Obfuscator tool !**
- **Certain types of pattern are not supported**
    - [Steps of usage](docs/steps_usage/python_steps_usage.md)
    - [Required code format](docs/recommendations/python_code_recommendations.md)
    - [Malfunctions](docs/malfunctions/python_code_malfunctions.md)
    
| Parameters | Descriptions |
| ------ | ------ |
| -h, --help | show this help message and exit |
| -i, --input  | source directory - indicate a directory that contain your file |
| -o, --output | output directory that will be obfuscated - indicate a empty directory that will contain your file |
| -mlen, --mixerlength | define length of random strings generated [`lower:32`\|`medium:64`\|`high:128`] chars when `--replacetostr` or `--paddingscripts` or `-rfn, --replacefilesname` or `--replacetohex` features are specified, possible values: [`lower`\|`medium`\|`high`]|
|-ind, --indent | indicate the indentation of your python source code, possible values: [`2`\|`4`\|`8`] 
| -rts, --replacetostr | enable `replace string to string mixed` obfuscation feature |
| -ps, --paddingscript | enable `padding script` obfuscation feature|
| -rfn, --replacefilename | enable `replace file name` obfuscation feature |
| -rth, --replacetohex | enable `replace string to hex` obfuscation `(python files 2 only)`|
| -v, --verbose | improve verbosity |

## Obfuscation examples 
- [Python files obfuscated](docs/examples/python_code_examples.md)

## Todo
- Version 1.x.x-x:
    - Code optimization
    - Fix issues
    - Improved features already present
    - Add other functionalities

## License
- MIT

## Contact
- Hnfull **gitland@protonmail.com**

## Disclamer
- Intensio-Obfuscator is for education/research purposes only. The author takes NO responsibility ay for how you choose to use any of the tools provided
