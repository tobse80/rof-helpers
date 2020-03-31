from sys import platform
from subprocess import run, CompletedProcess

def is_target_reachable(target:str, tmoSec:int=1) -> bool:
   result = ping(target, tmoSec)
   if result.returncode:
      return False
   elif 'ttl' in str(result.stdout).lower():
      return True
   else:
      return False

def ping(target:str, tmoSec:int=1, count:int=1, size:int=64) -> CompletedProcess:
   if platform.startswith('linux'):
      cmd = ['ping', '-W', str(tmoSec), '-c', str(count), '-s', str(size - 8), target]
   elif platform.startswith('win'):
      cmd = ['ping', '-w', str(tmoSec * 1000), '-n', str(count), '-l', str(size), target]
   else:
      raise RuntimeError('"' + str(platform) + '" not supported.')

   return run(cmd, timeout = tmoSec + 1, capture_output = True)
