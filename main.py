# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online
import sys

def check_version(call_name):
  print(f'Try programiz.pro using python {sys.version}')
  name = f'as called "{call_name}"'
  message = f'Here is how I was {name}'
  print(message)


if __name__ == '__main__':
  check_version(__name__)
else:
  print("I'm not __main__")