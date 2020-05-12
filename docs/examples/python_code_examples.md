# Examples Python target files

## Basic RAT example project

- **Basic obfuscation**
- Defined `length` of random strings generated to `32` chars - `replace` all names of variables/classes/functions
  - `python3.x intensio_obfuscator.py -i examples/python/basic/input/basicRAT-example -o examples/python/basic/output/basicRAT-example -mlen lower -ind 4 -rts`
      - [source directory of project](../../intensio/examples/python/basic/input/basicRAT-example)
      - [output directory of project](../../intensio/examples/python/basic/output/basicRAT-example)


- **Intermediate obfuscation** 
- Defined `length` of random strings generated to `64` chars - `replace` all names of variables/classes/functions - `padding` random python scripts - `replace` all files names
  - `python3.x intensio_obfuscator.py -i examples/python/intermediate/input/basicRAT-example -o examples/python/intermediate/output/basicRAT-example -mlen medium -ind 4 -rts -ps -rfn`
      - [source directory of project](../../intensio/examples/python/intermediate/input/basicRAT-example)
      - [output directory of project](../../intensio/examples/python/intermediate/output/basicRAT-example)


- **Advanced obfuscation** 
- Defined `length` of random strings generated to `128` chars - `replace` all names of variables/classes/functions - `padding` random python scripts - `replace` all files names - `replace` all chars by their hexadecimal value
  - `python3.x intensio_obfuscator.py -i examples/python/advanced/input/basicRAT-example -o examples/python/advanced/output/basicRAT-example -mlen high -ind 4 -rts -ps -rfn -rth`
      - [source directory of project](../../intensio/examples/python/advanced/input/basicRAT-example)
      - [output directory of project](../../intensio/examples/python/advanced/output/basicRAT-example)


