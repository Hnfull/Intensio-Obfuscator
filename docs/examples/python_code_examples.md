# Examples Python target files

## Basic RAT example project

- **Basic obfuscation**
- (`replace` variables/classes/functions with strings of 32 chars)
  - ` python3.x intensio_obfuscator.py -i test/python/basic/input/basicRAT-example -o test/python/basic/output/basicRAT-example -m lower -rts`
      - [source directory of project](../../intensio/test/python/basic/input/basicRAT-example)
      - [output directory of project](../../intensio/test/python/basic/output/basicRAT-example)


- **Intermediate obfuscation** 
- (`replace` all names of variables/classes/functions - `Add` padding (random python code) with strings of 64 chars) - `replace` all files names)
  - `python3.x intensio_obfuscator.py -i test/python/intermediate/input/basicRAT-example -o test/python/intermediate/output/basicRAT-example -m medium -rts -ps -rfn`
      - [source directory of project](../../intensio/test/python/intermediate/input/basicRAT-example)
      - [output directory of project](../../intensio/test/python/intermediate/output/basicRAT-example)


- **Advanced obfuscation** 
- (`replace` all names of variables/classes/functions - `add` padding (random python script) with strings of 128 chars - `replace` all files names - `replace` all chars by their hexadecimal value)
  - `python3.x intensio_obfuscator.py -i test/python/advanced/input/basicRAT-example -o test/python/advanced/output/basicRAT-example -m high -rts -ps -rfn -rth`
      - [source directory of project](../../intensio/test/python/advanced/input/basicRAT-example)
      - [output directory of project](../../intensio/test/python/advanced/output/basicRAT-example)


