# Simulador QA de Plataforma POS + ATM

## 🎯 Objetivo
Simular una plataforma de transacciones financieras (POS y ATM) con autenticación de tarjetas, registro de transacciones, interfaz de usuario, APIs REST, base de datos PostgreSQL, y pruebas QA completas (manuales, automatizadas, rendimiento).

## 🧱 Arquitectura
- **Frontend:** SPA (React o Vue)
- **Backend:** FastAPI (Python) o Express (Node.js)
- **Base de datos:** PostgreSQL
- **Mensajería (opcional):** RabbitMQ o Kafka
- **Infraestructura:** Docker, GitHub Actions
- **Testing:** Gherkin (BDD), Cypress/Playwright, pytest, JMeter/Locust

## 📁 Estructura inicial
/backend  
/frontend  
/db  
/tests  
/docs  

## 🚀 Ejecución del servidor
Levantar el backend con:
uvicorn backend.main:app --reload

Abrir en navegador: http://127.0.0.1:8000/transactions

## 🧪 Pruebas QA
Ejecutar pruebas automatizadas con:
pytest -v

## 📡 Endpoints disponibles
- GET /transactions → devuelve lista de transacciones simuladas.

## 🗺️ Roadmap

### Fase 1 (Actual)
- Endpoint `/transactions` con pruebas unitarias en pytest.
- Documentación inicial en README.
- Configuración básica de entorno y dependencias.

### Fase 2 (Próxima)
- Autenticación de usuarios y tarjetas.
- Base de datos PostgreSQL para persistencia de transacciones.
- Dockerización del backend para despliegue reproducible.

### Fase 3
- Frontend SPA (React/Vue) para operadores.
- Integración con CI/CD (GitHub Actions).
- Pruebas E2E con Cypress/Playwright.

### Fase 4
- Pruebas de rendimiento con JMeter/Locust.
- Mensajería con RabbitMQ/Kafka para eventos de transacciones.
- Documentación BDD con Gherkin.

### Fase 5 (Escalamiento futuro)
- Monitoreo y logging centralizado.
- Integración con servicios externos (ej. pasarelas de pago simuladas).
- Optimización de arquitectura para alta concurrencia.


## 📌 Estado
Este proyecto está en construcción como parte de un portafolio QA técnico con enfoque BDD y automatización.
