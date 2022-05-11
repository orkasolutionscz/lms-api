import os
import time

import django
import paramiko

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api_rbbackup.models import Routers

username = 'mkadmin'
password = 'G0fXvZXmN3MJs'
backup_folder = '/mnt/mkbackups/'
export_file = 'mkservice_export.rsc'
backup_file = 'mkservice_backup.backup'


def backup_ip(ip, port, sleeptime):
    print(f'Budu zalohovat zarizenis IP: {ip} port: {port}')
    dest_dir = backup_folder + f'{ip}'
    os.makedirs(dest_dir, exist_ok=True)

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=ip,
                       port=port,
                       username=username,
                       password=password,
                       allow_agent=False,
                       look_for_keys=False)

        client.exec_command(f'/export file={export_file}')
        time.sleep(sleeptime)
        client.exec_command(f'/system backup save name={backup_file}')
        time.sleep(sleeptime)
        ftp_client = client.open_sftp()
        ftp_client.get(export_file, f'{dest_dir}/{export_file}')
        ftp_client.get(backup_file, f'{dest_dir}/{backup_file}')
        ftp_client.close()

    except:
        print(f'Chyba pri ukladani souboru zalohy a exportu zarizeni: {ip}')

    client.close()


def run():
    routers = Routers.objects.all()
    for row in routers:
        ip = row.addr
        port = row.port
        sleep_time = row.sleeptime
        backup_ip(ip, port, sleep_time)


def run_oneip(ip):
    row = Routers.objects.get(addr=ip)
    ip = row.addr
    port = row.port
    sleep_time = row.sleeptime
    backup_ip(ip, port, sleep_time)


if __name__ == "__main__":
    run()

