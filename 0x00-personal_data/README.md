# Personal data

## Resources

Read or watch:
- [What Is PII, non-PII, and Personal Data?](https://piwik.pro/blog/what-is-pii-personal-data/)
- [logging documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt package](https://github.com/pyca/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://www.youtube.com/watch?v=-ARI4Cz-awo)

## Learning Objectives

At the end of this project, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:
- Examples of Personally Identifiable Information (PII).
- How to implement a log filter that will obfuscate PII fields.
- How to encrypt a password and check the validity of an input password.
- How to authenticate to a database using environment variables.

## Requirements

- All your files will be interpreted/compiled on **Ubuntu 18.04 LTS** using **python3 (version 3.7)**.
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the **pycodestyle** style (version 2.5).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have documentation:
  ```bash
  python3 -c 'print(__import__("my_module").__doc__)'
  python3 -c 'print(__import__("my_module").MyClass.__doc__)'
  python3 -c 'print(__import__("my_module").my_function.__doc__)'
  python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

