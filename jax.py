# The full classification list based on the provided food items needs to be converted to the new format with "grupo" and "subgrupo".
# Creating a new dictionary format with keys as "grupo" and "subgrupo"

food_equivalence_classification_full_json = {
    "Leche Liconsa": "Lácteos",
    "Otra leche opción A": "Lácteos",
    "Otra leche opción B": "Lácteos",
    "Otra leche opción C": "Lácteos",
    "Otra Leche A": "Lácteos",
    "Otra Leche B": "Lácteos",
    "Otra Leche C": "Lácteos",
    "Leche materna": "Lácteos",
    "Leche preparada de sabor (chocolate u otro sabor)": "Lácteos",
    "Yogur de vaso: a) Entero natural": "Lácteos",
    "Yogur de vaso: b) Entero con frutas": "Lácteos",
    "Yogur de vaso: c) Bajo en grasa o light natural o con fruta": "Lácteos",
    "Yogur para beber: a) Entero natural": "Lácteos",
    "Yogur para beber: b) Entero con fruta": "Lácteos",
    "Yogur para beber: c) Bajo en grasa o light natural o con fruta": "Lácteos",
    "Danonino o similar": "Lácteos",
    "Yakult o similares": "Lácteos",
    "Plátano": "Frutas",
    "Naranja o mandarina": "Frutas",
    "Manzana o pera": "Frutas",
    "Melón o sandía": "Frutas",
    "Guayaba": "Frutas",
    "Mango": "Frutas",
    "Papaya": "Frutas",
    "Piña": "Frutas",
    "Toronja": "Frutas",
    "Fresa": "Frutas",
    "Uvas": "Frutas",
    "Durazno/melocotón": "Frutas",
    "Frutas en almíbar": "Frutas",
    "Frutas cristalizadas o secas": "Frutas",
    "Jícama": "Verduras",
    "Jitomate": "Verduras",
    "Hojas Verdes (acelgas espinacas quelites)": "Verduras",
    "Chayote": "Verduras",
    "Zanahoria": "Verduras",
    "Calabacita": "Verduras",
    "Brócoli o coliflor": "Verduras",
    "Col": "Verduras",
    "Ejotes": "Verduras",
    "Elote": "Verduras",
    "Lechuga": "Verduras",
    "Nopales": "Verduras",
    "Pepino": "Verduras",
    "Chile poblano": "Verduras",
    "Cebolla": "Verduras",
    "Verduras envasadas como chícharo zanahoria champiñones ejotes": "Verduras",
    "Arroz guisado": "Cereales y Tubérculos",
    "Avena en hojuelas amaranto natural o tostado": "Cereales y Tubérculos",
    "Pan blanco": "Cereales y Tubérculos",
    "Pan integral": "Cereales y Tubérculos",
    "Pan dulce (excepto donas y churros)": "Cereales y Tubérculos",
    "Donas y churros de panadería": "Cereales y Tubérculos",
    "Galletas integrales": "Cereales y Tubérculos",
    "Galletas saladas": "Cereales y Tubérculos",
    "Papas a) Cocida": "Cereales y Tubérculos",
    "Papas b) Frita": "Cereales y Tubérculos",
    "Torta o sándwich con pan blanco": "Cereales y Tubérculos",
    "Torta o sándwich con pan integral": "Cereales y Tubérculos",
    "Cereal a) Chocolate": "Cereales y Tubérculos",
    "Cereal b) Light/cuidado de la figura": "Cereales y Tubérculos",
    "Cereal c) Hojuela endulzada": "Cereales y Tubérculos",
    "Cereal d) Básico": "Cereales y Tubérculos",
    "Cereal e) Variedades": "Cereales y Tubérculos",
    "Cereal f) Sabor a frutas": "Cereales y Tubérculos",
    "Cereal g) Fibra": "Cereales y Tubérculos",
    "Cereal h) Especialidades": "Cereales y Tubérculos",
    "Cereal i) Multi ingredientes": "Cereales y Tubérculos",
    "Tamal (todos tipos)": "Cereales y Tubérculos",
    "Sopa de pasta": "Cereales y Tubérculos",
    "Frijoles preparados en casa: a) De la olla": "Leguminosas",
    "Frijoles preparados en casa: b) Refritos": "Leguminosas",
    "Lenteja garbanzo haba amarilla o alubia": "Leguminosas",
    "Queso panela o fresco o cottage": "Alimentos de origen animal",
    "Quesos madurados (chihuahua manchego gouda etc.)": "Alimentos de origen animal",
    "Carne de puerco": "Alimentos de origen animal",
    "Carne de res": "Alimentos de origen animal",
    "Carne de res seca (machaca)": "Alimentos de origen animal",
    "Longaniza o chorizo": "Alimentos de origen animal",
    "Salchicha de puerco pavo o combinado jamón": "Alimentos de origen animal",
    "Pollo a) Pierna muslo o pechuga": "Alimentos de origen animal",
    "Pollo b) Ala patas": "Alimentos de origen animal",
    "Pollo c) Higadito o molleja": "Alimentos de origen animal",
    "Huevo a) Tibio o cocido": "Alimentos de origen animal",
    "Huevo b) Frito estrellado o revuelto": "Alimentos de origen animal",
    "Pescado fresco": "Alimentos de origen animal",
    "Pescado seco (charalitos bacalao)": "Alimentos de origen animal",
    "Atún y sardina (en tomate agua o aceite)": "Alimentos de origen animal",
    "Algún marisco (camarón ostiones etc.)": "Alimentos de origen animal",
    "Aguacate": "Aceites y Grasas",
    "Margarina": "Aceites y Grasas",
    "Mantequilla": "Aceites y Grasas",
    "Mayonesa": "Aceites y Grasas",
    "Manteca vegetal": "Aceites y Grasas",
    "Manteca animal (cerdo o pollo)": "Aceites y Grasas",
    "Azúcar agregada a la leche": "Azúcares",
    "Refresco Normal": "Azúcares",
    "Refresco Dieta": "Azúcares",
    "Café con azúcar": "Azúcares",
    "Jugos naturales sin azúcar": "Azúcares",
    "Jugos naturales con azúcar": "Azúcares",
    "Aguas de fruta natural con azúcar": "Azúcares",
    "Chocolate": "Azúcares",
    "Dulces (caramelos paletas)": "Azúcares",
    "Gelatina flan": "Azúcares",
    "Pastel o pay": "Azúcares",
    "Helado nieves y paletas de agua": "Azúcares",
    "Helado y paletas de leche": "Azúcares",
    "Néctares con azúcar": "Azúcares",
    "Barras de cereal": "Azúcares",
    "Frituras": "Misceláneos",
    "Pastelillos industrializados": "Misceláneos",
    "Galletas dulces": "Misceláneos",
    "Paletas de malvavisco": "Misceláneos",
    "Sopas instantáneas": "Misceláneos",
    "Salsas y aderezos (cátsup)": "Misceláneos",
    "Salsas de soya o inglesa": "Misceláneos",
    "Bebidas alcohólicas": "Misceláneos",
    "Agua sola": "Misceláneos",
    "Caldo de pollo": "Misceláneos",
    "Sopa con verduras": "Misceláneos",
    "Limón": "Misceláneos",
    "Sal": "Misceláneos",
    "Salsas picante": "Misceláneos",
    "Hamburguesa" : "",
    "Pizza" : "",
    "Hot dog" : "",
    "Carne de puerco" : "",
    "Carne de res" : "",
    "Carne de res seca (machaca)" : "",
    "Longaniza o chorizo" : "",
    "Salchicha de puerco pavo o combinado jamón" : "",
    "Pollo a) Pierna muslo o pechuga" : "",
    "Pollo b) Ala patas" : "",
    "Pollo c) Higadito o molleja" : "",
    "Huevo a) Tibio o cocido" : "",
    "Huevo b) Frito estrellado o revuelto" : "",
    "Pescado fresco" : "",
    "Pescado seco (charalitos bacalao)" : "",
    "Atún y sardina (en tomate agua o aceite)" : "",
    "Algún marisco (camarón ostiones etc.)" : "",
    "Frijoles preparados en casa: a) De la olla" : "",
    "Frijoles preparados en casa: b) Refritos" : "",
    "Lenteja garbanzo haba amarilla o alubia" : ""
}

