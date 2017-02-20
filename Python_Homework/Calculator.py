from __future__ import print_function, division
import cmd


class Calculator(cmd.Cmd):
     prompt = 'calc >>> '
     intro = 'Simple calculator that can do addition, subtraction, multiplication and division.'

     def do_add(self, line):
             args = line.split()
             total = 0
             for arg in args:
                     total += float(arg.strip())
             print(total)



     def do_subtract(self, line):
             args = line.split()
             total = 0
             if len(args) > 0:
                     total = float(args[0])
             for arg in args[1:]:
                     total -= float(arg.strip())
             print(total)

     def do_multiply(self, line):
             args = line.split()
             total = 0
             if len(args) > 0:
                     total = float(args[0])
             for arg in args[1:]:
                     total *= float(arg.strip())
             print(total)

     def do_divide(self, line):
             args = line.split()
             total = 0
             if len(args) > 0:
                     total = float(args[0])
             for arg in args[1:]:
                     total /= float(arg.strip())
             print(total)



     def do_EOF(self, line):
             print('bye, bye')
             return True


if __name__ == '__main__':
     Calculator().cmdloop()
