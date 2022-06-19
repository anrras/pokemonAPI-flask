DROP TABLE IF EXISTS pokedex;

CREATE TABLE pokedex (
    number INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type_1 TEXT NOT NULL,
    type_2 TEXT,
    total INTEGER NOT NULL,
    hp INTEGER NOT NULL,
    attack INTEGER NOT NULL,
    defense INTEGER NOT NULL,
    sp_atk INTEGER NOT NULL,
    sp_def INTEGER NOT NULL,
    speed INTEGER NOT NULL,
    generation INTEGER NOT NULL,
    legendary BOOLEAN NOT NULL
);