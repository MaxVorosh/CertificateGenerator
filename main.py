from Certificate import Certificate
import os

blank = Certificate('Максим')
blank.set_nomination('За написание этой программы получает')
blank.add_item(os.path.join('data', 'setrecursionlimit.png'), 10, 10, scale_x=10, scale_y=10, alpha=100, angle=8)
blank.add_item(os.path.join('data', 'cpplogo.png'), 1000, 800, alpha=100)
blank.save('blank.jpeg')
