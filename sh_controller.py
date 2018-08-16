#!/usr/bin/env python3

import os


def sh_input():

    print('________________________')
    print('|                       |')
    print('|                       |')
    print('|     sh controller     |')
    print('|                       |')
    print('|_______________________|')
    
    # initial inputs
    os_username = input('server username: ')
    os_password = input('server password: ')
    git_repo_url = input('git repo url: ')
    email = input('Email Addrss: ')
    vps_ip = input('Server IP: ')
    server_name = input('Server Name: ')
    ssh_port = int(input('SSH Port (number btwn 1024 and 65535): '))

    while ssh_port < 1024 or ssh_port > 65535:
        print('please reneter a valid port number')
        ssh_port = input('SSH Port (number btwn 1024 and 65535): ')
    
    sh_controller(os_username,os_password,git_repo_url,email,vps_ip,server_name,ssh_port)

        # sh - c 'echo "<os_username>:<os_password>" >> .credentials'            

        # ssh root@<vps_ip>

        # user decides what they want to do

def welcome_msg():
    os.system('clear')
    print('Welcome')
    print('What would you like to do?')
    user_input = input('''[1]Nano setup\n\
[2]Permissions\n\
[3]fireWalld\n\
[4]Ntp\n\
[5]nGinx\n\
[6]Fail2ban\n\
[7]Update from Github\n
[A]All\n\
[[X]eXit\n:>''')
    return user_input

def sh_controller(os_username,os_password,git_repo_url,email,vps_ip,server_name,ssh_port):
    user_choice = welcome_msg()
    user_choice = user_choice.lower()
    _nano = ['1', 'nano']
    _permissions = ['2', 'permissions']
    _firewall = ['3', 'firewalld', 'firewall']
    _ntp = ['4', 'ntp']
    _nginx = ['5', 'nginx']
    _fail2ban = ['6', 'fail2ban']
    _git_hub = ['7', 'github']
    _all = ['a', 'all']
    _exit = ['x', 'exit']
    accept_input = _nano     \
                + _permissions  \
                + _firewall     \
                + _ntp  \
                + _nginx    \
                + _fail2ban     \
                + _all  \
                + _exit

    if user_choice in accept_input:
        os.system(f"ssh root@{vps_ip} 'apt-get update'")
        os.system(f"ssh root@{vps_ip} 'apt-get upgrade'")
        os.system(f"ssh root@{vps_ip} 'apt-get install python3-pip'")
        print('updating/upgrading virtual server')

        # generat credentials
        print('generating credentials')
        os.system(f'mkdir {server_name}')
        os.system(f'touch {server_name}/{server_name}_config.sh')
        os.system(f'echo "{os_username}:{os_password}" >> {server_name}/.credentials')


        if user_choice in _nano:
            nano_config(vps_ip, server_name)
            os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/{server_name}_config.sh')
            exit_ssh(server_name)

        elif user_choice in _permissions:
            permissions_config(os_username, server_name)
            os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/{server_name}_config.sh')
            exit_ssh(server_name)

        elif user_choice in _firewall:
            firewall_config(vps_ip, ssh_port, server_name)
            os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/{server_name}_config.sh')
            exit_ssh(server_name)

        elif user_choice in _ntp:
            ntp_config(vps_ip, server_name)
            os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/{server_name}_config.sh')
            exit_ssh(server_name)

        elif user_choice in _nginx:
            nginx_config(vps_ip, server_name)
            os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/{server_name}_config.sh')
            exit_ssh(server_name)

        elif user_choice in _fail2ban:
            fail2ban_config(vps_ip, server_name)
            os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/{server_name}_config.sh')
            exit_ssh(server_name)

        elif user_choice in _git_hub:
            git_clone(vps_ip, git_repo_url)

        elif user_choice in _all:
            print('UPDATING ALL')
            nano_config(vps_ip, server_name)
            permissions_config(os_username, server_name)
            firewall_config(vps_ip, ssh_port, server_name)
            ntp_config(vps_ip, server_name)
            nginx_config(vps_ip, server_name)
            fail2ban_config(vps_ip, server_name)
            git_clone(vps_ip, git_repo_url)
            print('UPDATED ALL OPTIONS') 
            os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/{server_name}_config.sh')
            exit_ssh(server_name)

        elif user_choice in _exit:
            exit_ssh(server_name)

        else:
            print('something went wrong try again')          

    else:
        print('try again')

def nano_config(vps_ip, server_name):
    print('UPDATING NANORC')
    os.system(f"ssh root@{vps_ip} 'apt-get install nano'")
    os.system(f"sed 's/<vps_ip>/{vps_ip}/g' nano_config.sh > {server_name}/{server_name}_config.sh:")

def permissions_config(os_username, server_name):
    print('UPDATING PERMISSIONS')
    os.system(f"sed 's/<os_username>/{os_username}/g' permissions_config.sh > {server_name}/{server_name}_config.sh:")
    # run permission setup 

def firewall_config(vps_ip, ssh_port, server_name):
    print('UPDATING FIREWALLd')
    os.system(f"ssh root@{vps_ip} 'apt-get install firewalld'")
    os.system(f"sed 's/<defined_ssh_port>/{ssh_port}/g' firewalld_config.sh > {server_name}/{server_name}_config.sh:")
    # run firewallb setup

def ntp_config(vps_ip, server_name):
    print('UPDATING NTP')
    os.system(f"ssh root@{vps_ip} 'apt-get install ntp'")
    os.system(f"sed 's/<vps_ip>/{vps_ip}/g' ntp_config.sh > {server_name}/{server_name}_config.sh:")
    # run ntp setup

def nginx_config(vps_ip, server_name):
    print('UPDATING NGINX')
    os.system(f"ssh root@{vps_ip} 'apt-get install nginx'")
    os.system(f"sed 's/<vps_ip>/{vps_ip}/g' nginx_config.sh > {server_name}/{server_name}_config.sh:")
    # run nginx setup 

def fail2ban_config(vps_ip, server_name):
    print('UPDATING FAIL2BAN')
    os.system(f"ssh root@{vps_ip} 'apt-get install fail2ban'")
    os.system(f"sed 's/<vps_ip>/{vps_ip}/g' fail2ban_config.sh > {server_name}/{server_name}_config.sh:")
    # run fail2ban setup 

def git_clone(vps_ip, git_repo_url):
    print('CLONING GIT REPO')
    os.system(f"ssh root@{vps_ip} 'git clone {git_repo_url}'")

def exit_ssh(server_name):
    os.system(f'rm {server_name}/.credentials')
    print('.credentials removed') 





if __name__ == '__main__':
    # sh_controller()
    sh_input()