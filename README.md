# Intensio-Obfuscator (Beta)

![](https://img.shields.io/badge/Python->=3.5-blue.svg)
![](https://img.shields.io/badge/Version-1.0.2-green.svg)
![](https://img.shields.io/badge/Licence-MIT-red.svg)

- Takes a python source code and transform it into an obfuscated python code, replace name of variables/classes/functions to random chars and defined length, removes comments, line breaks and add to each line a random script with an always differents values.

## Requirements
- Python >= 3.5
- requirements.txt

## Files supported
- Files written in python 2.x and 3.x 

## Installation
`git clone https://github.com/Hnfull/Intensio-Obfuscator.git`

`pip3 install -r Intensio-Obfuscator/requirements.txt`

`cd Intensio-Obfuscator/intensio/`

## Features
| Features | Descriptions |
| ------ | ------ |
| Replace | Replace all names of variables/classes/functions defined and remove all line breaks |
| Padding | Add random scripts after each line and remove all line breaks |
| Remove | Remove all commentaries and all line breaks |
| Mixer lower | Generate words with 32 chars that replace variables/classes/functions defined in source code and in random scripts if 'replace' or 'padding' features are specified |
| Mixer medium | Generate words with 64 chars that replace variables/classes/functions defined in source code and in random scripts if 'replace' or 'padding' features are specified|
| Mixer high | Generate words with 128 chars that replace variables/classes/functions defined in source code and in random scripts if 'replace' or 'padding' features are specified |

## Usages
| Parameters | Descriptions |
| ------ | ------ |
| -h, --help | show this help message and exit |
| -i, --input  | source directory - indicate a directory that contain your file(s) |
| -c, --code | language used in input directory, default value: [python], possible value: [python] |
| -o, --output | output directory that will be obfuscated - indicate a empty directory that will contain your file(s) |
| -m, --mixer | length levels of the number of characters  for output variables /classes/functions, default value: [medium], possible values: [lower, medium, high] |
| -r, --replace | activate the 'replace' obfuscation feature |
| -p, --padding | activate the 'padding' obfuscation feature |
| -rm, --remove | activate the 'remove' obfuscation feature |

- If you want exclude python variables/classes/functions which will be taken by the 'replace' feature, edit `intensio/exclude/python/exclude_python_words.txt`

- If you want to include python variables/classes/functions that are not included when launching the 'replace' feature, edit `intensio/include/python/include_python_words.txt`

## Examples
- [Python target file(s)](https://github.com/Hnfull/Intensio-Obfuscator/blob/master/docs/examples/python_examples.md)

## Recommendations
- [List of recommendations](https://github.com/Hnfull/Intensio-Obfuscator/blob/master/docs/recommendations.md)

## Malfunctions
- [List of malfunctions](https://github.com/Hnfull/Intensio-Obfuscator/blob/master/docs/malfunctions.md)

## Todo
- Version 1.0.1-x:
    - Code optimization
    - Fix bugs and problems
    - Improved features already present

- Version 1.1.0:
    - Support files written in C
    
- Version 1.2.0:
    - Support files written in C++

## License
- MIT

## Disclamer
- Intensio-Obfuscator is for education/research purposes only. The author takes NO responsibility ay for how you choose to use any of the tools provided
