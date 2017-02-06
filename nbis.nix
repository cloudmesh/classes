{stdenv, fetchzip, which, cmake, gcc, xorg, withX11 ? false}:

let 

  pickSystem = sysstring:
    if sysstring == "i686-linux" then "--32"
    else if sysstring == "x86_64-linux" then "--64"
    else throw "unsupported system ${sysstring}";

  xorgFlags = withX11: if withX11 then "" else "--without-X11";

  flags = "${pickSystem stdenv.system} ${xorgFlags withX11}";

in

stdenv.mkDerivation {
  name = "NBIS";

  src = fetchzip {
    name = "nbis_v5_0_0";
    url = "http://nigos.nist.gov:8080/nist/nbis/nbis_v5_0_0.zip";
    sha256 = "0q489hajbfmsckd42nwhv4ghljibyjy3xgrw8cjsap07a2sn38iz";
  };

  buildInputs = [ which cmake gcc ];

  configurePhase = ''
    mkdir -p $out
    ./setup.sh $out ${flags}
  '';
}
