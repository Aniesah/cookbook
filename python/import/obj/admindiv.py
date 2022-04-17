class AdministrativeDivision:
  def __init__(self, level):
    self.level = level
  
  pass


class Province(AdministrativeDivision):
  type = 'Province'
  area = 0
  center = ''
  
  def __init__(self, name):
    self.name = name
    self.level = 1
  
  def __str__(self):
    return f"{self.name} {self.type}"
  
  pass


class Regency(AdministrativeDivision):
  type = 'Regency'
  area = 0
  center = ''
  
  def __init__(self, name):
    self.name = name
    self.level = 2
  
  def __str__(self):
    return f"{self.name} {self.type}"

  pass

class City(AdministrativeDivision):
  type = 'City'
  area = 0
  center = ''
  
  def __init__(self, name):
    self.name = name
    self.level = 2
  
  def __str__(self):
    return f"{self.name} {self.type}"


class District(AdministrativeDivision):
  type = 'District'
  area = 0
  center = ''
  
  def __init__(self, name):
    self.name = name
    self.level = 3
  
  def __str__(self):
    return f"{self.name} {self.type}"
  
  pass
