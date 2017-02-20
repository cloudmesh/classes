from __future__ import print_function, division
import cmd


class HelloWorld(cmd.Cmd):
    '''Simple command processor example.'''

    def do_greet(self, line):
        if line is not None and len(line.strip()) > 0:
            print('Hello, %s!' % line.strip().title())
        else:
            print('Hello!')

    def do_deploy(self, line):
    	print('deploy')
    def do_kill(self, line):
	print('kill')
    def do_benchmark(self, line):
	print('benchmark')
    def do_report(self, line):
	print('report')


    def do_EOF(self, line):
        print('bye, bye')
        return True


if __name__ == '__main__':
    HelloWorld().cmdloop()
