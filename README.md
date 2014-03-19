httpFlood
=========

This script is designed to put HTTP servers and web applications (PHP/whatever, database, ...) under stress by sending them a (potentially) huge number of simultaneous non-cacheable requests.

It can be __very aggressive__ by :

 * setting the delay between successive requests (`sleepDurationSeconds` parameter) to 0 (zero)
 * allowing multiple processes to run concurrently and send HTTP requests (`nbProcesses`  parameter)


WARNING :
---------

 * this can cause a sudden load on the targetted webserver
 * improper use of this script __can__ cause DoS
 * kiddies, your IP address will be __very easy__ to spot in the web server logs


Final word :
------------

 * __DO! NOT! RUN! THIS! ON! SERVERS! YOU! DON'T! OWN/CONTROL!__
 * use at your own risk
