# Examples Python target files

## Basic RAT example project

- **Basic obfuscation**
- (defined `length` of random strings generated to `32` chars - defined obfuscation `level` of random strings generated to `simple` - `replace` variables/classes/functions with strings of 32 chars)
  - ` python3.x intensio_obfuscator.py -i test/python/basic/input/basicRAT-example -o test/python/basic/output/basicRAT-example -mlen lower -mlvl simple -rts`
      - [source directory of project](../../intensio/test/python/basic/input/basicRAT-example)
      - [output directory of project](../../intensio/test/python/basic/output/basicRAT-example)


- **Intermediate obfuscation** 
- (defined `length` of random strings generated to `64` chars - defined obfuscation `level` of random strings generated to `hard` - `replace` all names of variables/classes/functions - `padding` (random python scripts) - `replace` all files names)
  - `python3.x intensio_obfuscator.py -i test/python/intermediate/input/basicRAT-example -o test/python/intermediate/output/basicRAT-example -mlen medium -mlvl hard -rts -ps -rfn`
      - [source directory of project](../../intensio/test/python/intermediate/input/basicRAT-example)
      - [output directory of project](../../intensio/test/python/intermediate/output/basicRAT-example)


- **Advanced obfuscation** 
- (defined `length` of random strings generated to `128` chars - defined obfuscation `level` of random strings generated to `hard` - `replace` all names of variables/classes/functions - `padding` (random python scripts) - `replace` all files names - `replace` all chars by their hexadecimal value)
  - `python3.x intensio_obfuscator.py -i test/python/advanced/input/basicRAT-example -o test/python/advanced/output/basicRAT-example -mlen high -mlvl hard -rts -ps -rfn -rth`
      - [source directory of project](../../intensio/test/python/advanced/input/basicRAT-example)
      - [output directory of project](../../intensio/test/python/advanced/output/basicRAT-example)


