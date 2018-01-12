"""
파이썬 3.4 환경
konlpy, pygame 인스톨필요
한글폰트를 \Lib\site-packages\pytagcloud\fonts 에 복사
fonts.json 편집
{
    "name":"korean"
    "ttf":"폰트이름"
    "name":"다른항목것복사"
}
"""
#! /usr/bin/python3.4
# -*- coding: utf-8 -*-
from collections import Counter
from konlpy.tag import Twitter
import pytagcloud
import codecs

# 문재인 대통령 신년인사 전문 (2018.01.10.), utf-8 로 읽음
f = codecs.open( "moon.dat", "r", "utf-8" )
data = f.read()

# 형태소분석
nlp = Twitter()
nouns = nlp.nouns(data)

count = Counter(nouns)

tag = count.most_common(50)
# 나온 태그 중 잘못된 부분을 삭제한 것 
del tag[48], tag[30], tag[19], tag[8], tag[7], tag[2], tag[1]
taglist = pytagcloud.make_tags(tag, maxsize=260)

pytagcloud.create_tag_image(taglist, 'wordcloud.jpg', size=(1024, 768), fontname='Korean', rectangular=False)
f.close()
