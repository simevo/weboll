\c
truncate w31_input cascade;
\set command `echo "curl $DATA_LOCATION/w31_input_last_days.copy"`
COPY w31_input FROM PROGRAM :'command' CSV HEADER;
truncate w31_macroaree_input cascade;
\set command `echo "curl $DATA_LOCATION/w31_macroaree_input_last_days.copy"`
COPY w31_macroaree_input FROM PROGRAM :'command' CSV HEADER;
truncate w31 cascade;
\set command `echo "curl $DATA_LOCATION/w31_last_5_days.copy"`
COPY w31 FROM PROGRAM :'command' CSV HEADER;
truncate w31_data_macroaree_livelli cascade;
\set command `echo "curl $DATA_LOCATION/w31_data_macroaree_livelli_last_5_days.copy"`
COPY w31_data_macroaree_livelli FROM PROGRAM :'command' CSV HEADER;
truncate w31_data_macroaree_parametri cascade;
\set command `echo "curl $DATA_LOCATION/w31_data_macroaree_parametri_last_5_days.copy"`
COPY w31_data_macroaree_parametri FROM PROGRAM :'command' CSV HEADER;
truncate w31_data_microaree_livelli cascade;
\set command `echo "curl $DATA_LOCATION/w31_data_microaree_livelli_last_5_days.copy"`
COPY w31_data_microaree_livelli FROM PROGRAM :'command' CSV HEADER;
truncate w31_data_microaree_parametri cascade;
\set command `echo "curl $DATA_LOCATION/w31_data_microaree_parametri_last_5_days.copy"`
COPY w31_data_microaree_parametri FROM PROGRAM :'command' CSV HEADER;