<p align="center">
  <img src="static/Assets/Image/portada.jpeg" alt="Kriptom" width="auto">
</p>

# Coffee Organic Life ☕

**Coffee Organic Life** es una plataforma web desarrollada en Django diseñada para la venta y promoción de café orgánico peruano de alta calidad. El proyecto combina una tienda en línea funcional con secciones informativas y de contacto, ofreciendo una experiencia moderna y responsiva.

## 🚀 Características Principales

### 🛒 Tienda Virtual (APPTienda)
- **Catálogo de Productos:** Visualización de productos con tarjetas detalladas (precio, stock, tipo de molido, grano).
- **Sistema de Búsqueda:** Búsqueda en tiempo real por título, contenido u origen del café.
- **Filtros Avanzados:**
  - **Rango de Precio:** Slider y campos numéricos para filtrar por presupuesto.
  - **Categorías:** Filtros por tipo de grano (Tostado) y tipo de molido (Fino, Medio, Grueso).
- **Indicadores Visuales:** Badges para productos destacados y estado de stock (En Stock / Agotado).

### 📞 Contacto (APPContacto)
- **Formulario de Contacto:** Envío de mensajes directo.
- **Ubicación Interactiva:** Integración con Google Maps API para mostrar la ubicación física de la tienda.
- **Redes Sociales:** Enlaces directos a plataformas (WhatsApp, Facebook, Instagram, etc.).

### 🏠 Home & Blog (APPHome / APPBlog)
- **Landing Page:** Página de inicio atractiva con información sobre la marca.
- **Grid Responsivo:** Diseño adaptable a móviles, tablets y escritorio.

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3, Django 2.2+
- **Frontend:** HTML5, CSS3 (Diseño personalizado + Grid System), JavaScript.
- **Base de Datos:** SQLite (por defecto).
- **Integraciones:** Google Maps API.

## ⚙️ Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. **Clonar el repositorio** (si aplica) o descargar el código fuente.

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv env
   # Windows
   .\env\Scripts\activate
   # Linux/Mac
   source env/bin/activate
   ```

3. **Instalar dependencias:**
   Asegúrate de tener instaladas las librerías necesarias (principalmente Django y Pillow para el manejo de imágenes).
   ```bash
   pip install django pillow
   ```

4. **Realizar migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un superusuario (opcional):**
   Para acceder al panel de administración de Django.
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor:**
   ```bash
   python manage.py runserver
   ```

7. **Ver el proyecto:**
   Abre tu navegador y visita `http://127.0.0.1:8000/`

## 📂 Estructura del Proyecto

- `root/`
  - `APPHome/`: Lógica de la página de inicio y base templates.
  - `APPTienda/`: Lógica de la tienda, modelos de productos y filtros.
  - `APPContacto/`: Vista de contacto y formularios.
  - `APPBlog/`: Sistema de blog.
  - `manage.py`: Script de gestión de Django.
  - `media/`: Archivos multimedia (imágenes de productos).

## 👤 Autor

**Isaias Cesar Quintana Errazabal**
Desarrollador Full Stack Jr. en formación.
