with import <nixpkgs> { };



pkgs.mkShell {
  buildInputs = [
    redis
    postgresql
    (python3.withPackages
      (ps: [
        ps.sqlalchemy
        ps.pandas
        ps.psycopg2
       ]))
];
}
