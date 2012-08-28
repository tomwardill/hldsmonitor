hldsmonitor
===========

A [Server Density](http://www.serverdensity.com) plugin for monitoring the ping and number of players on a Valve Dedicated Server (HL2, TF2, CS:S).

Installation
------------

You will first require [SourceLib](https://github.com/frostschutz/SourceLib), the easiest way to install it is from a branch that supports egg install.

1. ```sudo easy_install https://github.com/tomwardill/SourceLib/tarball/master```
2. Follow the [Writing a plugin guide](http://support.serverdensity.com/knowledgebase/articles/76018-writing-a-plugin-linux-mac-and-freebsd). This is a bit awkward, but the plugin is not on the plugin directory for Server Density.
3. Add the following to your agent configuration:

```
[Hldsmonitor]
server = SERVERIP
port = SERVERPORT
```

4. Restart your agent

Enjoy your graphs.