# Malfunctions

### 1) When [-rts, --replacetostr] is called
- If a `variable/class/function` has an identical name with a word between `' '` or `" "` in an `stdout` function
  - Can generate an error = **no**
    - **input:**
      ```python
      test = "mixer"

      print("this is a test !")
      ```

    - **output:**
      ```python
      ChrVMVxrZASDnzCcsWSmIBrfoWgQkdKD = "mixer"

      print("this is a ChrVMVxrZASDnzCcsWSmIBrfoWgQkdKD !")
      # your text will have the same value that the mixer value of `variables/class/function`
      ```

### 2) when you called  `[-rfn, --replacefilename]`
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
  	- Intensio-Obfuscator will detect a non compliant format code for obfuscation and exclude this file name automatically

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
    - Intensio-Obfuscator will detect a non compliant format code for obfuscation and exclude this file name automatically