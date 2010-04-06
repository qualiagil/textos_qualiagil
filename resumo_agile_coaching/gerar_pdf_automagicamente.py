import os
import time

ctime_inicial = os.stat('agile_coaching_resumo.tex').st_ctime

while True:
    ctime_atual = os.stat('agile_coaching_resumo.tex').st_ctime
    if ctime_atual != ctime_inicial:
        ctime_inicial = ctime_atual
        os.system('latexmk -pdf *.tex')
    time.sleep(1)
