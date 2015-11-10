enscript -r -1 --file-align=1 --highlight --line-numbers -o - `find . -name '*.py'` | ps2pdf - files.python.pdf
