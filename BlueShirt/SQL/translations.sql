CREATE TABLE translations (
    id SERIAL PRIMARY KEY,
    tkey TEXT NOT NULL,
    tlanguage TEXT NOT NULL,
    ttext TEXT NOT NULL,
    unique(tkey, tlanguage, ttext)
)