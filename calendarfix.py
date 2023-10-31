from ics import Calendar, Event

#General function that reads a .vcs file
def read_vcs(file):
  with open(file,"r") as f:
    vcs_data=f.read()
  return vcs_data

