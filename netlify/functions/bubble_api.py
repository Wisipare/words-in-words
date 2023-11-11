# bubble_api.py

def handler(event, context):
    # Lógica para procesar la solicitud
    # Llama a tu función Python existente o ejecuta el código necesario
    result = "Hola desde la API de Netlify con Python"

    # Devuelve la respuesta
    return {
        "statusCode": 200,
        "body": result
    }