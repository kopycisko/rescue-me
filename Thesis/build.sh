#!/bin/bash
texliveonfly -c lualatex main.tex | grep Warning
bibtex main.aux
texliveonfly -c lualatex main.tex | grep Warning
texliveonfly -c lualatex main.tex | grep Warning
