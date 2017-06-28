route delete  172.0.0.0 mask 255.0.0.0 172.16.194.190


route delete  10.0.0.0 mask 255.0.0.0 172.16.194.190


route delete  192.0.0.0 mask 255.0.0.0 172.16.194.190

REM service dhcpd start

REM  linux route add -net 10.0.0.0 netmask 255.0.0.0 gw 172.16.194.190 eth0.2
REM        route add -net 192.0.0.0 netmask 255.0.0.0 gw 172.16.194.190 eth0.2