*** Settings ***
Library           common/ping.py

*** Test Cases ***
Ping Google
   Wait Until Keyword Succeeds   10s   1s    Is target reachable   google.de

*** Keywords ***
