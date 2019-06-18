# Recommendations

#### Do not define identically your names of local variables/classes/functions to python keywords or names of functions/classes of imported python libraries !

- Recommendation:
  ```
  import argparse
  self.parser.add_argument("-c", "--code", choices=["python"],default="python",help="language used in source file or directory")
  yourChoices = input("number :")
  print(yourChoices)

  # yourChoices variable defined is not a function of argparse library :)
  ```
- Not recommended
  ```
  import argparse
  self.parser.add_argument("-c", "--code", choices=["python"],default="python",help="language used in source file or directory")
  choices = input("number :")
  print(choices)

  # choices variable defined is a function of argparse library :(
  ```

#### If `#` (commentary) after a line of code, example the space betwen the end of code and `#`, is important, otherwise the 'Rcommentaries' `-rc --rcommentaries` feature will not work

- Recommendation:
  ```
  test = 'test' # it's a test

  # after 'test' a space is present :)
  ```
- Not recommended
  ```
  test = 'test'# it's a test

  # after 'test' a space is not present :(
  ```

#### All commentaries between `"""` or `'''` on multiple lines should be exactly as in source code examples.

- Recommendation:
  ```
  """
  --- Display -----
  name : test

  see the the placement of quotes :)
  """
  ```
- Not recommended
  ```
  """ --- Display -----
  name : test """

  see the the placement of quotes :(
  ```

#### If a variable containt text between `"""` or `'''` on multiple lines should be exactly as in source code examples.

- Recommendation:
  ```
  test = """
  --- Display -----
  name : test

  see the the placement of quotes :)
  """
  ```
- Not recommended
  ```
  test = """
  --- Display -----
  name : test """

  see the the placement of quotes :(
  ```
