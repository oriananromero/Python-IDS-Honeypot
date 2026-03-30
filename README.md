# 🛡️ Multi-Port IDS & Honeypot en Python

## 📖 Descripción del Proyecto
Este proyecto es un **Sistema de Detección de Intrusiones (IDS)** basado en un "Honeypot" de baja interacción. Utiliza **programación concurrente (multithreading)** para monitorizar simultáneamente varios puertos críticos y alertar sobre intentos de conexión sospechosos en tiempo real.

Desarrollado como parte de un laboratorio de ciberseguridad defensiva para identificar fases de reconocimiento en una red local.

## 🚀 Características Técnicas
- **Multithreading:** Implementación de la librería `threading` para gestionar múltiples sockets de escucha sin bloquear el flujo principal.
- **Detección de Conexiones:** Identificación de IP de origen, puerto objetivo y marca de tiempo (*timestamp*) exacta.
- **Análisis de Red:** Capacidad de detectar escaneos de tipo **TCP Connect Scan (`-sT`)**.
- **Entorno de Pruebas:** Validado mediante ataques dirigidos desde una máquina **Metasploitable2** hacia un nodo **Ubuntu**.

## 🛠️ Puertos Monitorizados (Cebos)
Se han seleccionado puertos comúnmente atacados para servicios críticos:
- **21 (FTP):** Transferencia de archivos insegura.
- **3306 (MySQL):** Base de datos (monitorización de intentos de acceso no autorizado y exfiltración de datos).
- **80 (HTTP):** Tráfico web no cifrado.
- **445 (SMB):** Puerto crítico para propagación de Ransomware.

## 🧠 Lecciones Aprendidas: El Desafío de Nmap
Durante el desarrollo, se identificó que el script (usando `accept()`) no detectaba los escaneos sigilosos por defecto de Nmap (**SYN Stealth Scan `-sS`**). 
* **Razón técnica:** El script requiere completar el *TCP Three-Way Handshake*. Los escaneos `-sS` envían un `RST` antes de finalizar la conexión, evitando que el socket de Python registre la conexión.
* **Solución aplicada:** Se validó el funcionamiento forzando un **TCP Connect Scan (`-sT`)**, lo que garantiza que la alerta salte al completarse el saludo de red.

## 📸 Demostración de Alertas

<img width="811" height="189" alt="vigilante_python_puertos" src="https://github.com/user-attachments/assets/6c022b3f-7ca8-46ae-8610-8be5d51309f2" />

<img width="719" height="517" alt="ataque_metasploitable" src="https://github.com/user-attachments/assets/13211b9a-8b7e-40c2-9fef-ca7248f810f5" />

<img width="907" height="233" alt="alerta_vigilante_puertos" src="https://github.com/user-attachments/assets/f815d802-3707-4945-bd0f-fa08c60f9731" />

<img width="1650" height="229" alt="alertas_rafaga_nmap" src="https://github.com/user-attachments/assets/d390fb34-92a6-4700-9074-b9704ceb9634" />

**Se puede ver el código utulizado para esta prueba en la carpeta */code* donde los textos los he cambiado al inglés.

## 💻 Ejecución
```bash
sudo python3 vigilante_pro.py


