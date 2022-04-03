# kitchen
A place where to maintain the cookbook


## add folders -- 03-apr-2022
1. Check status of git

```batch
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        basic/
        cpp/
        css/
        fortran/
        gnuplot/
        go/
        java/
        js/
        json/
        lisp/
        node.js/
        pascal/
        perl/
        php/
        python/
        r/
        svg/
        tex/

nothing added to commit but untracked files present (use "git add" to track)

$ 
```

2. Add one by one.

```batch
$ git add basic

$ git commit -a -m "new basic folder"
[main cfb4fc4] new basic folder
 3 files changed, 24 insertions(+)
 create mode 100644 basic/.gitignore
 create mode 100644 basic/LICENSE
 create mode 100644 basic/README.md

$ git add cpp

$ git commit -a -m "new cpp folder"
[main dc1df3e] new cpp folder
 3 files changed, 55 insertions(+)
 create mode 100644 cpp/.gitignore
 create mode 100644 cpp/LICENSE
 create mode 100644 cpp/README.md

$ git add css

$ git commit -a -m "new css folder"
[main 77d24d3] new css folder
 3 files changed, 24 insertions(+)
 create mode 100644 css/.gitignore
 create mode 100644 css/LICENSE
 create mode 100644 css/README.md

$ git add fortran

$ git commit -a -m "new fortran folder"
[main 9cacedd] new fortran folder
 3 files changed, 55 insertions(+)
 create mode 100644 fortran/.gitignore
 create mode 100644 fortran/LICENSE
 create mode 100644 fortran/README.md

$ git add gnuplot

$ git commit -a -m "new gnuplot folder"
[main 7936983] new gnuplot folder
 3 files changed, 25 insertions(+)
 create mode 100644 gnuplot/.gitignore
 create mode 100644 gnuplot/LICENSE
 create mode 100644 gnuplot/README.md

$ git add go

$ git commit -a -m "new go folder"
[main 67fcde4] new go folder
 3 files changed, 38 insertions(+)
 create mode 100644 go/.gitignore
 create mode 100644 go/LICENSE
 create mode 100644 go/README.md

$ git add java

$ git commit -a -m "new java folder"
[main 96d1ecc] new java folder
 3 files changed, 46 insertions(+)
 create mode 100644 java/.gitignore
 create mode 100644 java/LICENSE
 create mode 100644 java/README.md

$ git add js

$ git commit -a -m "new js folder"
[main 71e7da7] new js folder
 4 files changed, 25 insertions(+)
 create mode 100644 js/.gitignore
 create mode 100644 js/LICENSE
 create mode 100644 js/README.md
 create mode 100644 js/hello/hello_world.js

$ git add json

$ git commit -a -m "new json folder"
[main 13ecd1f] new json folder
 3 files changed, 24 insertions(+)
 create mode 100644 json/.gitignore
 create mode 100644 json/LICENSE
 create mode 100644 json/README.md

$ git add lisp

$ git commit -a -m "new lisp folder"
[main 707cbfa] new lisp folder
 3 files changed, 24 insertions(+)
 create mode 100644 lisp/.gitignore
 create mode 100644 lisp/LICENSE
 create mode 100644 lisp/README.md

$ git add node.js

$ git commit -a -m "new node.js folder"
[main 65b118b] new node.js folder
 3 files changed, 127 insertions(+)
 create mode 100644 node.js/.gitignore
 create mode 100644 node.js/LICENSE
 create mode 100644 node.js/README.md

$ git add pascal

$ git commit -a -m "new pascal folder"
[main 37fb06d] new pascal folder
 3 files changed, 24 insertions(+)
 create mode 100644 pascal/.gitignore
 create mode 100644 pascal/LICENSE
 create mode 100644 pascal/README.md

$ git add perl

$ git commit -a -m "new perl folder"
[main 9f046da] new perl folder
 3 files changed, 58 insertions(+)
 create mode 100644 perl/.gitignore
 create mode 100644 perl/LICENSE
 create mode 100644 perl/README.md

$ git add php

$ git commit -a -m "new php folder"
[main bccf36c] new php folder
 3 files changed, 24 insertions(+)
 create mode 100644 php/.gitignore
 create mode 100644 php/LICENSE
 create mode 100644 php/README.md

$ git add python
warning: LF will be replaced by CRLF in python/animation/basic_animation.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in python/animation/simple_anim.py.
The file will have its original line endings in your working directory

$ git commit -a -m "new python folder"
[main 5654c33] new python folder
 7 files changed, 254 insertions(+)
 create mode 100644 python/.gitignore
 create mode 100644 python/LICENSE
 create mode 100644 python/README.md
 create mode 100644 python/animation/basic_animation.gif
 create mode 100644 python/animation/basic_animation.py
 create mode 100644 python/animation/simple_anim.py
 create mode 100644 python/hello/hello_world.py

$ git add r

$ git commit -a -m "new r folder"
[main d1b60dd] new r folder
 3 files changed, 62 insertions(+)
 create mode 100644 r/.gitignore
 create mode 100644 r/LICENSE
 create mode 100644 r/README.md

$ git add svg

$ git commit -a -m "new svg folder"
[main 1e74cce] new svg folder
 3 files changed, 24 insertions(+)
 create mode 100644 svg/.gitignore
 create mode 100644 svg/LICENSE
 create mode 100644 svg/README.md

$ git add tex

$ git commit -a -m "new tex folder"
[main 324097d] new tex folder
 3 files changed, 299 insertions(+)
 create mode 100644 tex/.gitignore
 create mode 100644 tex/LICENSE
 create mode 100644 tex/README.md

```

3. Check git status.

```batch
$ git status
On branch main
Your branch is ahead of 'origin/main' by 18 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

4. Lakukan push.

```batch
$ git push
Enumerating objects: 91, done.
Counting objects: 100% (91/91), done.
Delta compression using up to 4 threads
Compressing objects: 100% (66/66), done.
Writing objects: 100% (90/90), 716.09 KiB | 6.69 MiB/s, done.
Total 90 (delta 22), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (22/22), done.
To https://github.com/dudung/cookbook.git
   d258adf..324097d  main -> main

```

4. View [current history](https://github.com/dudung/cookbook/tree/324097df8fc2ab1e752e6c8e760b23344bf05086).


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
