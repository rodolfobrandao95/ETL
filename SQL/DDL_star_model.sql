CREATE TABLE [CITY_DM]
(
    id INTEGER NOT NULL,
    city_name VARCHAR(50) NOT NULL,
    state_name VARCHAR(50) NOT NULL,
    state_initials CHAR(2) NOT NULL
);

ALTER TABLE [CITY_DM]
    ADD CONSTRAINT city_dm_pk PRIMARY KEY ([id]);

-- //////////////////////////////////////////////////////////////////////

CREATE TABLE [TIME_DM]
(
    id INTEGER NOT NULL,
    month_number INTEGER NOT NULL,
    bimonth_number INTEGER NOT NULL,
    quarter_number INTEGER NOT NULL,
    half_year_number INTEGER NOT NULL
);

ALTER TABLE [TIME_DM]
    ADD CONSTRAINT time_dm_pk PRIMARY KEY ([id]);

-- //////////////////////////////////////////////////////////////////////

CREATE TABLE [FATE_DM]
(
    CITY_DM_id INTEGER NOT NULL,
    TIME_DM_id INTEGER NOT NULL,
    beneficiaries_number INTEGER NOT NULL,
    amount_value DECIMAL(17,2) NOT NULL
);

ALTER TABLE [FATE_DM]
    ADD CONSTRAINT fate_dm_pk PRIMARY KEY ([CITY_DM_id], [TIME_DM_id]);

ALTER TABLE [FATE_DM]
    ADD CONSTRAINT city_dm_fate_dm_fk FOREIGN KEY ([CITY_DM_id])
        REFERENCES [CITY_DM] ([id]);

ALTER TABLE [FATE_DM]
    ADD CONSTRAINT time_dm_fate_dm_fk FOREIGN KEY ([TIME_DM_id])
        REFERENCES [TIME_DM] ([id]);