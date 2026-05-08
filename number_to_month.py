# Replace the "ANSWER HERE" for your answer

def number_to_month(month):
    meses={
        1:"enero",
        2:"febrero",
        3:"marzo",
        4:"abril",
        5:"mayo",
        6:"junio",
        7:"julio",
        8:"agosto",
        9:"septiembre",
        10:"octubre",
        11:"noviembre",
        12:"diciembre",

    }
    if month in meses: salida=meses[month]
    else: salida="error"

    return salida