# CHANGESLOG 

## 02-06-2019
- [Upgrade] Version 1.0.0
- [Add] Repository created

## 07-06-2019
- [Upgrade] Version 1.0.1
- [Add] `include_python_words.txt`
- [Add] `exclude_python_words.txt`
- [Add] Allow execute each obfuscation features separately
- [Fix] spelling errors in README and commentaries
- [Update] Code improvement
- [Add] rules to replacement of variables - classes - functions
- [Add] rules to padding random scripts 
- [Update] one file example and multiple files example (larger project)
- [Update] README.md file improvement

## 15-06-2019
- [Upgrade] Version 1.0.2
- [Update] Path change from `include_python_words.txt` path to `include/python/include_python_words.txt`
- [Update] Path change from `exclude_python_words.txt` path to `include/python/exclude_python_words.txt`
- [Add] a display tqdm bar progress  when  `-r --replace`, `-p --padding`, `-rm --remove` features are specified
- [Update] Correcting spelling errors in `intensio_replace.py`, `intensio_obfuscation.py`, `intensio_padding.py`, `intensio_remove.py`
- [Update] Improvement of the code by adding a better management of the display of the analyzed inputs/outputs and the variables/classes/functions found
- [Remove] `-f --onfile` and `-d --multiplefiles` parameters, henceforth it is necessary to pointed a directory that containt files to obfuscate


## 17-06-2019
- [Ugrade] Version 1.0.3
- [Add] new feature `-rp --rprint` this parameter remove all print functions
- [Update] `-rm --remove` parameter to `-rc --rcommentaries` parameter to remove all commentaries
- [Add] `docs/recommendation.md` reference to all the best practices for using this tool
- [Add] `docs/malfunctions.md`  reference any known dysfunctions
- [Add] `docs/examples/python_example.md` to put all examples will follow shortly
- [Update] Code improvements
- [Fix] spelling errors

## 01-07-2019
- [Upgrade] to Version 1.0.4
- [Update] `-rc --rcommentaries`, this parameter is henceforth by executed default
- [Remove] `docs/malfunctions.md` reference any known dysfunctions, is merged with `docs/recommendation.md`
- [Add] an copy of Intensio-Obfuscator project at test obfuscation code #5
- [Add] verbose mode `-v --verbose` #9
- [Update] Improvement of the handle and detect process to all features #11
- [Update] `-m --mixer` to `-m --mixerlevel`
- [Update] Documentation Improvement
- [Update] Code improvements
- [Fix] spelling errors

## 25-07-2019
- [Upgrade] to Version 1.0.5
- [Fix] issue #17
- [Fix] issue #18
- [Fix] issue #19
- [Update] Documentation Improvement 
- [Update] color when tool Failed and Successful
- 