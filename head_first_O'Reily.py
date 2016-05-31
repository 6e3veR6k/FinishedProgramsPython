def sanitize(time):
	splitter_list = [':', '.', '-']
	for el in splitter_list:
		if el in time:
			return ".".join(time.split(el))


def get_coach_data(filename):
	try:
		with open(filename) as file:
			data = file.readline()
			data_lst = data.strip().split(',')
			return AthleteList(data_lst.pop(0), data_lst.pop(0), data_lst)
	except IOError as ioerror:
		print "File error: " + str(ioerror)
		return None


class AthleteList(list):
	def __init__(self, a_name, a_dob=None, a_time=[]):
		list.__init__([])
		self.name = a_name
		self.dob = a_dob
		self.extend(a_time)
	
	def top3(self):
		return sorted(set([sanitize(t) for t in self]), reverse=True)[:3]

mikey = get_coach_data("mikey2.txt")	
mikey.append('2-55')
mikey.extend(['3.01', '3-03', '3:04'])
print mikey.top3()