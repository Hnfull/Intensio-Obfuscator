# Recommendations

#### 1) The `-rc --rcommentaries` (parameter by default) should not be disabled, otherwise the other features can generate errors
- Can generate an error = yes
- Recommended:
    - Not modify the default execution of this feature

- Not recommended:
    - Desactivate the default execution of this feature

#### 2) Do not define your names of local `variables/classes/functions` of your program identically to keywords python of `functions/classes` of imported libraries
- Can generate an error = yes
- Recommended:
    ```python
    import argparse
    self.parser.add_argument("-t", "--test")
    yourChoices = input("number :")
    print(yourChoices)

    # yourChoices variable defined is not a function or parameter of argparse library :)
    ```

- Not recommended:
    ```python
    import argparse
    self.parser.add_argument("-t", "--test")
    add_argument = input("number :") # Line of error
    print(add_argument)

    # add_argument variable defined is already an function of argparse library :(
    ```

#### 3) You ought exclude python keywords of libraries of your program which will be taken by the 'Replace' feature 
- Can generate an error = yes
- Required:
    ```python
    import argparse
    self.parser.add_argument("-t", "--test", choices=["test1, test2"], default="test1", help="this is a test !")
    yourChoices = input("number :")
    print(yourChoices)
    ```
    - Edit [words exclusion](../../intensio/exclude/python/exclude_python_words.txt) and add keywords `choices`, `default` and `help` of argparse library, because the Replace feature take all variables, with this rule `variables=`

#### 4) If `#` commentary after line of code, can potentially generate an error if `Rcommentaries` feature not recognize commentary correctly and remove the code of line
- Can generate an error = yes
- Strongly Recommended (no error can appear):
    ```python
    # commentary
    test = 'test'
    ```

- Less recommended:
    ```python
    test = 'test'# it's a test
    ```

#### 5) All commentaries between `"""` or `'''` on multiple lines should be exactly as in source code examples
- Can generate an error = yes
- Recommended:
    ```python
    """
    --- Display -----
    name : test

    see the the placement of quotes :)
    """
    ```

- Not recommended:
    ```python
    """ --- Display -----
    name : test """

    see the the placement of quotes :(
    ```

#### 6) If a variable containt text between `"""` or `'''` on multiple lines should be exactly as in source code examples
- Can generate an error = yes
- Recommended:
    ```python
    test = """
    --- Display -----
    name : test

    see the the placement of quotes :)
    """
    ```
    
- Not recommended:
    ```python
    test = """
    --- Display -----
    name : test """

    see the the placement of quotes :(
    ```
    
#### 7) If your value is between `[]` or `()` or `{}` in your source code, the `padding` feature may react differently depending on the code written
- Can generate an error = no
- Recommended
    ```python
    # padding here
    a = ["a", "b", "c"]
    # padding here
    b = ("d", "e", "f")
    # padding here
    ```

- Less recommended
    ```python
    # padding here
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
    # padding here
    ```
    
#### 8) If a variables/classes/functions are not takin by Replace feature (optionnal)
- Can generate an error = no**
- Required:
    - Edit [words inclusion](../../intensio/include/python/include_python_words.txt) and add your variables/classes/functions name
    ```
