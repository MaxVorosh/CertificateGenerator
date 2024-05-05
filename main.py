from Certificate import Certificate
import os

blank = Certificate('Максим')
blank.set_nomination('За написание этой программы получает')
blank.add_item(os.path.join('data', 'setrecursionlimit.png'), 10, 10, 10, 10, 100, 8)
blank.save('blank.png')
