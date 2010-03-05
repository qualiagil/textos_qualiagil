Textos do Quali-Ágil
====================

Todos os textos gerados pelo Quali-Ágil [NSI] serão guardados e compartilhados através deste repositório.

Integrantes (com respectivos usuários do GitHub):

* Gustavo Rezende (nsigustavo)
* Hugo Lopes (hugobr)
* Rodrigo Manhães (rodrigomanhaes)
* Marianna Siqueira (mariannareis)


Gerando arquivos PDF a partir dos arquivos TeX
----------------------------------------------

O script ``latexmk.pl`` foi obtido a partir do site <http://www.phys.psu.edu/~collins/software/latexmk-jcc/>, como dica do Diego Manhães Pinheiro. O motivo de usar o ``latexmk`` é que não é necessário rodar o ``latex`` e o ``bibtex`` diversas vezes mais - o script cuida disso.


Instalação do ``latexmk.pl``
-------------------------

As únicas dependências do ``latexmk.pl`` são o ``TeX``, ``LaTeX`` e ``Perl``.

    $ sudo cp latexmk.pl /usr/bin/latexmk
    $ sudo chmod a+rx /usr/bin/latexmk


Usando o ``latexmk.pl``
-----------------------

Após feito a instalação do script basta chama-lo na linha de comando da seguinte maneira (pra gerar um pdf):

    $ latexmk -pdf nome_do_texto.tex

Quando não é especificada nenhuma opção, como no caso foi especificado o -pdf, o ``latexmk`` gera arquivos PDF e DVI.
