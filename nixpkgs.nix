with import <nixpkgs> {};

let

  # to update, run:
  # nix-prefetch-git git://github.com/NixOS/nixpkgs-channels refs/heads/nixpkgs-unstable
  src = pkgs.fetchFromGitHub {
    owner = "NixOS";
    repo = "nixpkgs-channels";
    rev = "1fa75a5bb7cdb9f2413d8b20726ce69523bfe4c6"; # 2017/01/02
    sha256 = "1m20qfgqnbbxzxdkf5x5kvhj996zw6pkikzsyckghxcpwh38ipcv";
  };

  pinned-pkgs = import src {};

in
pinned-pkgs
