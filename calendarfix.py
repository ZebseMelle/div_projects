from ics import Calendar, Event
import os
import pandas as pd

path = os.path.join(os,"kalender.vcs")
vcsfile = read_vcs(path)

#General function that reads a .vcs file
def read_vcs(file):
  with open(file,"r") as f:
    vcs_data=f.read()
  return vcs_data

def remove_segment(data):
  data

