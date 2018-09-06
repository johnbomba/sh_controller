# put the server updates, upgrades, pip and tree install here

os.system(f"ssh root@{vps_ip} 'apt-get update'")
os.system(f"ssh root@{vps_ip} 'apt-get upgrade'")
os.system(f"ssh root@{vps_ip} 'apt-get install python3-pip tree'")
