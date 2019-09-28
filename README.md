# Nautilus CtrlTab

Allow to switch tabs via `Ctrl+Shift+Tab` and `Ctrl+Tab` in Nautilus, in addition to the existing `Ctrl+PageUp` and `Ctrl+PageDown` hotkeys

## Installation

### 1) Install [Nautilus Python](https://wiki.gnome.org/Projects/NautilusPython)

* Fedora: `dnf install nautilus-python`
* Ubuntu and other Debian-based distributions: `apt install python-nautilus`
* Arch Linux: `pacman -S python-nautilus`
* openSUSE: `zypper install python-nautilus`
* Solus: `eopkg install nautilus-python`

### 2) Get CtrlTabSwitch and install it

```
git clone https://github.com/Nindaleth/nautilus_ctrltab
mkdir -p ~/.local/share/nautilus-python/extensions/
ln -s nautilus_ctrltab/CtrlTabSwitch.py ~/.local/share/nautilus-python/extensions/
```

### 3) Restart Nautilus

```
killall nautilus
```

## Acknowledgements

Approach based on [BackspaceBack by Ricardo Lenz](https://github.com/riclc/nautilus_backspace)
