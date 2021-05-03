from time import sleep
from .processData import process_file

class dataProcessor():
  def __init__(self, force = True):
    print("dataProcessor")

  def pump(self):
    print("pumping")
    # once to start, then loop
    self.parse()
    #while not(sleep(60)):
       #self.parse()

  def parse(self):
    print("parsing file")
    try:
        process_file()
    except Exception as e:
        print("failed to process the file: {}",e)
    
def main():
  print("starting")
  pump = dataProcessor()
  pump.pump()

main()