# -*- coding: utf-8 -*-

from module.plugins.internal.MultiHook import MultiHook
import json


class RealdebridComHook(MultiHook):
    __name__    = "RealdebridComHook"
    __type__    = "hook"
    __version__ = "0.46"

    __config__ = [("pluginmode"    , "all;listed;unlisted", "Use for plugins"                     , "all"),
                  ("pluginlist"    , "str"                , "Plugin list (comma separated)"       , ""   ),
                  ("revertfailed"  , "bool"               , "Revert to standard download if fails", True ),
                  ("reload"        , "bool"               , "Reload plugin list"                  , True ),
                  ("reloadinterval", "int"                , "Reload interval in hours"            , 12   ),
                  ("ssl"           , "bool"               , "Use HTTPS"                           , True )]

    __description__ = """Real-Debrid.com hook plugin"""
    __license__     = "GPLv3"
    __authors__     = [("Devirex Hazzard", "naibaf_11@yahoo.de")]


    def getHosters(self):
        https = "https" if self.getConfig('ssl') else "http"
        data = getURL(https + "://api.real-debrid.com/rest/1.0/hosts/domains") 

        return json.loads(data)
