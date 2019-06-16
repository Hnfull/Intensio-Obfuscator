# Intensio-Obfuscator (Beta)

![](https://img.shields.io/badge/Python->=3.5-blue.svg)
![](https://img.shields.io/badge/Version-1.0.2-green.svg)
![](https://img.shields.io/badge/Licence-MIT-red.svg)

- Takes a python source code and transform it into an obfuscated python code, replace name of variables/classes/functions to random chars and defined length, removes comments, line breaks and add to each line a random script with an always differents values.

## Requirement
- Python >= 3.5
- requirement.txt

## Files supported
- Files written in python 2.x and 3.x 

## Installation
`git clone https://github.com/Hnfull/Intensio-Obfuscator.git`

`cd Intensio-Obfuscator/`

`pip3 install -r requirement.txt`

`cd intensio/`

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
#### Python target file(s):
- `python3.x intensio_obfuscator.py -i test/python/basic/input/basicRAT -c python -o test/python/basic/output/basicRAT -m lower -r -rm`
    - [source directory of project](https://github.com/Hnfull/Intensio-Obfuscator/tree/master/intensio/test/python/basic/input/basicRAT)
    - [output directory of project](https://github.com/Hnfull/Intensio-Obfuscator/tree/master/intensio/test/python/basic/output/basicRAT)

- `python3.x intensio_obfuscator.py -i test/python/advanced/input/basicRAT -c python -o test/python/advanced/output/basicRAT -m high -r -p -rm`
    - [source directory of project](https://github.com/Hnfull/Intensio-Obfuscator/tree/master/intensio/test/python/advanced/input/basicRAT)
    - [output directory of project](https://github.com/Hnfull/Intensio-Obfuscator/tree/master/intensio/test/python/advanced/output/basicRAT)
 
## Recommendations
- If `#` (comment) after a line of code, exaemple `test = 'test' # it's a test`, the space betwen the end of code and `#` is important, otherwise the functionality 'remove' will not work
- All comments between `"""` or `'''` on multiple lines should be exactly as in source code examples.


## Possible malfunctions
- **Do not define identically your names of local variables/classes/functions to python keywords or names of functions/classes of imported python libraries !**

- If a variable/class/function has an identical name with a word between `' '` or `" "` in `print()` function, your text will have the same value that the mixer variables/class/function.

- If a variable/class/function has an identical name with a word  in after `#` (commentary) your text will have the same value that the mixer variables/class/function.

- If you named your variables/classes/functions in the same way as python keywords or names of functions/class of imported python libraries, an error may appear. Edit `intensio/exclude/python/excluded_python_words.txt` to add the variables not to obfuscate or change your names of local variables/classes/fuctions, if your variables/classes/functions  have the same name as a keyword it, he will be obfuscated and errors will appear.


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
