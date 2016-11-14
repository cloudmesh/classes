with import <nixpkgs> {};

with pkgs;

let

  pythonTools = with python27Packages; [
    python27Full
    pip
    virtualenv
    ipython
    numpy
    scipy
    pandas
  ];

  nbis = callPackage ./nbis.nix {};

in

stdenv.mkDerivation {
  name = "python-lesson-1";
  buildInputs = [
    pythonTools
    pandoc
  ];
  shellHook = ''
    test -d venv || virtualenv venv
    source venv/bin/activate
  '';
}
