# python_c--_compiler
A compiler for a custom "C--" language implemented in python.

## C-- Specification
The language specifies a list of reserved words, special symbols, a specific way to structure identifiers (variable names), numbers and delimiters.

### Reserved words
- if
- else
- int
- return
- void
- while
- input
- output

### Special symbols
- **+** (arithmetic addition operation)
- **-** (arithmetic subtraction operation)
- __\*__ (arithmetic multiplication operation)
- **/** (arithmetic division operation)
- **<** (logic operator less than)
- **<=** (logic operator less or equal than)
- **\>** (logic operator more than)
- **\>=** (logic operator more or equal than)
- **==** (logic operator equal)
- **!=** (logic operator different)
- **=** (assignation)
- **;** (semicolon)
- **,** (comma)
- **(** (open parenthesis)
- **)** (close parenthesis)
- **\[** (open square brackets)
- **]** (close square brackets)
- **{** (open curly brackets)
- **}** (close curly brackets)
- __/\*__ (open comment)
- __\*/__ (close comment)

### Identifiers and Numbers
Identifiers and numbers for this language are defined by the following regular expressions
> **ID** = _letter+_
> **NUM** = _digit+_

Where _letter_ = \[a-zA-Z], and _digit_ = \[0-9]
