def compare_groups(data_set, group_col_1, group_col_2, col_count, group_1, group_2, conversion_from, conversion_to, p_value_set=0.05, num_tests=6):
    """
    Esta función calcula las pruebas estadísticas para comparar las proporciones de dos grupos de datos
    basándose en statsmodels.stats.proportion.proportions_ztest y aplica la corrección de Bonferroni si es necesario.
    """
    # Ajuste del nivel de significancia usando la corrección de Bonferroni
    adjusted_p_value_set = p_value_set / num_tests
    
    count = np.array([
        data_set[(data_set[group_col_1] == group_1) & (data_set[group_col_2] == conversion_to)][col_count].nunique(),
        data_set[(data_set[group_col_1] == group_2) & (data_set[group_col_2] == conversion_to)][col_count].nunique()
    ])

    nobs = np.array([
        data_set[(data_set[group_col_1] == group_1) & (data_set[group_col_2] == conversion_from)][col_count].nunique(),
        data_set[(data_set[group_col_1] == group_2) & (data_set[group_col_2] == conversion_from)][col_count].nunique()
    ])

    stat, pval = proportions_ztest(count, nobs)

    print('El p_valor de la prueba es:', np.round(pval, 3))
    print()

    # Interpretación del resultado de la prueba
    if pval < adjusted_p_value_set:
        print('Existe diferencia estadística significativa entre las proporciones de los grupos analizados')
    else:
        print('No existe diferencia estadística significativa entre las proporciones de los grupos analizados')