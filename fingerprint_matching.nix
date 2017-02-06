{ pkgs ? import ./nixpkgs.nix }:

with pkgs;

let pythonTools = python2Full.withPackages (self: [
      self.numpy
      self.pandas
      self.matplotlib
      self.pyqt4
      self.attrs
   ]);

   nbis = callPackage ./nbis.nix {};

in

[ pythonTools nbis ]

