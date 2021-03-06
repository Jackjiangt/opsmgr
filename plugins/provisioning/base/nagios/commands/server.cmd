#--- Monitoring commands for OpsMgr role: server

command[server-cpu]      = sudo /etc/nagios/plugins/check-cpu.rb -w 80 -c 90
command[server-mem]      = sudo /etc/nagios/plugins/check-mem.sh -w 250 -c 100
command[server-disk]     = sudo /etc/nagios/plugins/check-disk.rb -x iso9660
command[server-logs]     = sudo /etc/nagios/plugins/check-for-large-files.sh -d /var/log -s 1048576
command[server-socket]   = sudo /etc/nagios/plugins/check-syslog-socket.rb
command[server-rsyslogd] = sudo /etc/nagios/plugins/check-procs.rb -p rsyslogd -w 80 -c 320 -W 1 -C 1
command[server-sshd]     = sudo /etc/nagios/plugins/check-procs.rb -p sshd -w 80 -c 320 -W 1 -C 1
command[server-cron]     = sudo /etc/nagios/plugins/check-procs.rb -p cron -w 80 -c 320 -W 1 -C 1
