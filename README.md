# xtblock
Use iptables and ipset to block XT nodes

Install ipset:
```	
	apt-get install ipset
```

Clone this repository:
```	
	git clone https://github.com/abitfan/xtblock 
```

Create an ipset bloacklist:
```	
	ipset create xtblock hash:net
```

Add iptables block rule:
```
	ipstables -I INPUT -m set --match-set xtblock src -j DROP
```

Fetch list of XT nodes:
```
	./fetchxtnodes.py > /tmp/xtnodes.txt
```

Add nodes to blacklist:
```
	./reloadipset < /tmp/xtnodes.txt
```

Add to cron:
```
	5 6 * * * /path/to/fetchxtnodes.py > /tmp/xtnodes.txt && /path/to/reloadipset < /tmp/xtnodes.txt
```

