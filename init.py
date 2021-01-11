#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
import json
import logManager
with open('./config.json') as json_file:
    global config
    config = json.load(json_file)

