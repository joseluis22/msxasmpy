# msxasmpy

MSX Assembler in Python

I never wrote an assembler in any language,
used Python beyond basic scripting,
understood how lex/yacc work
or wrote any Z80 assembly code.

So naturally I want to write an assembler from scratch,
in Python, using lex/yacc
and learn Z80 assembly coding while at it.

Hopefully every little bit of code will be isolated
and covered by test unit and support fuzzing.

If things go swell, I may try to reduce Python use to
a manageable subset that could be automatically translated to C.
This would allow for maximum performance and support on any platform with working ANSI C 89 compiler,
while hopefully avoiding typical C coding errors
like off by one, pointer use after free(), assign instead of compare etc.

If Z80 assembler for MSX is a success,
next platform/CPU would be Neo Geo Pocket with Toshiba TLCS900H CPU.

Download and unpack http://www.dabeaz.com/ply/ply-3.9.tar.gz or later in src before use.

Nothing is working right now.

I'm watching this video tutorial for simple flex tokenizer: https://www.youtube.com/watch?v=54bo1qaHAfk
