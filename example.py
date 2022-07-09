from scrapli.driver.core import IOSXEDriver
from rich import print as rprint

MY_DEVICE = [
    {
        "host": "192.168.1.12",
        "auth_username": "jcapps",
        "auth_password": "cisco",
        "auth_strict_key": False,
        "ssh_config_file": True,
    },
    {
        "host": "192.168.1.13",
        "auth_username": "jcapps",
        "auth_password": "cisco",
        "auth_strict_key": False,
        "ssh_config_file": True,
    },
    {
        "host": "192.168.1.14",
        "auth_username": "jcapps",
        "auth_password": "cisco",
        "auth_strict_key": False,
        "ssh_config_file": True,
    },
    {
        "host": "192.168.1.15",
        "auth_username": "jcapps",
        "auth_password": "cisco",
        "auth_strict_key": False,
        "ssh_config_file": True,
    },
]

for device in MY_DEVICE:
    with IOSXEDriver(**device) as conn:
        response = conn.send_command("show version")
        structured_result = response.textfsm_parse_output()
    for info in structured_result:
        rprint(info)