# Assuming we can generate generic subgroups based on a simple heuristic (e.g., splitting by main category)
for food in food_equivalence_classification_full_json.keys():
    grupo = food_equivalence_classification_full_json[food]
    # Example heuristic for "subgrupo": use the first word of the food item or its type
    if "leche" in food.lower():
        subgrupo = "Leche"
    elif "yogur" in food.lower():
        subgrupo = "Yogur"
    elif "queso" in food.lower():
        subgrupo = "Queso"
    elif "cereal" in food.lower():
        subgrupo = "Cereal"
    elif "pollo" in food.lower():
        subgrupo = "Pollo"
    elif "carne" in food.lower():
        subgrupo = "Carne"
    elif "fruta" in grupo.lower():
        subgrupo = "Frutas"
    elif "verdura" in grupo.lower():
        subgrupo = "Verduras"
    elif "pescado" in food.lower():
        subgrupo = "Pescado"
    elif "pan" in food.lower():
        subgrupo = "Pan"
    else:
        subgrupo = "General"

    # Adding the new structure to the dictionary
    food_equivalence_classification_full_json[food] = {
        "grupo": grupo,
        "subgrupo": subgrupo
    }

# Convert the dictionary to a json file
import json
file_path_json = "food_equivalence_classification_full_with_subgroup.json"
with open(file_path_json, 'w', encoding='utf-8') as json_file:
    json.dump(food_equivalence_classification_full_json, json_file, ensure_ascii=False, indent=4)

file_path_json
