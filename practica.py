import pymongo
import json

#myclient = pymongo. MongoClient ("mongodb://Localhost: 27017")
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

print(myclient)
mydb = myclient["netflix2"]
mycoll = mydb["data"]


#print('1er. CONSULTA -----------------------------------------------------------------------')

# # Consulta para encontrar el documento con el título "Taxi Driver"
# document = mycoll.find_one({"title": "Taxi Driver"})

# # Imprimir el documento encontrado
# print(document)


#print('3ra. CONSULTA -----------------------------------------------------------------------')

# # Consulta para actualizar los documentos
# result = mycoll.update_many({"type": "MOVIE"}, {"$set": {"seasons": 1}})

# # Imprimir el número de documentos actualizados
# print("Número de documentos actualizados:", result.modified_count)



#print('5ta. CONSULTA -----------------------------------------------------------------------')

# # Consulta para eliminar los documentos
# result = mycoll.delete_many({"release_year": {"$lt": 2000}})

# # Imprimir el número de documentos eliminados
# print("Número de documentos eliminados:", result.deleted_count)



# print('7ma. CONSULTA -----------------------------------------------------------------------')

# # Consulta para encontrar películas del género 'thriller'
# thriller_movies = mycoll.find({"genres": "thriller", "type": "MOVIE"})

# # Imprimir los títulos de las películas encontradas
# print("Películas del género 'thriller':")
# for movie in thriller_movies:
#     print(movie["title"])



print('9na. CONSULTA -----------------------------------------------------------------------')

# Consulta de agregación para encontrar la película con la puntuación de IMDb más alta
pipeline = [
    {"$match": {"type": "MOVIE"}},  # Filtro para seleccionar solo películas
    {"$group": {"_id": None, "max_imdb_score": {"$max": "$imdb_score"}, "movie": {"$first": "$title"}}}  # Encontrar la película con la puntuación de IMDb más alta
]

# Ejecutar la consulta de agregación
result = list(mycoll.aggregate(pipeline))

# Imprimir el resultado
if result:
    print("Película con la puntuación de IMDb más alta:")
    print("Título:", result[0]["movie"])
    print("Puntuación de IMDb:", result[0]["max_imdb_score"])
else:
    print("No se encontraron películas.")

