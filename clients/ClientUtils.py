from datetime import date, timedelta 
import uuid

def uuidStr() -> str:
  return str(uuid.uuid4())

def todayStr() -> str:
  return str(date.today())

def tomorrowStr() -> str:
  return str(date.today() + timedelta(days=2))