# rescue-me
Project and master thesis on rescuing miners basing on MineTronics underground localisation system.

In order to compile latex soruce, there is need to:
* go to the Thesis directory
* issue command 'texliveonfly -c lualatex main.tex'
* if everything goes ok, issue command 'bibtex main.aux'
* then issue twice 'texliveonfly -c lualatex main.tex'
* the output, pdf file will be named main.pdf

It can be that you will get Fatal errors. There can be a few problems causing that errors.

Case 1 - old tlmgr
tlmgr got changed its repository when texlive 2016 got introduced. If you have texlive 2015 you will need to change tlmgr repository setting to be able to use it with your version of texlive.

There is need to:
* issue command 'tlmgr option repository ftp://tug.org/historic/systems/texlive/2015/tlnet-final'
* issue command 'tlmgr update --self --all'

Case 2 - File `luaotfload.sty' not found

There is need to:
* issue command 'sudo apt-get install texlive-luatex'
* issue command 'luaotfload-tool --update'

Case 3 - No polish babel

There is need to:
* issue command 'tlmgr install babel-polish'
