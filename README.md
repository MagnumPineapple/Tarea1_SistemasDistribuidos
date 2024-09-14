Tarea 1 - Sistemas Distribuidos (02-2024)

Repositorio de Tarea N°1 de Sistemas Distribuidos, en donde se incluyen los códigos para al implementación del sistema que se pide.

Pasos para implementar el sistema.

1. Crear el sistema de caché (Redis)
```bash
sudo docker run --name redis-server -p 6379:6379 -d redis
sudo docker ps
redis-cli
```

2. Crear las particiones de Redis
```bash
for port in {6381..6388}; do sudo docker run -d --name redis-$port -p $port:6379 redis; done
sudo docker ps
```

3. Configuración de políticas de remoción para cada partición (LRU y LFU)
```bash
redis-cli 6381 CONFIG SET maxmemory-policy allkeys-lru
redis-cli 6381 CONFIG SET maxmemory-policy allkeys-lfu
redis-cli 6381 CONFIG SET maxmemory 100mb
```
Se debe repetir el mismo procedmiento anterior (paso 3) para todas las particiones (aparte del puerto 6381)

Link del video: https://drive.google.com/file/d/1X5YFJQwpkY9LyNNJaTe6ojpblku-VupK/view?usp=sharing
