from . import font_ru_lc
from . import font_ru_uc
ru_chars=[]
for s in font_ru_uc.f_ru_uc:
    ru_chars.append(s)
for s in font_ru_lc.f_ru_lc:
    ru_chars.append(s)
#for s in b:
#    ru_chars.append(s)
f_ru={'min':1040, 'max':1103, 'chars':ru_chars}