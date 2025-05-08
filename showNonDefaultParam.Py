import hou

for pane in hou.ui.curDesktop().panes():
  for tab in pane.tabs():
    if tab.type() == hou.paneTabType.Parm:
      if tab.filterEnabled():
        tab.setFilterEnabled(False)
      else:
        tab.setFilterEnabled(True)
        # set filter Non-Default
        tab.setFilterMode(hou.parmFilterMode.NonDefaultParms)