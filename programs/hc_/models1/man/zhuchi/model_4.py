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
      "model":"我要代表老先生的子女，感谢父亲大人对我们的养育和教诲之恩。古语云：“百善孝为先”，千言万语也代表不了儿女们对父母养育之恩的无限感激之情，是您们带给了我们生命，让我们能感受到清新的空气、温暖的阳光、五彩的世界和人间的温情。心宽能长寿，德美可延年，看着眼前父亲斑斑的白发，我们兄弟姊妹心情十分激动。"
    },
    {
      "model":"在此我想代表老先生的子女对大家说，我父亲长寿的原因在于：从小经历艰苦磨难，非常勤劳，筋骨强壮；心胸开阔，性情豁达，宽厚善良；孝敬老人，友爱弟兄，帮助亲友，一生一世问心无愧；他热爱家庭，儿孙孝顺和睦。这些，都使得他能延年益寿！也感谢朋友们和远道而来的亲戚们对父亲的悉心照顾，使得父亲有了平静安详的晚年生活，也免去了我们这些儿孙的后顾之忧， 再次谢谢你们。我们都要感谢老人积善行德、言传身教留给后人的精神财富！！！"
    },
    {
      "model":"您艰苦朴素的精神教育我们热爱生活，热爱家庭；使您严格的管教让我们读书成人、诚实做人，使您永不气馁的鼓励和高标准的要求激励我们创业发展、勤劳做事，造就了今天的幸福生活。今天看到您已经是白发苍苍，但精神焕发，笑口颜开，心态平和，我们由衷的高兴激动。在此，我代表您的儿女向二老表示：我们要牢记您们的谆谆教导，继承您们的奋斗精神，感恩您们的养育之恩，珍惜这来之不易的幸福生活，珍惜这份难得的天伦之乐，团结和睦，继续拼搏，使生活更为富裕，家庭更加幸福，你二老的日子更为舒心。"
    },
    {
      "model":"作为主持人，我想替晚辈们对您说，您在我们晚辈的心中永远是神圣的、伟大的！我们的幸福来自于%(bf)s的支持和鼓励，我们的快乐来自于%(bf)s的呵护和疼爱，我们的团结和睦来自于%(bf)s的殷殷嘱咐和谆谆教诲！在此，我作为代表向%(bf)s表示：我们一定要牢记你们的教导，承继你们的精神，团结和睦，积极进取，在学业、事业上都取得丰收！同时一定要孝敬你们安度晚年，百年到老。"
    },
    {
      "model":"身为主持人，我代表老先生的子女对父亲送上祝福，祝爸爸幸福安康，福寿无边！ 父爱深似海，父爱重如山。父爱如山，高大而巍峨；父爱如天，粗犷而深远；父爱是深遂的、伟大的、纯洁而不求回报的。父亲像是一棵树，总是不言不语，却让他枝叶繁茂的坚实臂膀为树下的我们遮风挡雨、制造荫凉。不知不觉间我们已长大，而树却渐渐老去，甚至新发的树叶都不再充满生机。让我们由衷地说一声：爸爸，我爱你，生日快乐！"
    },
    {
      "model":"在这里我代表所有的嘉宾，祝愿%(bf)s增福增寿增富贵，添光添彩添吉祥。 诸位亲友、各位来宾，今天真是群贤毕至，鼓舞欢欣。感谢大家在百忙之中抽出时间前来赴宴、祝福。这正是：亲朋共享天伦乐，欢声笑语寿满堂。"
    },
    {
      "model":"我代表%(bf)s的子女，子女们没有忘记父母长辈养育之恩，为需要帮助的亲友慷慨解囊，为家乡建设贡献力量。可以说，他把孝心献给了母亲，把爱心献给了家乡，把关心献给了亲人，把诚心献给了朋友。我想，让我们共同响起热烈的掌声，为%(zbxm)s先生送去无穷无尽的信心！ 嘉宾旨酒，笑指青山来献寿。百岁平安，人共梅花老岁寒。今天，这里高朋满座，让寒冷的冬天有了春天般的温暖。"
    },
    {
      "model":"我代表老先生的子女.在您那博大温暖的胸怀里,真正使我感受到了爱的奉献.在您的生日里,请让我深情的说声谢谢!树木的繁茂归功于土地的养育,儿子的成长归功于父母的辛劳，父亲的爱是含蓄的,每一次严厉的责备,每一回无声的付出,每一道可口的家常小菜,都诠释出一个父亲对儿子的那种特殊的关爱.它是一种崇高的爱,只是给予,不求索取,不讨恩情.对于我来说,最大的幸福莫过于有理解自己的父母.我得到了这种幸福,并从未失去过.所以在您的生日,我想再次向您说一声谢谢!"
    },
    {
      "model":"我代表老先生的子女，首先我要说感谢。第一我要感谢父亲对我们儿女的养育之恩。树木的繁茂归功于土地的养育，儿女的成长归功于父母的辛劳。%(nl)s年的岁月沧桑写在父亲的脸上，写在儿女心灵深处的记忆中。人们常说父爱如山，正是父亲用他那高山一样的臂膀，大海一样的胸怀，支持着、温暖着我们。"
    },
    {
      "model":"我代表老先生的子女想对您说，是您老人家用超过常人的艰辛养育了我们几位儿女，是您老人家用成龙成凤的严爱供养我们读书成人，奠定了我们人生的起点，是您老人家用永不气馁的鼓励和高标准的要求激励我们开拓事业，造就了我们的今天。看着眼前我的父母斑斑的白发，虽然他们不曾是高官显贵、名流宿儒，但他们的一生却是创业的一生，刚强的一生，他们是普通的，但在我们子女的心中二老永远是神圣的、伟大的！"
    },
  ]