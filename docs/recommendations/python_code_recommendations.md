# Mandatory recommendations  


### 1) The `-rc --removecommentaries` (parameter by default) should not be disabled, otherwise the other features can generate errors
- Can generate an error = **yes**
- **Recommended:**
    - Not modify the default execution of this feature

- **Not recommended:**
    - Desactivate the default execution of this feature


### 2) Do not define your names of local `variables/classes/functions` in your source program identically to `functions/classes/parameters-of-function` names of imported libraries
- Can generate an error = **yes**
- **Recommended:**
    ```python
    import argparse
    self.parser.add_argument("-t", "--test")
    yourChoices = input("number :")
    print(yourChoices)

    # 'yourChoices' variable defined have not the same name with function or parameter of function/class of argparse library, so 'add_arguments' will not be replaced by [-rts --replacetostr] feature
    ```

- **Not recommended:**
    ```python
    import argparse
    self.parser.add_argument("-t", "--test")
    add_argument = input("number :") # Line of error
    print(add_argument)

    # 'add_argument' variable defined is already a name of function of argparse library, all 'add_arguments' will be replaced by [-rts --replacetostr] feature
    ```

### 3) You must exclude the parameters of the functions/classes of imported libraries into your source program otherwise they will be taken by the `-rts, --replacetostr` feature 
- Can generate an error = **yes**
- **Recommended:**
    ```python
    import argparse
    self.parser.add_argument("-t", "--test", choices=["test1, test2"], default="test1", help="this is a test !")
    yourChoices = input("number :")
    print(yourChoices)
    
    # The [-rts --replacetostr] feature will replace the 'choices', 'default' and 'help' parameters of 'add_argument' function from argparse library, because their syntaxes is -> 'parameter=', except if you have exclude their words in 'exclude_python_words.txt'
    ```
    - Edit [words exclusion](../../intensio/exclude/python/exclude_python_words.txt) and add `choices`, `default` and `help` parameters of add_argument function of argparse library


### 4) If `#` commentary after line of code, can potentially generate an error if `-rc, --removecommentaries` feature not recognize commentary correctly and remove the code of line
- Can generate an error = **no**
- **Recommended:**
    ```python
    # commentary
    test = 'test'
    ```

- **Less recommended:**
    ```python
    test = 'test'# it's a test
    ```

### 5) All commentaries between `"""` or `'''` on multiple lines should be exactly as in source code examples
- Can generate an error = **yes**
- **Recommended:**
    ```python
    """
    --- Display -----
    name : test

    see the the placement of quotes
    """
    ```

- **Not recommended:**
    ```python
    """ --- Display -----
    name : test """

    see the the placement of quotes
    ```

### 6) If a variable containt text between `"""` or `'''` on multiple lines should be exactly as in source code examples
- Can generate an error = **yes**
- **Recommended:**
    ```python
    test = """
    --- Display -----
    name : test

    see the the placement of quotes 
    """
    ```
    
- **Not recommended:**
    ```python
    test = """
    --- Display -----
    name : test """

    see the the placement of quotes 
    ```
    
### 7) If your value is between `[]` or `()` or `{}` in your source code, the `-ps, --paddingscripts` feature may react differently depending on the code written
- Can generate an error = **no**
- **Recommended**
    ```python
    # padding script here
    a = ["a", "b", "c"]
    # padding script here
    b = ("d", "e", "f")
    # padding script here
    ```

- **Less recommended**
    ```python
    # padding script here
    a = [
        "a", 
        "b", 
        "c"
        ]
    b = (
        "d", 
        "e", 
        "f"
        )
    # padding script here
    ```

### 8) If multiple variables follow on a line, the `-rts, --replacetostr` feature does not recognize a particular case
- Can generate an error = **no**
- Code example
    ```python
    prompt = input(">>")
    cmd, action = prompt.partition(' ')
    ```
- **Recommended**
    - This tool not recognize this case, you should edit [words inclusion](../../intensio/include/python/include_python_words.txt) and add your `cmd` variable, only `action` variable is replaced automaticaly


### 9) If a variables/classes/functions are not takin by `-rts, --Replacetostr` feature (optionnal)
- Can generate an error = **no**
- **Recommended:**
    - Edit [words inclusion](../../intensio/include/python/include_python_words.txt) and add your variables/classes/functions name
