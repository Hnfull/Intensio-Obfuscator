# CHANGELOG of Intensio-Obfuscator project

## 03-10-2020 
- [Remove] intensio_error.py file, that contained useless feature to improve verbosity type of error during the reading of Intensio-Obfuscator code
- [Remove] `simple` level of string generated for obfuscation is removed, previous parameter` hard` level obfuscation is used by default for level of strings generated for obfuscation now
- [Remove] parameter `-mlvl, --mixerlevel` to control obfuscation level of strings generated (`simple` by default or `hard`)

## 02-01-2020
- [Update] visibility of code with PEP 8 recommandation part : `maximum line length` 

## 01-28-2020
- [Upgrade] to version 1.0.8
- [Update] `-m, -mixerlevel` becomes `-mlen, --mixerlength` to control length of random strings generated
- [Update] redefine all colors without external library
- [Fix] issue # 14
- [Fix] issue # 28
- [Add] new paramter `-mlvl, --mixerlevel` to control obfuscation level of strings generated (`simple` by default or `hard`)
 
## 01-07-2020
- [Upgrade] to version 1.0.7
- [Update] spelling error (remove becomes delete)
- [Update] name of class `Remove` to `Delete`
- [Update] name of `intensio_remove.py` to `intensio_delete.py`
- [Add] new feature to exclude file name of obfuscation #35
- [Add] `Intensio-Obfuscator/intensio/exclude/file_name/exclude_file_name_by_user.txt` allow a user to exclude file name when the `replace file name [-rfn, --replacefilename]` is called

## 10-02-2019
- [Upgrade] to version 1.0.6 
- [Update] documentation Improvement 
- [Update] improve visual quality of code
- [Update] `replace string to string mixed` feature, better detect somes code cases
- [Update] `padding script` feature, add 2 new random scripts
- [Update] change path of `Intensio-Obfuscator/intensio/exclude/python/include_python_words.txt` to `Intensio-Obfuscator/intensio/exclude/string_to_string_mixed_feature/exclude_word.txt`
- [Update] `exclude/string_to_string_mixed/exclude_words.txt`, adding several native python functions
- [Update] improve check process in `replace string to string mixed` feature and `padding script` feature with `-v, --verbose` parameter is enable
- [Update] `remove line space` feature is no longer called after each obfuscation function, henceforth now she is called only once at the beginning of the obfuscation process.
- [Update] change `print()` function that write in all file with fileinput library by sys.stdout.write function, now no space line is added after end line
- [Update] improve all regex that catch a specifique pattern in a file
- [Fix] issue #20 - no answer of user
- [Fix] issue #21 - updating `Remove comments` feature when she handle multiple quotes on one line and multiple lines \(I am waiting for the user to validate the fix\)
- [Fix] issue #22
- [Remove] `-c, --python` parameter, because is useless currently
- [Remove] demo, `docs/examples/python_code_examples.md` is enough
- [Remove] `Remove print function` feature, simpler action by the user herself
- [Remove] `Intensio-Obfuscator/intensio/include/python/include_python_words.txt` file is now useless with improve caught words in `replace string to string mixed` feature
- [Add] color and type of progress bar
- [Add] `correction padding class` feature (check if class are empty after `remove comments` feature is executed and adding padding)
- [Add] `correction padding function` feature (check if function are empty after `remove comments` feature is executed and adding padding)
- [Add] verbosity mode into `remove pyc file` feature - `padding class` feature - `padding function` feature
- [Add] check process in `replace file name` feature - `replace string to hex` feature - `padding class` feature - `padding function` feature and `remove pyc file` feature with `-v, --verbose` parameter
- [Add] `Intensio-Obfuscator/releases/` to store all old version of project 

## 07-27-2019
- [Upgrade] to version 1.0.5
- [Update] Documentation Improvement 
- [Update] color when tool Failed and Successful
- [Update] renaming all parameters and functions
- [Fix] issue #17
- [Fix] issue #18
- [Fix] issue #19
- [Add] new feature `-rth, --replacetohex`, see README.md for more informations
- [Add] new part of obfuscation `intermediate` in examples
- [Add] new feature `-rfn, --replacefilesname` see README.md for more informations
- [Add] new feature to trash all pyc files

## 07-01-2019
- [Upgrade] to version 1.0.4
- [Update] `-rc --rcomments`, this parameter is henceforth by executed default
- [Update] `-m --mixer` to `-m --mixerlevel`
- [Update] documentation Improvement
- [Fix] issue #11 - Improvement of the handle and detect process to all features
- [Remove] `docs/malfunctions.md` reference any known dysfunctions, is merged with `docs/recommendation.md`
- [Add] an copy of Intensio-Obfuscator project at test obfuscation code #5
- [Add] verbose mode `-v --verbose` #9

## 06-17-2019
- [Ugrade] version 1.0.3
- [Update] `-rm --remove` parameter to `-rc --rcomments` parameter to remove all comments
- [Add] new feature `-rp --rprint` this parameter remove all print functions
- [Add] `docs/recommendation.md` reference to all the best practices for using this tool
- [Add] `docs/malfunctions.md`  reference any known dysfunctions
- [Add] `docs/examples/python_example.md` to put all examples will follow shortly

## 06-15-2019
- [Upgrade] version 1.0.2
- [Update] Path change from `include_python_words.txt` path to `include/python/include_python_words.txt`
- [Update] Path change from `exclude_python_words.txt` path to `include/python/exclude_python_words.txt`
- [Update] Correcting spelling errors in `intensio_replace.py`, `intensio_obfuscation.py`, `intensio_padding.py`, `intensio_remove.py`
- [Update] Improvement of the code by adding a better management of the display of the analyzed inputs/outputs and the variables/classes/functions found
- [Remove] `-f --onfile` and `-d --multiplefiles` parameters, henceforth it is necessary to pointed a directory that containt files to obfuscate
- [Add] a display tqdm bar progress  when  `-r --replace`, `-p --padding`, `-rm --remove` features are specified

## 06-07-2019
- [Upgrade] version 1.0.1
- [Update] one file example and multiple files example (larger project)
- [Update] README.md file improvement
- [Add] rules to replacement of variables - classes - functions
- [Add] rules to padding random scripts 
- [Add] `include_python_words.txt`
- [Add] `exclude_python_words.txt`
- [Add] Allow execute each obfuscation features separately

## 06-02-2019
- [Upgrade] version 1.0.0
- [Add] Repository created