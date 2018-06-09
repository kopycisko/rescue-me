#!/bin/bash
texliveonfly -c xelatex main.tex | grep Warning
bibtex main.aux
texliveonfly -c xelatex main.tex | grep Warning
texliveonfly -c xelatex main.tex | grep Warning
