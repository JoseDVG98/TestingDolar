

class PagHistorico:
    #pagina url
    modulo = "//*[@href='https://www.dolar-colombia.com/historico']"
    #Submit de la fecha
    submit = "//*[@class='button']"
    #Calendario para escoger la fecha
    calendario = "//*[@id='fecha']"
    #Dentro de calendario al dar clic en el enunciado de mes y año. El año viene con los {} para formatear un valor en la cadena
    mesyano_calendario="//*[@class='dp__date-control__text']"
    ano_calendario="//*[@class='dp__date-list__item' and @data-value='{}']"
    reversa_calendario="//*[@class='dp-icons dp-icons_prev']"
    dia_calendario="//*[@class='dp__day' and @date-value='{ano},{mes},{dia}']" #El dia viene formateado para buscarlo por fecha exacta

