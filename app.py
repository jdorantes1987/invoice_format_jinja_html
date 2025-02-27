import os
import webbrowser 

from jinja2 import Template

# CUIT que emitio la factura
#
# Podes usar 20409378472 para desarrollo
# sin necesidad de key o cert
# Para mas info https://docs.afipsdk.com/paso-a-paso/instalacion

html = open(r"templates\invoice.html").read()

# Datos de la empresa
business_data = {
	'business_name': 'María Pérez.', # Nombre / Razon social
	'address': 'Mi dirección', # Direccion
	'tax_id': '+58 4143893828', # CUIL/CUIT
	'gross_income_id': 12345432, # Ingresos brutos
	'start_date': '25/10/2017', # Fecha inicio de actividades
	'vat_condition': 'Responsable inscripto' # Condicion frente al IVA
}

# Datos del comprobante
bill = {
	'number': '000000032', # Numero de comprobante
	'point_of_sale': '0001', # Numero del punto de venta
	'date': '25/10/2017', # Fecha de emision del comprobante
	'since': '25/10/2017', # Fecha de comienzo
	'until': '25/10/2017', # Fecha de fin
	'expiration': '25/10/2017', # Fecha de expiracion del comprobante
	'type': 'B', # Tipo de comprobante
	'code': '6', # Codigo de tipo del comprobante
	'concept': 'Productos', # Concepto del comprobante (Productos / Servicios / Productos y servicios)
	'CAE': 12345678912345, # CAE
	'CAE_expiration': '05/11/2017' # Fecha de expiracion del CAE
}

# Items del comprobante
items = [
	{
		'code': '321', # Codigo
		'name': 'Cafe Americano', # Nombre
		'quantity': '1,00', # Cantidad
		'measurement_unit': 'Unidad', # Unidad de medida
		'price': '1500,00', # Precio
		'tax_percent': '21%', # Precio
		'percent_subsidized': '0,00', # Precio subsidiado
		'impost_subsidized': '0,00', # Impuestos subsidiado
		'subtotal': '1500,00' # Subtotal
	}
]

# Datos de a quien va emitido del comprobante
billing_data = {
	'tax_id': 12345678912, # Document/CUIT/CUIL
	'name': 'Pepe perez', # Nombre / Razon social
	'vat_condition': 'Consumidor final', # Condicion frente al iva
	'address': 'Calle falsa 123', # Direccion
	'payment_method': 'Efectivo' # Forma de pago
}

# Resumen
overall = {
	'subtotal': '150,00', # Subtotal
	'impost_tax': '0,00', # Tributos
	'total': '150,00', # Total
}


# Iniciamos el template con el HTML
template = Template(html)

# Generamos el HTML con los datos de nuestro comprobante
template_html = template.render(
    business_data= business_data,
    bill= bill,
    items= items,
    billing_data= billing_data,
    overall= overall
)

filename = os.getcwd() + '/' + 'files/PDF/edo_cta.html'

with open(filename, 'w', encoding='utf-8') as f:
    f.write(template_html)
    f.close

rdFile = webbrowser.open(filename)  #Full path to your file