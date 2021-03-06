from modules.output._OutputModule import _OutputModule
import logging

class log(_OutputModule):
  def __init__(self, parent, name):
    _OutputModule.__init__(self, parent, name)
    self.logger = logging.getLogger()

  def performAction(self, args = {}):
    try:
      if "thump" in args["OSC"]["JSON"]["data"]:
        return
    except KeyError:
      pass
    self.logger.info("Log: called with {}".format(args))
