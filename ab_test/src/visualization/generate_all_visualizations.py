def generate_all_visualizations(df_a, target_date):
    """
    Genera y muestra una serie de visualizaciones de eventos y usuarios.
    Parámetros:
    - df_a: DataFrame principal con los eventos.
    - data_filtered: DataFrame filtrado para el embudo.
    """

    
    
    
    data_counts = df_a.groupby('event_name')['device_id_hash'].agg([
        ('total_events', 'count'),
        ('unique_users', 'nunique')
    ]).reset_index().sort_values(by='total_events', ascending=False)


    data_filtered = df_a[df_a['event_timestamp'] >= target_date]
    
    plt.figure(figsize=(14, 8))
    sns.set_style("darkgrid")
    
    
    for i, row in data_counts.iterrows():
        plt.barh(row['event_name'], row['total_events'], color='royalblue', alpha=0.6, 
                 label='Total Events' if i == 0 else "")
        plt.barh(row['event_name'], row['unique_users'], color='teal', alpha=0.6, 
                 label='Unique Users' if i == 0 else "")

    plt.xlabel('Conteo')
    plt.ylabel('Nombre del evento')
    plt.title('Total de eventos y usuarios únicos por evento')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

  
    plt.figure(figsize=(15, 6))
    counts = df_a.groupby('device_id_hash')['event_name'].count()
    counts.hist(bins=150, color='teal')
    plt.xlabel('Número de eventos')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de los eventos')
    plt.xlim(0, 300)

    # Creación de gráfico con serie de tiempo. 
    plt.figure(figsize=(15, 6))
    data_ev = df_a.groupby('date')['event_name'].count()
    data_ev.plot(kind='line', marker='o')
    plt.title('Evolución de los datos de tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Número de eventos')

   # Creación del embudo de eventos.
    data_counts_filtered = data_filtered.groupby('event_name')['device_id_hash'].agg([
        ('total_events', 'count'),
        ('unique_users', 'nunique')
    ]).reset_index().sort_values(by='total_events', ascending=False)


    fig = go.Figure(go.Funnel(
        y = data_counts_filtered['event_name'],
        x = data_counts_filtered['unique_users'],
        marker=dict(color=['royalblue', 'cornflowerblue', 'royalblue', 'cornflowerblue', 'royalblue'])
    ))
    fig.update_layout(title='Embudo de usuarios por eventos')
    
    print(f" Se filtraron los datos usando la fecha correspondiente a: {target_date}\n")
    data_loss = (1-(data_filtered['event_name'].count() / data['event_name'].count()))*100
    print(f'Al filtrar los datos, se pierden {data_loss:.4f}% de los datos.')
    
   
    fig.show()   
    plt.show()  