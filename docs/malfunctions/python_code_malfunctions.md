# Malfunctions

### 1) when `[-rfn, --replacefilename]` is called
- If you `import` python file
  - Can generate an error = **no**
    - **Recommended:**
        ```python
        # I have test1.py file that contain several functions or classes
        from path.test1 import get
        get("user")
        ```

    - **Not Recommended:**
        ```python
        # I have test1.py file that contain several functions or classes
        from path import test1
        test1.get("user")
        ```
  	- Intensio-Obfuscator will detect a non compliant format (currently this type of import is not supported by tool) code for obfuscation and exclude this file name automatically
    - You can exclude manually a file name [file name exclusion](../../intensio/exclude/file_name/exclude_file_name_by_user.txt) 

- If you `import` python file and in path the file name have the same name that a folder
  - Can generate an error = **no**
    - **Recommended:**
        ```python
        # I have test1.py file that contain several functions or classes
        from path.mytest.test1 import get
        get("user")
        ```

    - **Not Recommended:**
        ```python
        # I have test1.py file that contain several functions or classes
        from path.test1.test1 import get
        get("user")
        ```
    - Intensio-Obfuscator will detect a non compliant format (currently this type of import is not supported by tool) code for obfuscation and exclude this file name automatically