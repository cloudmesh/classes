from __future__ import print_function, division
import cmd


class mycmd(cmd.Cmd):

	prompt = 'mycmd >> '
	def do_destroy(self, line):
		print('This is destroy')
		
	def do_kill(self, line):
		print('This is kill')
		
	def do_benchmark(self, line):
		print('This is benchmark')
		
	def do_report(self, line):
		print('This is report')
		
	def do_deploy(self, line):
		print('This is deploy')

	def do_EOF(self, line):
		print('bye, bye')
		return True


if __name__ == '__main__':
    mycmd().cmdloop()
