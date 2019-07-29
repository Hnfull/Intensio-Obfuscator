# Malfunctions

#### 1) If a `variable/class/function` has an identical name with a word between `' '` or `" "` in `print()` function, your text will have the same value that the mixer `variables/class/function` if `-rts, --replacetostr` parameter is called
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
  ```

#### 2) If a `variable/class/function` has an identical name with a word in after `#` (commentary) your text will have the same value that the mixer `variable/class/function` if `-rts, --replacetostr` parameter is called
- Can generate an error = **no**
- **input:**
  ```python
  testCommentary = "commentary" # this is a test commentary !
  ```

- **output:**
  ```python
  hGBARlTuxHnmuINAeGZyCQWesbdsZHDe = "commentary" # this is a hGBARlTuxHnmuINAeGZyCQWesbdsZHDe !
  ```
