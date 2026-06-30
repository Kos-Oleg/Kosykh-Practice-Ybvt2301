#!/bin/bash
set -e
echo "=== Установка Zabbix 6.0 ==="
wget https://repo.zabbix.com/zabbix/6.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.0-4+ubuntu22.04_all.deb
dpkg -i zabbix-release_6.0-4+ubuntu22.04_all.deb
apt update
apt install -y zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent
echo "=== Установка Zabbix завершена ==="
echo "Доступ: http://192.168.1.10/zabbix (Admin/zabbix)"
