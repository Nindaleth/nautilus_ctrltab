*Nautilus CtrlTab*
-----------------------
Allow to switch tabs via Ctrl+Shift+Tab/Ctrl+Tab in Nautilus, in addition to the existing Ctrl+PageUp/Ctrl+PageDown hotkeys

Installation
-----------------------
1) Install [Nautilus Python](https://wiki.gnome.org/Projects/NautilusPython)

* Debian-based distributions: `apt-get install python-nautilus`
* Fedora: `dnf install nautilus-python`

2) Download CtrlTabSwitch and install it

`git clone https://github.com/nindaleth/nautilus_ctrltab`
`mkdir -p ~/.local/share/nautilus-python/extensions/`
`ln -s nautilus_ctrltab/CtrlTabSwitch.py ~/.local/share/nautilus-python/extensions/`

3) Restart Nautilus

`killall nautilus`

Acknowledgements
-----------------------
Approach based on [BackspaceBack by Ricardo Lenz](https://github.com/riclc/nautilus_backspace)
