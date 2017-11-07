import os
import sys
import maya.standalone

os.environ['PROD_SERVER'] = 'p:/badgers_and_foxes'

# maya.standalone.initialize(name='python')
maya.standalone.initialize()

import pymel.core as pm
import importExportEdits
reload(importExportEdits)


class BatchMaya(object):
    PROD_SERVER = 'p:/badgers_and_foxes'

    def __init__(self, episode, shot, task, refList=None):
        self.episode = episode
        self.shot = shot
        self.task = task
        self.refList = refList
        shotPath = os.path.join(self.PROD_SERVER, r'01_SAISON_1/13_PRODUCTION/04_EPISODES/02_Fabrication_3D',
                                self.episode, self.shot, self.task[:3].lower())
        workPath = shotPath + r'/maya/work'
        resFiles = os.listdir(workPath)
        resFiles = [x for x in resFiles if x.startswith(self.episode)]
        resFiles.sort(reverse=True)
        workScene = os.path.join(workPath, resFiles[0])
        self.shotPath = shotPath
        self.workPath = workPath
        self.workScene = workScene

    def doIt(self):
        print self.workScene
        pm.openFile(self.workScene)
        importExportEdits.exportEdits(refPassed=self.refList)


if __name__ == '__main__':
    print sys.argv, '<--------------------------------------'
    if len(sys.argv)== 5 :
        bat = BatchMaya(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        bat = BatchMaya(sys.argv[1], sys.argv[2], sys.argv[3])
    bat.doIt()
