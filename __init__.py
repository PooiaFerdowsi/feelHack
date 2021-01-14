import os;

while True:
  text = input("statement");
  if text = 'init':
    print('Virus files has make');
    # make virus codes
    try:
      os.mkdir(input('Virus path'));
     except FileNotFoundError:
      print('Path is not valid');
     # to make virus files
    lang = None;
    if os.name == "nt":
      lang = "bat";
    if os.name == "posix":
      lang = "bash";
    print('Virus maked');
