# Examples Python target file(s)

## Basic RAT project

- Basic obfuscation
- (**replace** `variables/classes/functions` with strings of 32 chars)
  - ` python3.x intensio_obfuscator.py -i test/python/basic/input/basicRAT-example -c python -o test/python/basic/output/basicRAT-example -m lower -r`
      - [source directory of project](../../intensio/test/python/basic/input/basicRAT-example)
      - [output directory of project](../../intensio/test/python/basic/output/basicRAT-example)

- Intermediate obfuscation 
- (**Replace** `variables/classes/functions` and **Add** `padding (random python code)` with strings of 64 chars)
  - `python3.x intensio_obfuscator.py -i test/python/intermediate/input/basicRAT-example -c python -o test/python/intermediate/output/basicRAT-example -m medium -r -p`
      - [source directory of project](../../intensio/test/python/intermediate/input/basicRAT-example)
      - [output directory of project](../../intensio/test/python/intermediate/output/basicRAT-example)

- Advanced obfuscation 
- (**Replace** `variables/classes/functions` and **Add** `padding (random python code)` with strings of 128 chars, **Remove** all `print()` functions and **Replace** all chars by their hexadecimal value)
  - `python3.x intensio_obfuscator.py -i test/python/advanced/input/basicRAT-example -c python -o test/python/advanced/output/basicRAT-example -m high -r -p -rp -hex`
      - [source directory of project](../../intensio/test/python/advanced/input/basicRAT-example)
      - [output directory of project](../../intensio/test/python/advanced/output/basicRAT-example)


