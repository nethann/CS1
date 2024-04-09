class NegativeVal(Exception):
  def __init__(self, message="Negative Step count entered"): 
    self.message = message
    Exception.__init__(self, self.message)

    
def steps_to_miles(num_steps):
  try: 
    person_steps = int(num_steps)
    if person_steps < 0: 
      raise NegativeVal

    else:
      miles = person_steps / 2000
      return miles

  except ValueError: 
    raise ValueError("Exception: Non-numeric value Entered")

def main():
  try:
      steps = input("Enter the number of steps: ")
      miles = steps_to_miles(steps)
      print(f'Miles walked: {miles:.2f}')
  except (ValueError, NegativeVal) as caught_error:
      print(caught_error)

main()
