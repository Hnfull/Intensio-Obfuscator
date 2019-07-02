# Recommendations / Malfunctions

## Recommendations

**Read all recommendations if you have an error** 

#### 1) The `-rc --rcommentaries` parameter should not be disabled, otherwise the other features can generate errors
**Can generate an error = yes**
- Recommended:
    - Weariness of the default execution of this feature

- Not recommended:
    - Desactivate of the default execution of this feature

#### 2) Do not define identically your names of local variables/classes/functions to python keywords or names of functions/classes of imported python libraries !
**Can generate an error = yes**
- Recommended:
    ```
    import argparse
    self.parser.add_argument("-c", "--code", choices=["python"],default="python",help="language used in source file or directory")
    yourChoices = input("number :")
    print(yourChoices)

    # yourChoices variable defined is not a function of argparse library :)
    ```

- Not recommended:
    ```
    import argparse
    self.parser.add_argument("-c", "--code", choices=["python"],default="python",help="language used in source file or directory")
    choices = input("number :")
    print(choices)

    # choices variable defined is a function of argparse library :(
    ```

#### 3) If `#` commentary after line of code, can potentially generate an error if Rcommentaries feature not recognize commentary correctly and remove the code of line
**Can generate an error = yes**
- Strongly Recommended (no error can appear):
    ```
    # commentary above
    test = 'test'
    ```

- Not recommended:
    ```
    test = 'test'# it's a test

    # after 'test' a space is not present :(
    ```

#### 4) All commentaries between `"""` or `'''` on multiple lines should be exactly as in source code examples
**Can generate an error = yes**
- Recommended:
    ```
    """
    --- Display -----
    name : test

    see the the placement of quotes :)
    """
    ```

- Not recommended:
    ```
    """ --- Display -----
    name : test """

    see the the placement of quotes :(
    ```

#### 5) If a variable containt text between `"""` or `'''` on multiple lines should be exactly as in source code examples
**Can generate an error = yes**
- Recommended:
    ```
    test = """
    --- Display -----
    name : test

    see the the placement of quotes :)
    """
    ```
    
- Not recommended:
    ```
    test = """
    --- Display -----
    name : test """

    see the the placement of quotes :(
    ```
    
#### 6) If your value is between `[]` or `()` or `{}` in your source code, the `padding` feature may react differently depending on the code written
**Can generate an error = no**
- Recommended
    ```
    padding here
    padding here
    a = ["a", "b", "c"]
    padding here
    b = ("d", "e", "f")
    padding here
    padding here
    ```

- Less recommended
    ```
    padding here
    padding here
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
    
    padding here
    padding here
    ```

# Malfunctions
  
#### 1) If a variable/class/function has an identical name with a word between `' '` or `" "` in `print()` function, your text will have the same value that the mixer variables/class/function
**Can generate an error = no**
- input:
  ```
  test = "mixer"

  print("this is a test !")
  ```

- output:
  ```
  ChrVMVxrZASDnzCcsWSmIBrfoWgQkdKD = "mixer"

  print("this is a ChrVMVxrZASDnzCcsWSmIBrfoWgQkdKD !")
  ```

#### 2) If a variable/class/function has an identical name with a word  in after `#` (commentary) your text will have the same value that the mixer variable/class/function.
**Can generate an error = no**
- input:
  ```
  testCommentary = "commentary" # this is a testCommentary !
  ```

- output:
  ```
  hGBARlTuxHnmuINAeGZyCQWesbdsZHDe = "commentary" # this is a hGBARlTuxHnmuINAeGZyCQWesbdsZHDe !
  ```
