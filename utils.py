#!/usr/bin/env python3

from sys import stderr
from inspect import currentframe,getframeinfo
from datetime import datetime as dt
COLOR_ESCAPE = "%c"%0x1b
YELLOW       = "[33m"
COLOR_ESCAPE_END = "[0m"

def dbg(*debugStatements,segmentChar="|",showPreamble = True):
    """
    print a debug statement with information about which file and line the dbg statement was generated
    *debugStatements is either a single formatted string or series of args that are automatically joined into a string whose symbols are segmented by segmentChar.
    showPreamble: ordinarily show time / file / line location for when/where the dbg statement occurred.  Set to False to suppress.
    """
    cf = currentframe()

    String = segmentChar.join([str(x) for x in debugStatements]) if len(debugStatements) > 1 else str(debugStatements[0])
    Preamble = "[D] {}:{} ({}) -".format(getframeinfo(cf.f_back).filename,cf.f_back.f_lineno,dt.now().strftime("%H:%M%S.%f")) if showPreamble else ''
    DebugMessage = Preamble+String
    stderr.write(f"{COLOR_ESCAPE}{YELLOW}{DebugMessage}{COLOR_ESCAPE}{COLOR_ESCAPE_END}\n")
