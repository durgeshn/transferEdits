import os
from PySide import QtGui
import tempfile
import pymel.core as pm

from transferEdits.core import importExportEdits

reload(importExportEdits)

from transferEdits.ui import EditsIEWin

reload(EditsIEWin)

from shiboken import wrapInstance
import maya.OpenMayaUI as omui


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)


projectPath = 'P:/badgers_and_foxes/01_SAISON_1/13_PRODUCTION/04_EPISODES/02_Fabrication_3D'


class EditsIE(QtGui.QMainWindow, EditsIEWin.Ui_MainWindow):
    editDir = os.path.join(tempfile.gettempdir(), 'editExportMa').replace('\\', '/')

    def __init__(self, prnt=maya_main_window(), dept='lay'):
        super(EditsIE, self).__init__(prnt)
        self.setupUi(self)
        self.proj_cb.addItems(['BDG'])
        self.dept = dept
        self.editDir = None
        self.makeConnections()
        self.setWindowTitle('TestEditWin')

    def makeConnections(self):
        self.fillEpisodes()
        self.fillListWidget()
        self.ep_cb.currentIndexChanged.connect(self.fillShots)
        self.importEdits_pb.clicked.connect(self.importEdits)
        self.finaliz_pb.clicked.connect(self.finalizing)
        self.close_pb.clicked.connect(self.closeWin)

    def fillEpisodes(self):
        self.ep_cb.clear()
        self.ep_cb.addItem('SELECT')
        allEpi = os.listdir(projectPath)
        allEpi.sort()
        for each in allEpi:
            if not each.startswith('BDG'):
                continue
            self.ep_cb.addItem(each)

    def fillListWidget(self):

        self.assetRefTree_wt.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)

        self.assetRefTree_wt.clear()
        assetItem = QtGui.QTreeWidgetItem(self.assetRefTree_wt)
        assetItem.setText(0, 'Assets')
        camItem = QtGui.QTreeWidgetItem(self.assetRefTree_wt)
        camItem.setText(0, 'CAMERA')

        for each in pm.listReferences():
            refNode = str(each.refNode)
            if refNode.startswith('st_') or refNode.startswith('edit_'):
                continue
            if 'CAM' in refNode:
                item = QtGui.QTreeWidgetItem(camItem)
                item.setText(0, refNode)
            else:
                item = QtGui.QTreeWidgetItem(assetItem)
                item.setText(0, refNode)

    @property
    def winEvent(self):
        return True

    def fillShots(self):
        episode = self.ep_cb.currentText()
        shotPath = os.path.join(projectPath, episode)
        self.sh_cb.clear()
        self.sh_cb.addItem('SELECT')
        allShots = os.listdir(shotPath)
        allShots.sort()
        for each in allShots:
            if not each.startswith('sh'):
                continue
            self.sh_cb.addItem(each)

    def importEdits(self):
        episode = self.ep_cb.currentText()
        shot = self.sh_cb.currentText()

        if not episode.startswith('BDG'):
            raise RuntimeError('Please select a proper EPISODE.')
        if not shot.startswith('sh'):
            raise RuntimeError('Please select a proper SHOT.')

        self.cleanUpEdits()
        shotFile = None
        shotDir = os.path.join(projectPath, episode, shot, self.dept, 'maya/work').replace('\\', '/')
        print shotDir, '<----------------------------------'

        allFiles = [x for x in os.listdir(shotDir) if
                    x.endswith('.ma') and not x.endswith('tmp.ma') and not x.endswith('PORJ.ma')]
        allFiles.sort()
        latestVersion = allFiles[-1]
        # sourceFilePath = os.path.join(shotDir, latestVersion)
        temp = latestVersion.split('_')
        print temp, '================================================'
        ep = temp[0]
        sh = 'sh{:03}'.format(int(temp[1]))
        batPath = r'D:\user\durgesh.n\workspace\transferEdits\transferEdits\core\exportEdits.bat'
        # print [batPath, str(ep), sh, self.dept], '<----------------------------------------------'
        refList = []
        for each in self.assetRefTree_wt.selectedItems():
            refList.append(each.text(0))
        if not refList:
            refList = [str(x.refNode) for x in pm.listReferences() if
                       not str(x.refNode).startswith('edits_') and not str(x.refNode).startswith('st_')]
        print refList, '<<<<<<<<<<<<<<<<<<<<<<<<<< REF LIST'

        batchRefList = ','.join(refList)

        print 'batchRefList : ', batchRefList, '------------------------------'
        runCmd = ' '.join([batPath, str(ep), sh, self.dept])
        runCmd += ' "%s"' % batchRefList
        print '---------------------------------------------------'
        print runCmd
        print '---------------------------------------------------'
        os.system(runCmd)

        self.cleanUp(refList=','.join(refList))

        importExportEdits.importEdits(refList=batchRefList)

    def cleanUpEdits(self):
        for each in pm.listReferences():
            if str(each.refNode).startswith('edit_'):
                each.remove()

    def cleanUp(self, refList=''):
        if not refList:
            refList = ','.join([str(x.refNode) for x in pm.listReferences() if
                                not str(x.refNode).startswith('edits_') and not str(x.refNode).startswith('st_')])
        for ref in refList.split(','):
            print ref, '<--------------------------Ref Clean Up...................'
            if ref.startswith('st_'):
                continue
            refNode = pm.FileReference(ref)
            refNode.unload()
            refNode.clean()
            refNode.load()

    def finalizing(self):
        print 'finalizing...................'
        for eachRef in pm.listReferences():
            if str(eachRef.refNode).startswith('edit_'):
                eachRef.importContents()

    def closeWin(self):
        editsPresent = False
        for e in pm.listReferences():
            if str(e.refNode).startswith('edit_'):
                editsPresent = True
                break

        if editsPresent:
            ass = pm.confirmDialog(title='Confirm',
                                   message='Some edits are still in the scene.Please use finalize first.',
                                   button=['OK'], defaultButton='OK')
            return
        self.close()


if __name__ == '__main__':
    pass
