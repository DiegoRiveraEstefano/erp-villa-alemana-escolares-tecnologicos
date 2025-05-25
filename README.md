# ERP Villa Alemana Escolares Tecnológicos

Sistema de gestión integral para PYME de artículos escolares y tecnológicos.  
![Logo Conceptual](https://via.placeholder.com/100x30/2A4F7A/FFFFFF?text=ERP+Villa+Alemana)  

## 🛠️ Herramientas Principales
- **Frontend**: PicoCSS (Enfoque minimalista)
- **Backend**: Python 3.10 + Django 4.2
- **Base de Datos**: PostgreSQL
- **Auditoría**: django-auditlog
- **Admin Moderno**: django-jet-reboot
- **Gestión de Archivos**: whitenoise

**Licencia**: [MIT](LICENSE)

---

## 🚀 Configuración Inicial

### Requisitos
- Python 3.10+
- PostgreSQL 14+
- Virtualenv

### Instalación
1. Clonar repositorio:
   ```bash
   git clone https://github.com/tu-usuario/erp-villa-alemana.git
   cd erp-villa-alemana
   ```

2. Crear entorno virtual:
```bash
virtualenv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```
4. Configurar variables de entorno en .env:
```ini
SECRET_KEY=tu_clave_secreta
DATABASE_URL=postgres://user:password@localhost:5432/erp_db
DEBUG=True
```   
## Comandos Básicos

### Ejecutar Servidor de Desarrollo
```bash
python manage.py runserver
```
### Crear Superusuario
```bash
python manage.py createsuperuser
```
### Tipado Estático (mypy)
```bash
mypy erp_villa_alemana_escolares_tecnologicos
```
### Ejecutar Tests
```bash
pytest --cov=.
```

---

## 🔐 Modelo de Permisos

### Roles Predefinidos

|Rol|Slug|Descripción|
|---|---|---|
|Administrador|`admin`|Acceso total al sistema|
|Bodeguero|`warehouse`|Gestión de inventario|
|Ventas|`sales`|Registro de clientes y transacciones|
|Soporte|`support`|Edición limitada de datos de clientes|
|Contabilidad|`finance`|Acceso de solo lectura a datos financieros|

---

## 🤝 Contribuir

1. Hacer fork del proyecto
    
2. Crear rama: `git checkout -b feature/nueva-funcionalidad`
    
3. Commit: `git commit -m 'Agrega algo increíble'`
    
4. Push: `git push origin feature/nueva-funcionalidad`
    
5. Abrir Pull Request

---

## 📬 Soporte

¿Problemas? Abre un [issue](https://github.com/tu-usuario/erp-villa-alemana/issues)