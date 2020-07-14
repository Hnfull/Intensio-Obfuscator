# Required code format

### 1) When [-rts, --replacetostr] is called
- Do not define your names of local `variables/classes/functions` in your source program identically to `functions/classes/parameters-of-function` names of imported libraries
    - Can generate an error = **yes**
        - **Recommended:**
            ```python
            import argparse
            self.parser.add_argument("-t", "--test")
            yourChoices = input("number :")
            print(yourChoices)

            # 'yourChoices' variable defined have not the same name with function or parameter of function/class of argparse library, so 'add_arguments' will not be replaced by [-rts --replacetostr] feature
            
            # If you cannot change the source code edit an file and write all words that will you want to exclude (see src/intenso_obfuscator/exclude_examples/exclude_words_by_user.txt template '--excludewords' parameter)
            ```

        - **Not recommended:**
            ```python
            import argparse
            self.parser.add_argument("-t", "--test")
            add_argument = input("number :") # Line of error
            print(add_argument)

            # 'add_argument' variable defined is already a name of function of argparse library, all 'add_arguments' will be replaced by [-rts --replacetostr] feature
            ```

- You must exclude the name of functions/classes/parameter-of-function of imported libraries into your source program
    - Can generate an error = **yes**
        - **Recommended:**
            ```python
            import argparse
            self.parser.add_argument("-t", "--test", choices=["test1, test2"], default="test1", help="this is a test !")
            yourChoices = input("number :")
            print(yourChoices)
            
            # The [-rts --replacetostr] feature will replace the 'choices', 'default' and 'help' parameters of 'add_argument' function from argparse library, because their syntaxes is -> 'parameter=', except if you have exclude their words in a specific file (see src/intenso_obfuscator/exclude_examples/exclude_words_by_user.txt template and '--excludewords' parameter)
            ```
            - Edit an specific file (see `src/intenso_obfuscator/exclude_examples/exclude_words_by_user.txt` template and `--excludewords` parameter) and add `choices`, `default` and `help` parameters