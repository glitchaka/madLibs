#Concatenar cadena de caracteres.
#Supongamos que queremos crear una cadena que diga
# aprende a programar cin________________________.

# organizacion = "freeCodeCamp"

# print("aprende a programar con " + organizacion)
# print("Aprende a programar con {}".format(organizacion))
# print(f"Aprende a programar con {organizacion}") #f-string

#Mad Libs (Historias Cortas)
adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivosPlural = input("Sustantivo (plural): ")

madLibs = f"Programar es tan {adj}, Siempre me emociona por que me encanta {verbo1} problemas, Aprende a programar con freeCodeCamp y alcanza tus{sustantivosPlural}"

print(madLibs)

