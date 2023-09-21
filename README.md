# termdebug
termdebug with local variables window

This repo contains modified termdebug plugin exptacted from Vim, plus modified
pretty-printers extracted from GCC, tailored together to show local variables in a handy (for the author) way
while debugging in Vim.

## Installation
- Clone this repo somewhere
- Add path to pretty printers to your ~/.gdbinit
```
python
import sys
sys.path.insert(0, '<path to repo>/stl_pretty_printers/python')
```
- Replace termdebug from vim distro by link to the repo, usually this would look like
```
/usr/share/vim/vim90/pack/dist/opt/termdebug -> <path to repo>
```
