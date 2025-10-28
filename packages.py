import argparse
from pathlib import Path

# init packages
initp = lambda x: " ".join(x.strip().splitlines())
# init script
inits = lambda x: x.strip()

############################################# PACMAN
PACMAN_PACKAGES = initp("""
base-devel
git
make
cmake
neovim
zsh
tmux
keyd
chezmoi
python-pipx
gdb
make
fd
fzf
ripgrep
jq
seahorse
""")

############################################ AUR
AUR_HELPER = "paru"

INSTALL_AUR_HELPER = inits(f"""
git clone https://aur.archlinux.org/{AUR_HELPER}.git
cd {AUR_HELPER}
makepkg -si
""")

AUR_PACKAGES = initp("""
librewolf
tofi
""")

WAYLAND_PACKAGES = initp("""
i3status-rust
sway-contrib
swaync
nwg-displays
nwg-look
autotiling-rs
swaylock
i3status-rust
waybar
""")

PIPX_PACKAGES = initp("""
normcap
""")


############################################ extras
INSTALL_MISE = inits("""
curl https://mise.run | sh
""")

INSTALL_PYENV = inits("""
curl -fsSL https://pyenv.run | bash
""")

CHEZMOI_URL = "https://github.com/2elli/dots"

INIT_CHEZMOI = inits(f"""
chezmoi init {CHEZMOI_URL} --apply
""")

INIT_NEOVIM = inits("""
git clone https://github.com/2elli/nvim.git ~/.config/nvim
""")


def main():
    parser = argparse.ArgumentParser(prog="packages", description="helper script for installing needed packages")
    parser.add_argument("--all", action="store_true", help="print all")

    parser.add_argument("--all_packages", action="store_true", help="print all packages")
    parser.add_argument("--pacman", action="store_true", help="print pacman packages")
    parser.add_argument("--aur", action="store_true", help="print aur packages")
    parser.add_argument("--wayland", action="store_true", help="print wayland packages")
    parser.add_argument("--pipx", action="store_true", help="print pipx packages")

    parser.add_argument("--all_extras", action="store_true", help="print extra scripts")
    parser.add_argument("--pyenv", action="store_true", help="print pyenv install script")
    parser.add_argument("--mise", action="store_true", help="print mise install script")
    parser.add_argument("--chezmoi", action="store_true", help="print chezmoi script")
    parser.add_argument("--copy_keyd", action="store_true", help="print script to copy keyd from chezmoi to correct place")
    parser.add_argument("--nvim", action="store_true", help="setup nvim")

    args = parser.parse_args()

    # packages
    a = args.all or args.all_packages
    if a:
        print("# packages")
    if a or args.pacman:
        print("## pacman")
        print(("pacman -S --needed" if a else "") + PACMAN_PACKAGES)
    if a or args.aur:
        print("## aur")
        print((f"{AUR_HELPER} -S " if a else "") + AUR_PACKAGES)
    if a or args.wayland:
        print("## wayland")
        print(("pacman -S " if a else "") + WAYLAND_PACKAGES)
    if a or args.pipx:
        print("## pipx")
        print(PIPX_PACKAGES)

    # extras
    e = args.all or args.extras
    if e:
        print("# scripts")
    if e or args.pyenv:
        print("## pyenv")
        print(INSTALL_PYENV)
    if e or args.mise:
        print("## mise")
        print(INSTALL_MISE)
    if e or args.chezmoi:
        print("## chezmoi")
        print(INIT_CHEZMOI)
    if e or args.keyd:
        print("## copy keyd")
        print("cp $(chezmoi source-path)/dot_config/keyd/default.conf /etc/keyd/")
    if e or args.nvim:
        print("## neovim")
        print(INIT_NEOVIM)


if __name__ == "__main__":
    main()
