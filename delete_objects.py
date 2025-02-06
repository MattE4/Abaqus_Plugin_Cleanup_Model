from __future__ import print_function
from abaqus import *
from abaqusConstants import *
from caeModules import *

def delOb(kw_box1=None):
	
	vpName = session.currentViewportName
	modelName = session.sessionState[session.currentViewportName]['modelName']
	m = mdb.models[modelName]
	a = m.rootAssembly


	#################################################################################
	# delete suppressed instances
	
	if (kw_box1=='Both') or (kw_box1=='Suppressed Instances'):
		
		suppressed_instances = []
		for name in a.instances.keys():
			if len(a.instances[str(name)].vertices) == 0:
				suppressed_instances.append(name)
		
		if suppressed_instances:
			session.viewports[vpName].disableColorCodeUpdates()

			for i in suppressed_instances:
				del a.features[str(i)]

			a.regenerate()
			session.viewports[vpName].enableColorCodeUpdates()
			session.viewports[vpName].forceRefresh()
			
			print('\nDeleted '+str(len(suppressed_instances))+' instance(s)')
		

	#################################################################################
	# delete unused parts
	
	if (kw_box1=='Both') or (kw_box1=='Unused Parts'):
	
		# get part name for each instance and store in set
		used_part_names = {a.instances[name].partName for name in a.instances.keys()}
		
		# for each existing part, compare with used part set and delete if not in there
		x=0
		for name in m.parts.keys():
			if name not in used_part_names:
				del m.parts[str(name)]
				x+=1

		print('Deleted '+str(x)+' part(s)')
