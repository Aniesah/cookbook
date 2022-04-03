# kitchen
A place where to maintain the cookbook


## remove submodules -- 03-apr-2022
0. View [current history](https://github.com/dudung/cookbook/tree/363be85db210254373ae784589f701166cae66e5).
1. Check submodules.

```batch
$ cat .gitmodules
[submodule "python"]
        path = python
        url = https://github.com/dudung/python.git
[submodule "basic"]
        path = basic
        url = https://github.com/dudung/basic.git
[submodule "cpp"]
        path = cpp
        url = https://github.com/dudung/cpp.git
[submodule "go"]
        path = go
        url = https://github.com/dudung/go.git
[submodule "fortran"]
        path = fortran
        url = https://github.com/dudung/fortran.git
[submodule "java"]
        path = java
        url = https://github.com/dudung/java.git
[submodule "js"]
        path = js
        url = https://github.com/dudung/js.git
[submodule "json"]
        path = json
        url = https://github.com/dudung/json.git
[submodule "node.js"]
        path = node.js
        url = https://github.com/dudung/node.js.git
[submodule "lisp"]
        path = lisp
        url = https://github.com/dudung/lisp.git
[submodule "php"]
        path = php
        url = https://github.com/dudung/php.git
[submodule "bash"]
        path = bash
        url = https://github.com/dudung/bash.git
[submodule "css"]
        path = css
        url = https://github.com/dudung/css.git
[submodule "pascal"]
        path = pascal
        url = https://github.com/dudung/pascal.git
[submodule "perl"]
        path = perl
        url = https://github.com/dudung/perl.git
[submodule "r"]
        path = r
        url = https://github.com/dudung/r.git
[submodule "svg"]
        path = svg
        url = https://github.com/dudung/svg.git
[submodule "tex"]
        path = tex
        url = https://github.com/dudung/tex.git
[submodule "gnuplot"]
        path = gnuplot
        url = https://github.com/dudung/gnuplot
        
$ 
```

2. Remove all submodules.

```batch
$ git rm bash
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'bash'

$ git rm python
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'python'

$ git rm basic
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'basic'

$ git rm cpp
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'cpp'

$ git rm css
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'css'

$ git rm fortran
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'fortran'

$ git rm gnuplot
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'gnuplot'

$ git rm go
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'go'

$ git rm java
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'java'

$ git rm js
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'js'

$ git rm json
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'json'

$ git rm lisp
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'lisp'

$ git rm node.js
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'node.js'

$ git rm pascal
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'pascal'

$ git rm perl
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'perl'

$ git rm php
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'php'

$ git rm r
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'r'

$ git rm svg
warning: LF will be replaced by CRLF in .gitmodules.
The file will have its original line endings in your working directory
rm 'svg'

$ git rm tex
rm 'tex'

$ 
```

3. Check again available submodules.

```batch
$ cat .gitmodules

$ 
```

4. View the [commits](https://github.com/dudung/cookbook/commit/dbc3df772acba062457145a1e413d8260bccb7f5).
5. View [new current history](https://github.com/dudung/cookbook/tree/dbc3df772acba062457145a1e413d8260bccb7f5).