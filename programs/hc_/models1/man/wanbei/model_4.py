#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
__author__ = 'top'
date = '16/11/8'
我爱学习,学习使我快乐
'''
'''
长辈辈分	%(bf)s
年龄	%(nl)s
姓名	%(xm)s
举办地址	%(jbdz)s
//家庭住址	%(jtzz)s
晚辈辈分	%(fyrbf)s
//其他祝寿人姓名	%(qtxm)s
长辈名字	%(zbxm)s
季节	%(jj)s
'''

model_4 = [
    {
      "model":"晚辈们拥有的幸福、快乐，儿女们取得的荣誉、骄傲，这一切都来自%(bf)s。正因为有了%(bf)s的无私仁爱,有了%(bf)s的言传身教、身体力行，才能让儿女们的茁壮成长和幸福生活。%(zbxm)s%(bf)s夫妇在这%(nl)s年的风风雨雨中携手走来，他们互敬互爱，相濡以沫，致家有道，教子有方。今天，我们为%(nl)s%(bf)s夫妇这样与众不同的二老而感到自豪。"
    },
    {
      "model":"你把所有的爱，全部奉献给了我们。如今，岁月已悄悄爬上了你的额头，染白了你的双鬓，%(bf)s的苦，%(bf)s的爱；我们、儿孙们将终身难忘和难以报答。我们将永远牢记你的照料之恩。为此我代表后辈%(fyrbf)s，向%(bf)s鞠躬以表达我们儿孙们深深祝福。"
    },
    {
      "model":"首先请允许我代表老寿星及其家属，向在座的各位至以最热烈的欢迎和衷心的感谢！今天我以%(fyrbf)s的身份，做此次寿宴的主持人。说句实在话，我并没有播音员那磁性的嗓音，但为了表达我对老人的一片祝福心情，我满脸微笑地登上这主持的舞台，还希望大家能给我以掌声鼓励。在这里我谨代表所有的嘉宾，祝愿老人家增福增寿增富贵，添光添彩添吉祥。"
    },
    {
      "model":"老年朋友们，现在正是%(jj)s，愿你的心情也和%(jj)s那样清爽、淡雅！生日快乐！ 老不必叹，更不必讳；花有开有谢，树有荣有枯。年轻人有春天的美，而老人则能使人体味到一种秋天的成熟和坦率。人们常说家有一老就是一宝，人们尽可跑得比老年人快，却不能超过他的智力。愿你如春日天空般妩媚，愿你如夏日天空般明丽，愿你如秋日天空般高爽，愿你如冬日天空般朦胧，祝您拥有甜蜜温馨的生活！您生命的秋天，是枫叶一般的色彩，不是春光胜似春光，时值霜天季节，却格外显得神采奕奕。祝您天天快乐，健康长寿。"
    },
    {
      "model":"借此佳节之际我感谢你，你的笑颜似灿烂的阳光照亮了我的世界，你给予我的安慰和鼓励支持我度过一切艰苦。祝你生日快乐！祝你理想幻想梦想心想事成；公事私事心事事事称心；财路运路人生路路路畅通；晴天雪天天天开心，亲情友情爱情情情似海。我轻呵出一团气，将满天飘舞的思绪，凝结成一朵白云，用心把它绘的五彩斑斓，载上沉淀的祝福，带去来自远方的生日的问候——送给永远开心的你！"
    },
    {
      "model":"愿你如春日天空般妩媚，愿你如夏日天空般明丽，愿你如秋日天空般高爽，愿你如冬日天空般朦胧，祝你拥有甜蜜温馨的万年！%(jj)s是一个多思的季节，牵系着想你的心灵。窗前风干的落叶是记忆的书签，是整个%(jj)s的精美收藏，我沉醉在诗的意境里，把对你重阳的祝福埋藏在心灵深处！再美的日子，没人关怀就是遗憾，也许祝福只是一种形式，却能给我们带来温馨——所以我们都不吝啬寄给彼此关心，一样的日子，一样的牵挂，祝生日愉快！"
    },
    {
      "model":"您生命的秋天，是枫叶一般的色彩，不是春光胜似春光，时值霜天季节，却格外显得神采奕奕。祝您老生日节快乐，健康长寿。友谊之花我向一切至诚的人奉献，爱情的甜果我只与你一人分享。无需千言万语，无需海誓山盟；只要记住――两颗心撞击出火花的那一瞬间！空气中弥漫着欢乐，树梢上飘落着祝福，生日的激情在喷薄。我愿化作清风、阳光、白云，给你载来如意、健康、财富。生日快乐！"
    },
    {
      "model":"白云飘荡，重重叠叠的牵挂，在天空中飘远;菊花片片，绽放在清风的旅途，把牵挂定格在你的心田;茱萸插遍，久久远远的思念萦绕身边;浓浓的祝福，追随前行的脚步，快乐无穷倍，幸福N次方。风是我激情的号角，雨是我昂扬的战鼓，月亮代表我真诚的心声，太阳代表我燃烧的热情。无论你身在何时何地，我的祝福如影随行：生日快乐！"
    },
    {
      "model":"您生命的秋天，是枫叶一般的色彩，不是春光胜似春光，时值霜天季节，却格外显得神采奕奕。祝您老生日快乐，健康长寿"
    },
    {
      "model":"但是夕阳无限好，何须惆怅近黄昏! 苍龙日暮还行雨，老树春深更著花! 世上若有诤友，那就是如你对我那样关怀的朋友。愿你拥有无穷无尽的幸福与欢乐，你的生活永远美好,祝生日快乐！"
    },
  ]