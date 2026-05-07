CREATE TABLE if NOT EXISTS ensayo_virus_g(
    id_registro SERIAL PRIMARY KEY, 
    id_sujeto VARCHAR(50), 
    edad INT, 
    tipo_sangre VARCHAR(5),
    exposicion_previa_t_virus BOOLEAN, 
    nivel_biomarcador_g FLOAT, 
    carga_viral_inicial FLOAT, 
    mutacion_estable BOOLEAN, 
    log_biomarcador_g FLOAT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);