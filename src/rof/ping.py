import sys
import subprocess

def is_target_reachable(target:str, timeout=1) -> bool:
   result = ping(target, timeout)
   if result.returncode:
      return False
   elif 'ttl' in str(result.stdout).lower():
      return True
   else:
      return False

def ping(target:str, timeout:int=1, count:int=1, size:int=64) -> subprocess.CompletedProcess:
   if timeout < 0: timeout = 0  # 0 means forever
   if count < 1: count = 1
   if size < 8: size = 8

   if sys.platform.startswith('linux'):
      cmd = ['ping', '-c', str(count), '-s', str(size - 8), '-W', str(timeout), target]
   elif sys.platform.startswith('win'):
      cmd = ['ping', '-n', str(count), '-l', str(size)]
      if timeout == 0:
         cmd.append('-t')
      else:
         cmd.extend(('-w', str(timeout * 1000)))
      cmd.append(target)
   else:
      raise RuntimeError('"' + str(platform) + '" not supported.')

   return subprocess.run(cmd, timeout = timeout + 1, capture_output = True)
