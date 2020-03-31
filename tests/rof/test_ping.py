from .context import rof
import pytest

def test_is_target_reachable__loopback():
   # should always succeed
   assert rof.is_target_reachable("127.0.0.1")

def test_is_target_reachable__linklocal():
   # assumption: specific address is not present in current link-local net
   # PING: Fehler bei der Übertragung. Allgemeiner Fehler.
   assert not rof.is_target_reachable("169.254.0.1")

def test_is_target_reachable__private():
   # assumption: specific address is not present in this private net
   # Antwort von a.b.c.d: Zielnetz nicht erreichbar.
   assert not rof.is_target_reachable("192.168.212.212")

def test_is_target_reachable__notReachable():
   # assumption: specific address is not reachable
   # Zeitüberschreitung der Anforderung.
   assert not rof.is_target_reachable("2.3.4.5")

@pytest.mark.timeout(1)
def test_is_target_reachable__noTimeout():
   # assumption: specific address is not reachable
   # Zeitüberschreitung der Anforderung.
   assert not rof.is_target_reachable("2.3.4.5", tmoSec=0)
