import sublime, sublime_plugin, os

def initConstant():
	global Setttings
	global Options
	Setttings = sublime.load_settings('SearchFile.sublime-settings')
	Options = { 'ROOT': Setttings.get('root'), 'ENHANCE': Setttings.get('enhance') }

initConstant()

def findFile(findpath, filename, tmplist):
	if findpath == '':
		print 'empty file find '
		return True

	if findpath[0] == '/':
		tmplist = Options['ROOT']


	findpath = tmplist + '\\'.join(findpath.split('/'))

	if os.path.exists(findpath):
		try:
			sublime.active_window().open_file(findpath)
		except BaseException:
			print "Error on except"
			return False
	else:
		message = "Sorry, I cannot find the %s file."
		print message % findpath 
		return False

	return True

def parseSel(self, findpath):
	srcpath = self.view.file_name()
	tmplist = srcpath.split('\\')			
	tmplist.pop()
	tmplist = '\\'.join(tmplist) + '\\'
	sels = []

	FindResult = []
	

	if findpath.find('\n') != -1:
		allpath = findpath.split('\n')
		for index in range(len(allpath)):
			allpath[index] = allpath[index].replace('\t','').replace(' ','')

		FindResult = []
		for path in allpath:
			filename = path.split('/').pop()
			if findFile(path, filename, tmplist) == False:
				FindResult.append(filename)
	else:
		filename = findpath.split('/').pop()
		if findFile(findpath, filename, tmplist) == False:
			FindResult.append(filename)


	return FindResult
	


class SearchfileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print "\n\n\n"
		print "SeachFile Start"
		print "==============================================="	

		
		sels = self.view.sel()		

		
		notFindSel = []
		FindResult = []

		for index in range(len(sels)):
			findpath = self.view.substr(sels[index]).lstrip().rstrip()
			if findpath == '':
				notFindSel.append(index)
			else:				
				selresult = parseSel(self, findpath)
				if len(selresult) > 0:
					FindResult.append(','.join(selresult))


		if len(notFindSel) > 0 and Options['ENHANCE']:
			#self.view.run_command("expand_selection", {"to": "scope"})
			self.view.run_command("expand_selection", {"to": "brackets"})
			#print Options['ENHANCE']
			sels = self.view.sel()
			for i in notFindSel:
				findpath = self.view.substr(sels[i]).replace("'","").replace('"','').lstrip().rstrip()
				if findpath != '':
					selresult = parseSel(self, findpath)
					if len(selresult) > 0:
						FindResult.append(','.join(selresult))


		if len(FindResult) > 0:
			message = "Sorry, I cannot find the %s file."
			sublime.message_dialog(message % ','.join(FindResult))
		
		print "==============================================="
		print "SeachFile End"
		print "\n\n\n"

