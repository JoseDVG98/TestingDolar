

class PagCalculadora:
    modulo = "//*[@href='https://www.dolar-colombia.com/calculadora']"
    check_dolar_peso = "//label[@for='conversionDP']"
    check_peso_dolar = "//label[@for='conversionPD']"
    # Calendario para escoger la fecha
    calendario = "//*[@id='fecha']"
    # Dentro de calendario al dar clic en el enunciado de mes y año. El año viene con los {} para formatear un valor en la cadena
    mesyano_calendario = "//*[@class='dp__date-control__text']"
    ano_calendario = "//*[@class='dp__date-list__item' and @data-value='{}']"
    reversa_calendario = "//*[@class='dp-icons dp-icons_prev']"
    dia_calendario = "//*[@class='dp__day' and @date-value='{ano},{mes},{dia}']"
    input_valor = "//input[@id='valor']"
    calcular = "//button[@class='button button_bold']"
    valor="//div[3]/strong/abbr"









