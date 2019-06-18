# Malfunctions

#### Do not define identically your names of local variables/classes/functions to python keywords or names of functions/classes of imported python libraries

- Error
  ```
  import argparse
  self.parser.add_argument("-c", "--code", choices=["python"],default="python",help="language used in source file or directory")
  choices = input("number :")
  print(choices)

  # choices variable defined is a function of argparse library :( a error will appear when execute tool
  ```
  
#### If a variable/class/function has an identical name with a word between `' '` or `" "` in `print()` function, your text will have the same value that the mixer variables/class/function

- input
  ```
  test = "mixer"

  print("this is a test !")
  ```

- output
  ```
  ChrVMVxrZASDnzCcsWSmIBrfoWgQkdKD = "mixer"

  print("this is a ChrVMVxrZASDnzCcsWSmIBrfoWgQkdKD !")
  ```

#### If a variable/class/function has an identical name with a word  in after `#` (commentary) your text will have the same value that the mixer variable/class/function.

- input
  ```
  testCommentary = "commentary" # this is a testCommentary !
  ```

- output
  ```
  hGBARlTuxHnmuINAeGZyCQWesbdsZHDe = "commentary" # this is a hGBARlTuxHnmuINAeGZyCQWesbdsZHDe !
  ```
