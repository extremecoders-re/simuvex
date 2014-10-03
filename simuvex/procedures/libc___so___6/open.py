import simuvex
from simuvex.s_type import SimTypeString, SimTypeInt, SimTypeFd

######################################
# open
######################################

class open(simuvex.SimProcedure): #pylint:disable=W0622
	def __init__(self): # pylint: disable=W0231
		self.argument_types = {0: self.ty_ptr(SimTypeString()),
						       1: SimTypeInt(32, True)}
		self.return_type = SimTypeFd()

		# TODO: Symbolic fd
		path = self.arg(0)
		flags = self.arg(1)
		# TODO handle mode if flags == O_CREAT

		plugin = self.state['posix']

		# TODO handle errors and symbolic path
		fd = plugin.open(path, flags)
		self.ret(fd)
