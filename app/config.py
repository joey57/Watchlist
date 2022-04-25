class Config:
  '''
  General configuration parent class
  '''
  pass

class ProdConfig:
  '''
  Production configuration child class
  Args:
    Config: The parent configuration class with General configuration settings
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class
  Args: 
       Config: The parent configuration class with general configuration settings
  '''
  DEBUG = True

