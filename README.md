# 🧠 Building a Quiz API with Django REST Framework

> Proyecto grupal - Chiribaya 11 - Semana 7  

---

## 📖 Explicación del Proyecto

En este trabajo fuimos construyendo paso a paso una **API de Quiz** usando **Django REST Framework**.  
Hasta el momento hemos logrado:  

- Crear la estructura inicial del proyecto en Django.  
- Configurar los `settings.py` para trabajar con **REST Framework**.  
- Implementar el modelo `Quiz` con sus campos principales.  
- Definir los **serializers** para manejar la conversión de datos.  
- Crear las **vistas (views)** y **endpoints** para realizar las operaciones CRUD.  
- Configurar las **URLs** para exponer los endpoints en `/api/v1/`.  
- Ejecutar migraciones y comprobar el funcionamiento del servidor con las pruebas iniciales.  

En resumen, ya tenemos la **base del CRUD de Quizzes** funcionando en nuestra API. 🚀

---

## 👥 Integrantes del Grupo

- **Ailyn Medina**  
- **Toledo La Fuente Luis**  
- **Moya Condori Maria Fernanda**  

---

# 📌 PRIMERA PARTE: Quiz CRUD

### 🔹 Test Part 1
```bash
# View API root
curl http://127.0.0.1:8000/api/v1/

# Create quiz
curl -X POST http://127.0.0.1:8000/api/v1/quizzes/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Python Basics", "description": "Test your Python knowledge"}'

# List quizzes
curl http://127.0.0.1:8000/api/v1/quizzes/

# Get quiz detail
curl http://127.0.0.1:8000/api/v1/quizzes/1/

# Update quiz
curl -X PUT http://127.0.0.1:8000/api/v1/quizzes/1/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Advanced Python", "description": "Master Python"}'

# Delete quiz
curl -X DELETE http://127.0.0.1:8000/api/v1/quizzes/1/
```
---

# Medina Mallqui Ailyn:
  ### Create quiz 
  <img width="400" alt="image" src="https://github.com/user-attachments/assets/687ea864-a9b2-46e5-805d-abca607e9467" />
  
 ### List quizzes
 <img width="400" alt="image" src="https://github.com/user-attachments/assets/fba7e805-7d4a-4eb8-b90b-f8af343bc057" />
 
### Get quiz detail
<img width="400" alt="image" src="https://github.com/user-attachments/assets/77a447e7-b0d3-4d21-a375-106b657bf851" />

### Update quiz
<img width="400" alt="image" src="https://github.com/user-attachments/assets/f8d11005-787e-45ce-98ef-01c1eb32508d" />

### Delete quiz
<img width="400" alt="image" src="https://github.com/user-attachments/assets/cc5bf162-3643-472c-a8f8-c2e20089a014" />

--- 
# Toledo La Fuente Luis:

 ### Create quiz 
 <img width="400" alt="image" src="https://github.com/user-attachments/assets/fc0e7106-5f1d-4d11-924c-1d26a10adce9" />

 ### List quizzes
<img width="400" alt="image" src="https://github.com/user-attachments/assets/d81e60b5-44b7-4c0f-b34f-129dac23836c" />

### Get quiz detail
<img width="400" alt="image" src="https://github.com/user-attachments/assets/50c64c53-00a0-4be2-82fa-0fb012023525" />

### Update quiz
<img width="400" alt="image" src="https://github.com/user-attachments/assets/ad8f46d5-1e7b-4ff4-9511-878436f74e89" />

### Delete quiz
<img width="400" alt="image" src="https://github.com/user-attachments/assets/2a1835ac-d90c-4554-873f-84150e80ed26" />

--- 

# Moya Condori Maria Fernanda 
 ### Create quiz 
<img width="400" alt="image" src="https://github.com/user-attachments/assets/4975febf-c9fa-4446-98b8-e66cfde76f78" />

 ### List quizzes
 <img width="400" alt="image" src="https://github.com/user-attachments/assets/6497e47a-c04e-4b55-8148-79e4a89f7e2b" />

### Get quiz detail
<img width="400" alt="image" src="https://github.com/user-attachments/assets/baa9e6b3-c46f-4ede-8267-4b827ba34092" />

### Update quiz
<img width="400" alt="image" src="https://github.com/user-attachments/assets/aeb4bf63-47f2-4ec3-9cf8-9960ccd2650f" />

### Delete quiz
<img width="400" alt="image" src="https://github.com/user-attachments/assets/27c5e65d-650d-496f-96ea-1b26d2d0026a" />


# 📌 SEGUNDA PARTE: Quiz CRUD
# Medina Mallqui Ailyn:
  ### Create quiz 
<img width="580" height="147" alt="image" src="https://github.com/user-attachments/assets/742e7523-c2e7-41ab-a54b-4051c31d51bb" />
<img width="416" height="207" alt="image" src="https://github.com/user-attachments/assets/64c6fdcc-1539-4735-8994-2aa7522ab5a0" />

 ### Create question
<img width="429" height="106" alt="image" src="https://github.com/user-attachments/assets/78300491-351e-4580-ac6a-150b330b67b8" />
<img width="412" height="250" alt="image" src="https://github.com/user-attachments/assets/30b5dae1-fad1-40d0-9fff-299cc4f3ea51" />

### Create correct choice
<img width="423" height="112" alt="image" src="https://github.com/user-attachments/assets/ff1704f4-11fa-4d3f-a112-f24138c7077e" />

### Create incorrect choice
<img width="458" height="92" alt="image" src="https://github.com/user-attachments/assets/802d3820-36d0-4abf-9c7a-32e85da558be" />

###  List all questions
<img width="427" height="263" alt="image" src="https://github.com/user-attachments/assets/56c4fd5b-6417-4e6f-ab20-42d90875257e" />

###  List all choices
<img width="453" height="389" alt="image" src="https://github.com/user-attachments/assets/7e41943e-ffd6-42c4-ab41-fa0c0706b338" />


--- 
# Toledo La Fuente Luis:
### Create quiz 


### Create question


### Create correct choice


### Create incorrect choice


###  List all questions


###  List all choices


--- 

# Moya Condori Maria Fernanda 
### Create quiz 


### Create question


### Create correct choice


### Create incorrect choice


###  List all questions


###  List all choices
