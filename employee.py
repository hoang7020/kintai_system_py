import json
from json import JSONEncoder

class Employee:
  def __init__(self, name, u_time, s_time, email):
    self.name = name
    self.u_time = u_time
    self.s_time = s_time
    self.email = email
    
  def toJson(self):
      return json.dumps(self, default=lambda o: o.__dict__)

# subclass JSONEncoder
class EmployeeEncoder(JSONEncoder):
  def default(self, o):
    return o.__dict__