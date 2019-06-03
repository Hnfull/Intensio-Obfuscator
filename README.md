# Intensio-Obfuscator (unstable version)

![](https://img.shields.io/badge/Python-3.6-blue.svg)
![](https://img.shields.io/badge/Version-1.0.0-green.svg)

- Changing a python source code into an python obfuscated code

### Requirement
- Python >= 3.5

### Files supported
- Files written in python 2.x and 3.x 

### Features
| Feature | Description |
| ------ | ------ |
| Replace | Replace all variables defined |
| Padding | Add random scripts in after each line |
| Remove | Remove all commentaries and all new Lines (\n) |
| Secret | Only for the curious :) |
| Mixer lower | Generate variables with 32 chars that replace variables defined in source code and in random scripts  |
| Mixer medium | Generate variables with 64 chars that replace variables defined in source code and in random scripts |
| Mixer high | Generate variables with 128 chars that replace variables defined in source code and in random scripts  |

### Usages
```
-h, --help              -> show this help message and exit.
-f, --onefile           -> if only one file.
-d, --multiplefiles     -> if multiple files (project).
-i, --input             -> source file or directory - if multiple files indicate a directory that contain all your files.
-c, --code              -> language used in input file or directory. value: [python]
-o, --output            -> output file or directory that will be obfuscated - if multiple file indicate a empty directory that will contain all your files.
-m, --mixer             -> length level of variables mix output. values: [lower,medium,high]
-r, --replace           -> activate the 'replace' obfuscation feature.
-p, --padding           -> activate the 'padding' obfuscation feature.
-rm, --remove           -> activate the 'remove' obfuscation feature.
-s, --secret            -> activate the 'secret' bullshit feature.
```
- If you want exclude variables edit `intensio/excluded_variables.txt`

### Examples
#### Python target file(s):
-  One file basic: `python3.x intensio_obfuscator.py -f -i test/python/onefile/basic/input/input_test_file.py -c python -o test/python/onefile/basic/output/output_test_file.py -m lower -r -rm`
    - [source file](https://github.com/Hnfull/Intensio-Obfuscator/blob/master/intensio/test/python/onefile/basic/input/input_test_file.py)
    - [output file](https://github.com/Hnfull/Intensio-Obfuscator/blob/master/intensio/test/python/onefile/basic/output/output_test_file.py)
- One file advanced: `python3.x intensio_obfuscator.py -f -i test/python/onefile/advanced/input/input_test_file.py -c python -o test/python/onefile/advanced/output/output_test_file.py -m high -r -p -rm`
    - [source file](https://github.com/Hnfull/Intensio-Obfuscator/tree/master/intensio/test/python/onefile/advanced/input/input_test_file.py)
    - [output file](https://github.com/Hnfull/Intensio-Obfuscator/blob/master/intensio/test/python/onefile/advanced/output/output_test_file.py)

- Multiple files basic: `python3.x intensio_obfuscator.py -d -i test/python/multiplefiles/basic/input/basicRAT -c python -o test/python/multiplefiles/basic/output/basicRAT -m lower -r -rm`
    - [source directory](https://github.com/Hnfull/Intensio-Obfuscator/tree/master/intensio/test/python/multiplefiles/basic/input/basicRAT)
    - [output directory](https://github.com/Hnfull/Intensio-Obfuscator/tree/master/intensio/test/python/multiplefiles/basic/output/basicRAT)
- Multiple files advanced: `python3.x intensio_obfuscator.py -d -i test/python/multiplefiles/advanced/input/basicRAT -c python -o test/python/multiplefiles/advanced/output/basicRAT -m high -r -p -rm`
    - [source directory](https://github.com/Hnfull/Intensio-Obfuscator/tree/master/intensio/test/python/multiplefiles/advanced/input/basicRAT)
    - [output directory](https://github.com/Hnfull/Intensio-Obfuscator/tree/master/intensio/test/python/multiplefiles/advanced/output/basicRAT)

### Possible malfunctions
- If a variable has an identical name with a text between ' ' or " " in print() function, your text will have the same value that the mixer variable
 
### Upcoming features 
- Version 1.0.1-9:
    - Code optimization
    - Obfuscate files name
    - Fix bugs and problems
    - Improved features already present
    - Adding (https://github.com/nathanlopez/basicRAT) to multiple test files example
    
- Version 1.1.0:
    - Support files written in C
    
- Version 1.2.0:
    - Support files written in C++

### Disclamer
- Intensio-Obfuscator is for education/research purposes only. The author takes NO responsibility ay for how you choose to use any of the tools provided
