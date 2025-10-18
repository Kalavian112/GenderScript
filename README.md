# GenderScript
GenderScript is a tiny trans esolang :3
It operates on an array of 65,536 bytes as well as a byte register called "main".
All functions are of the form `function: argument`
For arguments, `byte` is an unsigned int8 and `int` is an unsigned int16.

## Functions
- `ggd` - Prints byte in main as ASCII char
- `egg` - Takes one byte of input (ASCII char) into main
- `trans: byte` - Sets main to `byte`
- `girl: int` - Puts byte at main into address `int`
- `boy: int` - Puts byte at address `int` into main
- `enby: int` - Adds byte at address `int` to byte at main, putting the result into main. Due to integer overflow this can also work for subtraction
- `MtF` - If main is equal to zero, skips next line
- `FtM: int` - Jumps to line number `int`
- `agender: comment` - Comment, ignored by interpreter
- `debug` - Prints debug message
