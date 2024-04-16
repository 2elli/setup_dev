#!/usr/bin/env bash

# check permissions
if [[ $EUID -ne 0 ]]; then
    exec sudo -s "$0" "$@"
fi

handle_args () {
    if [[ $0 == "-p" ]]; then
        echo "$NEEDED_PACKAGES"
    elif [[ $0 == "--help" ]]; then
        echo "Usage"
        echo "-p: print packages that need to be installed"
    else
        return 0
    fi
    exit
}

NEEDED_PACKAGES=(git tmux nvim zsh chezmoi)
ensure_packages () {
    # non-zero exit on failed package
    for pack in ${NEEDED_PACKAGES[@]}; do
        if ! which "$pack" &> /dev/null ; then
            echo "Missing package $pack"
            return 1
        fi
    done
    return 0
}

handle_args

if ensure_packages; then
    echo "All Packages Installed"
else
    echo "Fix missing packages, exiting"
    exit
fi

# copy dots
chezmoi init https://github.com/2elli/dots.git

# setup shell
chsh --shell /bin/zsh

# setup tmux + tpm
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
