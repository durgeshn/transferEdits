import tempfile
import maya.mel as mel
import pymel.core as pm
import os


def camExport():
    for each in pm.listReferences():
        if 'CAM' in str(each.refNode):
            cam = str(each.refNode)
            return cam


def exportEdits(refPassed=''):
    if not refPassed:
        refPassed = ','.join([str(x.refNode) for x in pm.listReferences()])
    expFolder = os.path.join(tempfile.gettempdir(), 'editExportMa').replace('\\', '/')
    if not os.path.isdir(expFolder):
        os.makedirs(expFolder)
    for each in refPassed.split(','):
        if str(each).startswith('st_'):
            continue
        if 'CAM' in each:
            each = camExport()
        editFilePath = os.path.join(expFolder, each).replace('\\', '/')
        cmd = 'exportEdits -f -type "editMA" -orn {} -includeNetwork -includeAnimation -includeShaders -includeSetAttrs 1 "{}";'.format(
            each, editFilePath)
        mel.eval(cmd)
    return expFolder, refPassed


def importEdits(refList=None):
    if not refList:
        refList = ','.join([str(x.refNode) for x in pm.listReferences()])

    expFolder = os.path.join(tempfile.gettempdir(), 'editExportMa').replace('\\', '/')
    if not os.path.isdir(expFolder):
        os.makedirs(expFolder)

    for each in refList.split(','):
        if each.startswith('st_'):
            print 'SETs found skipping...'
            continue
        if '_CAMRN' in each:
            editFile = [x for x in os.listdir(expFolder) if '_CAMRN.editMA' in x][0]
            replaceName = editFile.replace('.editMA', '')
            editFileNew = os.path.join(expFolder, editFile).replace('\\', '/')
            print editFileNew
            cmdCam = 'file -r -type "editMA"  -namespace "edit_{}" -applyTo "{}" -replaceName "{}" "{}" "{}";'.format(
                each, each, replaceName, each, editFileNew)
            mel.eval(cmdCam)
            continue
        editFile = os.path.join(expFolder, '{}.editMA'.format(each)).replace('\\', '/')
        if not os.path.isfile(editFile):
            continue
        cmd = 'file -r -type "editMA"  -namespace "edit_{}" -applyTo "{}" "{}";'.format(each, each,
                                                                                        editFile)
        mel.eval(cmd)
