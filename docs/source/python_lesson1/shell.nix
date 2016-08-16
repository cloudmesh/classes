with import <nixpkgs> {};

with pkgs;

let

  pythonTools = with python27Packages; [
    python27Full
    pip
    virtualenv
    numpy
  ];

  nbis = callPackage ./nbis.nix {};

in

stdenv.mkDerivation {
  name = "python-lesson-1";
  buildInputs = [
    pythonTools
    nbis
  ];
}
