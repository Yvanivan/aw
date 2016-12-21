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

model_6 = [
    {
      "model":"%(nl)s年华，人生的一个转折，也是人生的里程碑。今天，我们相聚在一起，就是要向%(zbxm)s先生表示一个热烈的祝贺，也同时表达一个美好的祝愿。俗话说得好，家宽出少年，人逢喜事精神爽，正值太平盛世、国家经济繁荣、社会进步发展、民族和谐和睦、人民生活安定，人们的精神面貌发生可喜的变化，你们看，我们的%(zbxm)s先生风光满面、还是一个勃勃英姿的青春年少啊。"
    },
    {
      "model":"各位朋友、各位来宾，%(bf)s的儿女们没有忘记%(bf)s的养育之恩，没有忘记同事朋友相助之意，特邀大家在这里为%(bf)s举行寿宴。可以说，%(fyrbf)s把孝心献给了%(bf)s，把爱心献给了%(bf)s，把关心献给了亲人，把诚心献给了大家。请所有的来宾和朋友把祝福的美酒举起来，敬献给寿星，祝愿寿星生日快乐！也祝大家长命百岁，幸福安康！干杯！谢谢！刚才这杯香醇的美酒是喝在嘴里，甜在心里！让我们用最热烈的掌声，同大家共进寿宴。"
    },
    {
      "model":"下面，让我们共同唱响《生日快乐歌》，祝福老寿星生日快乐。由我来领唱。我们唱两遍，第一遍由我领唱，第二遍请大家全体合唱。现在请老寿在心里默默的许下一个美好的心愿，同时也请我们全场所有的来宾共同为他许下一个美好的心愿，祝愿老寿星今后的生活像这灯光的颜色一样五彩缤纷，象这美食的味道一样甜甜蜜蜜，团团圆圆！愿美好的心愿伴随着青烟的升起开始实现！"
    },
    {
      "model":"让我们一起恭祝老寿星，福如东海，日月昌明。松鹤长春，春秋不老，古稀重新，欢乐远长。同时也祝愿在场嘉宾的每一位来宾都幸福安康！最后祝各位来宾万是如意，心想事成，让我们共同度过这美好的时光。"
    },
    {
      "model":"让我们一起恭祝老寿星，福如东海，日月昌明。松鹤长春，春秋不老，古稀重新，欢乐远长。同时也祝愿在场的每一位来宾都幸福安康，万事如意，心想事成！让我们共同度过这美好的时光。兄弟同心，其利断金！我们有理由相信，在全家人的共同努力下，家业一定会蒸蒸日上，兴盛繁荣！%(bf)s一定会健康长寿，老有所乐！"
    },
    {
      "model":"现在，让我们一起祝福：家永和，事永昌，福永生，子孙万代兴；人长久，春常在，月长圆，基业旺千年！祝福%(bf)s生命之树常青、生命之花常艳，生命之水常流，全体亲属都增福增寿增富贵，添光添彩添吉祥！"
    },
    {
      "model":"让我们共同举杯,祝福伟大的%(bf)s:福如东海长流水,寿比南山不老松!"
    },
    {
      "model":"让我们一起恭祝老寿星，福如东海，日月昌明。松鹤长春，春秋不老，古稀重新，欢乐远长。同时也祝愿在场嘉宾的每一位来宾都幸福安康！最后祝各位来宾万是如意，心想事成，让我们共同度过这美好的时光。"
    },
    {
      "model":"让我们共同举杯，再次祝愿%(zbxm)s先生%(nl)s大寿健康长寿，福如东海，寿比南山。美好的时光，很好的心情，伴随着悦耳动听的音乐和欢声笑语，同时，送各位可爱的来宾一件外套，前面是平安，后面是幸福，吉祥是领子，如意是袖子，快乐是扣子，口袋里满是温暖。愿好运像地雷一样，时常给你踩到；厄运像流星雨一样，永远淋你不到；财富像垃圾一样，随处可以捡到。"
    },
    {
      "model":"最后还是让我们献上最衷心的祝愿，祝福老人家生活之树常绿，生命之水长流，寿诞快乐，春辉永绽！祝福在座的所有来宾身体健康、工作顺利、合家欢乐、万事如意！谢谢大家！"
    },
  ]