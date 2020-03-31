#!/usr/bin/env python
import yaml

f = open('default/config.yml')
dataMap = yaml.load(f)
f.close()

print(dataMap)