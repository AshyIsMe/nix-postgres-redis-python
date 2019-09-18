with import <nixpkgs> { };



pkgs.mkShell {
  buildInputs = [
    redis
    postgresql
    (python3.withPackages
      (ps: [
        ps.elasticsearch
        ps.beautifulsoup4
        ps.requests
        ps.pytz
       ]))
];
}
