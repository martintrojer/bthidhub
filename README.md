# Install

    1. rpi lite(*) image
    2. sudo apt-get install libcairo2-dev libdbus-1-dev libgirepository1.0-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev
    3. python3 -m venv venv
    4. . venv/bin/activate
    5. pip3 install -r requirements.txt

bluez (bubba)

    1. git clone https://github.com/Dreamsorcerer/bluez.git
    2. ./configure --prefix=$HOME/devenv --sysconfdir=/etc --localstatedir=/var --with-dbusconfdir=$HOME/devenv/dbus --with-dbussystembusdir=$HOME/devenv/dbus --with-dbussessionbusdir=$HOME/devenv/dbus --disable-a2dp --disable-avrcp --disable-network --disable-systemd
    3. make -j 2 install

copy devenv over

    1. cd install/on_rpi
    2. cp input.conf main.conf sdp_record.xml /etc/bluetooth

    3. sudo ~/devenv/libexec/bluetooth/bluetoothd -p time,input,hog,autopair,policy,scanparam,deviceinfo
    4. sudo venv/bin/python3 remapper.py
