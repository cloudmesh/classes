with import <nixpkgs> {};

with pkgs;

let

  pythonTools = with python27Packages; [
    python27Full
    pip
    virtualenv
    numpy
    scipy
    matplotlib
    pandas
    statsmodels
    cycler
    pyqt4
  ];

  nbis = callPackage ./nbis.nix {};

in

stdenv.mkDerivation {
  name = "python-lesson-1";
  buildInputs = [
    pythonTools
    nbis
    pkgs.sqlite
    pkgs.sqlite-interactive
    pkgs.sqlitebrowser
  ];
  shellHook = ''
    test -d venv || virtualenv venv
    source venv/bin/activate
  '';
}
