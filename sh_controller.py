#!/usr/bin/env python3

import os


def sh_input():

    print('_________________________')
    print('|                        |')
    print('|       DEPLOYMENT       |')
    print('|                        |')
    print('|         SCRIPT         |')
    print('|________________________|')
    
    # initial inputs
    username = input('server username: ')
    password = input('server password: ')
    email = input('Email Addrss: ')
    server_name = input('Server Name: ')
    vps_ip = input('Server IP: ')
    ssh_port = int(input('SSH Port (number btwn 1024 and 65535): '))
    git_repo_url = input('git repo url: ')

    while ssh_port < 1024 or ssh_port > 65535:
        print('please reneter a valid port number')
        ssh_port = input('SSH Port (number btwn 1024 and 65535): ')
    
    sh_controller(username, password, git_repo_url, email, vps_ip, server_name, ssh_port)

def welcome_msg():
    os.system('clear')
    print('Welcome')
    print('What would you like to do?')
    user_input = input('''[1]Permissions\n\
[2]fireWalld\n\
[3]Ntp\n\
[4]nGinx\n\
[5]Fail2ban\n\
[6]Update from Github\n
[A]All\n\
[[X]eXit\n:>''')
    return user_input

def sh_controller(username,password,git_repo_url,email,vps_ip,server_name,ssh_port):
    user_choice = welcome_msg()
    user_choice = user_choice.lower()
    _permissions = ['1', 'permissions']
    _firewall = ['2', 'firewalld', 'firewall']
    _ntp = ['3', 'ntp']
    _nginx = ['4', 'nginx']
    _fail2ban = ['5', 'fail2ban']
    _git_hub = ['6', 'github']
    _all = ['a', 'all']
    _exit = ['x', 'exit']
    accept_input = _permissions  \
                + _firewall     \
                + _ntp  \
                + _nginx    \
                + _fail2ban     \
                + _all  \
                + _exit

    if user_choice in accept_input:
        # TODO replace the next 3 lines with initial server setup
        os.system(f"ssh root@{vps_ip} 'apt-get update'")
        os.system(f"ssh root@{vps_ip} 'apt-get upgrade'")
        os.system(f"ssh root@{vps_ip} 'apt-get install python3-pip tree'")

        os.system(f'mkdir {server_name}')
# genertate Credentials
        cred_gen(username, password, server_name, vps_ip)
# nano config settings 
        nano_config(vps_ip, server_name)
        print('updating/upgrading virtual server')
# generate username/password to .credentials
        create_user(username, password, vps_ip, server_name)
        print('generating credentials')
# setting ssh key
        set_ssh_key(username, server_name, vps_ip)


        if user_choice in _permissions:
            permissions_config(vps_ip, username, server_name)
            os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/{server_name}_config.sh')
            exit_ssh(server_name)

        elif user_choice in _firewall:
            firewall_config(vps_ip, ssh_port, server_name, username)
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
            firewall_config(vps_ip, ssh_port, server_name, username)
            ntp_config(vps_ip, server_name)
            nginx_config(vps_ip, server_name)
            fail2ban_config(vps_ip, server_name)
            git_clone(vps_ip, git_repo_url)
            permissions_config(vps_ip, username, server_name)
            print('UPDATED ALL OPTIONS') 

            exit_ssh(server_name)

        elif user_choice in _exit:
            exit_ssh(server_name)

        else:
            print('something went wrong try again')          

    else:
        print('try again')

def local(server_name):
    os.system(f'chmod +x /{server_name}/*.sh' )


def cred_gen(username, password, server_name,vps_ip):
    os.system(f"sed 's/<os_username>/{username}/g; s/<os_password>/{password}/g; s/<server_name>/{server_name}/g' cred_gen.sh > {server_name}/cred_config.sh")
    #local(server_name)
    os.system(f'chmod +x {server_name}/cred_config.sh')
    os.system(f"./{server_name}/cred_config.sh")

def create_user(username, password, vps_ip, server_name):
    os.system(f"sed 's/<os_username>/{username}/g; s/<server_name>/{server_name}/g' user_setup.sh > {server_name}/user_config.sh")
    local(server_name)
    os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/user_config.sh')

def set_ssh_key(username, server_name, vps_ip):
    os.system(f"sed 's/<vps_ip_addr>/{vps_ip}/g; s/<os_username>/{username}/g' ssh_copier.sh > {server_name}/ssh_config.sh")
    local(server_name)
    os.system(f'./{server_name}/ssh_config.sh')
    
def nano_config(vps_ip, server_name):
    print('UPDATING NANORC')
    os.system(f"ssh root@{vps_ip} 'apt-get install nano'")
    os.system(f"sed 's/<vps_ip>/{vps_ip}/g' nano_config.sh > {server_name}/nano_config.sh")
    os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/nano_config.sh')

def permissions_config(vps_ip, username, server_name):
    print('UPDATING PERMISSIONS')
    os.system(f"sed 's/<os_username>/{username}/g' password.sh > {server_name}/password_config.sh")
    local(server_name)
    os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/password_config.sh')
    os.system(f"sed 's/<os_username>/{username}/g' permissions_config.sh > {server_name}/permissions_config.sh")
    local(server_name)
    os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/permissions_config.sh')
    # run permission setup 

def firewall_config(vps_ip, ssh_port, server_name, username):
    print('UPDATING FIREWALLd')
    os.system(f"ssh root@{vps_ip} 'apt-get install firewalld'")
    os.system(f"sed 's/<defined_ssh_port>/{ssh_port}/g;s/<os_username>/{username}/g' firewalld_config.sh > {server_name}/firewall_config.sh")
    os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/firewall_config.sh')
    # run firewallb setup

def ntp_config(vps_ip, server_name):
    print('UPDATING NTP')
    os.system(f"ssh root@{vps_ip} 'apt-get install ntp'")
    os.system(f"sed 's/<vps_ip>/{vps_ip}/g' ntp_config.sh > {server_name}/ntp_config.sh")
    os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/ntp_config.sh')
    # run ntp setup

def nginx_config(vps_ip, server_name):
    print('UPDATING NGINX')
    os.system(f"ssh root@{vps_ip} 'apt-get install nginx'")
    os.system(f"sed 's/<vps_ip>/{vps_ip}/g' nginx_config.sh > {server_name}/nginx_config.sh")
    os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/nginx_config.sh')
    # run nginx setup 

def fail2ban_config(vps_ip, server_name):
    print('UPDATING FAIL2BAN')
    os.system(f"ssh root@{vps_ip} 'apt-get install fail2ban'")
    os.system(f"sed 's/<vps_ip>/{vps_ip}/g' fail2ban_config.sh > {server_name}/fail2ban_config.sh")
    os.system(f'ssh root@{vps_ip} "bash -s" < ./{server_name}/fail2ban_config.sh')
    # run fail2ban setup 

def git_clone(vps_ip, git_repo_url):
    print('CLONING GIT REPO')
    os.system(f"ssh root@{vps_ip} 'git clone {git_repo_url}'")

def exit_ssh(server_name):
    # os.system(f'rm {server_name}/.credentials')
    # os.system(f'ssh root@{vps_ip} "bash -s" < ./remove_cred.sh')
    # print('.credentials removed') 
    print('where is the .credentials file?')




if __name__ == '__main__':
    # sh_controller()
    sh_input()
    # cred_gen('greg6', 'greg6', 'greg6', '127.0.0.1',)