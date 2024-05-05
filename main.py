from Certificate import Certificate
import os

blank = Certificate('Максим')
blank.set_nomination('За написание этой программы получает')
blank.add_item(os.path.join('data', 'setrecursionlimit.png'), 10, 10, scale_x=9, scale_y=9, alpha=100, angle=8)
blank.add_item(os.path.join('data', 'cpplogo.png'), 50, 1400, scale_x=0.5, scale_y=0.5, alpha=100)
blank.add_item(os.path.join('data', 'erat.png'), 100, 700, alpha=100, angle=-30, scale_x=1.25, scale_y=1.25)
blank.add_item(os.path.join('data', 'Hanoi.png'), 1500, 700, alpha=100, angle=10, scale_x=2, scale_y=2)
blank.set_bg(os.path.join('data', 'bg.png'))
blank.save('blank.jpeg')
