#Achieve terminal capabilities through modules in python and built-in methods
import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
stdin, stdout, stderr=ssh.exec_command("uptime")
stdout.read()
