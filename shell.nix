with import ./nixpkgs.nix;

with pkgs;

let

  pythonTools = with python2Packages; [
    python2Full
    pip
    virtualenv
    ghp-import
    ipython
    numpy
    scipy
    pandas
  ];

in

stdenv.mkDerivation {
  name = "class-env";
  buildInputs = [
    pythonTools
    pandoc
  ];
  shellHook = ''
    # https://github.com/pikajude/darwinixpkgs/blob/master/doc/languages-frameworks/python.md
    # fixes: ZIP does not support timestamps before 1980
    export SOURCE_DATE_EPOCH=$(date +%s)

    export SSL_CERT_FILE=${cacert}/etc/ssl/certs/ca-bundle.crt
    test -d venv || virtualenv venv
    source venv/bin/activate
  '';
}
