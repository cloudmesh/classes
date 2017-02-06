with import ./nixpkgs.nix;

with pkgs;

let

  pythonTools = with python2Packages; [
    python2Full
    pip
    virtualenv
    ghp-import
    ipython
    ipykernel
    jupyter
    attrs
    matplotlib
    numpy
    scipy
    pandas
  ];

  fingerprint = callPackage ./fingerprint_matching.nix {};

in

stdenv.mkDerivation {
  name = "class-env";
  buildInputs = [
    pythonTools
    pandoc
  ] ++ fingerprint;
  shellHook = ''
    # https://github.com/pikajude/darwinixpkgs/blob/master/doc/languages-frameworks/python.md
    # fixes: ZIP does not support timestamps before 1980
    export SOURCE_DATE_EPOCH=$(date +%s)

    export SSL_CERT_FILE=${cacert}/etc/ssl/certs/ca-bundle.crt
    test -d venv || virtualenv venv
    source venv/bin/activate
  '';
}
