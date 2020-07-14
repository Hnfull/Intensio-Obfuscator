# basicRAT-example for Test

- Source (https://github.com/nathanlopez/basicRAT)

**Disclaimer: This RAT Test is for research purposes only, and should only be used on authorized systems. Accessing a computer system or network without authorization or explicit permission is illegal.**

## Features
* Cross-platform
* AES CBC encrypted C2 with D-H exchange
* Reverse shell
* File upload/download
* Standard utilities (wget, unzip)
* System survey

## Usage
```
$ python basicRAT_server.py --port 1337

basicRAT server listening on port 1337...

[127.0.0.1] basicRAT> help

download <files>    - Download file(s).
help                - Show this help menu.
persistence         - Apply persistence mechanism.
quit                - Gracefully kill client and server.
rekey               - Regenerate crypto key.
run <command>       - Execute a command on the target.
scan <ip>           - Scan top 25 ports on a single host.
survey              - Run a system survey.
unzip <file>        - Unzip a file.
upload <files>      - Upload files(s).
wget <url>          - Download a file from the web.

```

## Build a stand-alone executable
Keep in mind that before building you will likely want to modify both the `HOST` and `PORT` variables located at the top of `basicRAT_client.py` to fit your needs.

On Linux you will need Python 2.x, [PyInstaller](http://www.pyinstaller.org/), and pycrypto. Then run something like `pyinstaller2 --onefile basicRAT_client.py` and it should generate a `dist/` folder that contains a stand-alone ELF executable.

On Windows you will need Python 2.x, PyInstaller, pycrypto, pywin32, and pefile. Then run something like `C:\path\to\PyInstaller-3.2\PyInstaller-3.2\pyinstaller.py --onefile basicRAT_client.py` and it should generate a `dist/` folder that contains a stand-alone PE (portable executable).

## Authors
* Austin Jackson [@vesche](https://github.com/vesche)
* Skyler Curtis [@deadPix3l](https://github.com/deadPix3l)
