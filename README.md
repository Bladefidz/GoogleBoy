GoogleBoy
==================

### Description
Crawl google search result.


feature:
---------
* Read keywords stored in a text file.
* Recursive query to add in keyword.
* Run in background process.
* Ultra ligthweight.
* Using standart python libraries.

usage:
------
```shell
python googleboy.py [-h] -f FILE -R RECURSIVE KEYWORD
```

optional arguments:
-------------------
```shell
  -h, --help            Show this help message and exit
  -f, --file            File contains keywords
  -R, --recursive       Recursive query
```

example usage:
--------------
```shell
python googleboy.py -f "daftar_sekolah.txt" -R "* jl * 0351 *"
```
Or you can view test's folder to read the result.

under developments:
-------------------
* thread: Launch process as thread (default number of thread: 10).
* random user agents: Build massive user agents dictionary to avoid detection as robot and randomize it every run a process.
* logfile: Give user free to create their log file or locate it to any directory or folders (default: keyword+recursive_query.txt).
* loglevel: Create better loglevel {1,2,3,4,5} (default: 3).
