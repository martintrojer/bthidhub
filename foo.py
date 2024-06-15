
from dasbus.connection import SystemMessageBus
import crypt, spwd, subprocess


bus = SystemMessageBus()

ADAPTER_OBJECT = '/org/bluez/hci0'
ADAPTER_INTERFACE = 'org.bluez.Adapter1'

adapter = bus.get_proxy(service_name="org.bluez", object_path=ADAPTER_OBJECT, interface_name=ADAPTER_INTERFACE)

print(adapter)

password = spwd.getspnam('martintrojer').sp_pwdp
