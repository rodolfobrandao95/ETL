CREATE TABLE [time_dm]
(
    [id] INTEGER NOT NULL,
    [year] INTEGER NOT NULL,
    [month_number] INTEGER NOT NULL,
    [bimonth_number] INTEGER NOT NULL,
    [quarter_number] INTEGER NOT NULL,
    [half_year_number] INTEGER NOT NULL
);

ALTER TABLE [time_dm]
    ADD CONSTRAINT [time_dm_pk] PRIMARY KEY ([id]);

--

CREATE TABLE [city_dm]
(
    [id] INTEGER NOT NULL,
    [city_name] VARCHAR(50) NOT NULL,
    [state_initials] CHAR(2) NOT NULL,
    [state_region] VARCHAR(50) NOT NULL
);

ALTER TABLE [city_dm]
    ADD CONSTRAINT [city_dm_pk] PRIMARY KEY ([id]);

--

CREATE TABLE [fate_dm]
(
    [time_dm_id] INTEGER NOT NULL,
    [city_dm_id ]INTEGER NOT NULL,
    [beneficiaries_number] INTEGER NOT NULL,
    [amount_value] DECIMAL(17,2) NOT NULL
);

ALTER TABLE [fate_dm]
    ADD CONSTRAINT [fate_dm_pk] PRIMARY KEY ([time_dm_id], [city_dm_id]);

ALTER TABLE [fate_dm]
    ADD CONSTRAINT [time_dm_fate_dm_fk] FOREIGN KEY ([time_dm_id])
        REFERENCES [time_dm]([id]);

ALTER TABLE [fate_dm]
    ADD CONSTRAINT [city_dm_fate_dm_fk] FOREIGN KEY ([city_dm_id])
        REFERENCES [city_dm]([id]);