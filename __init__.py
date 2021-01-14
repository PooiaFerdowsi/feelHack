import os;
import subprocess;

while True:
  text = input("statement");
  if text == 'init':
    print('Virus files has make');
    # make virus codes

    lang = None;
    if os.name == "nt":
      lang = "bat";
    if os.name == "posix":
      lang = "bash";
     #
    if lang == "bat":
      file = open("main.bat","w+");
      file.write("""
             @echo off
             color 0a
             mode 1000
       
            :a
 
             echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
 
             ping > nul
             ping > nul
             ping > nul
 
            goto a
                 """);
      file.close();         
      print('Virus maked');
      subprocess.call([r'main.bat']);
      os.remove('main.bat');
                 
                 
