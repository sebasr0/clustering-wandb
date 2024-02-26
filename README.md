# Clustering de KMeans en el Conjunto de Datos Iris con Registro en WandB y GitHub Actions

Este proyecto demuestra cómo automatizar el entrenamiento de un modelo de clustering KMeans en el conjunto de datos Iris y registrar los detalles del experimento utilizando Weights & Biases (WandB), todo esto integrado con GitHub Actions para una ejecución automática.

## Prerrequisitos

Asegúrate de tener configurado tu entorno de GitHub y WandB con las siguientes consideraciones:

- Una cuenta de GitHub.
- Una cuenta en WandB y una API KEY generada.
- Configurar la API KEY de WandB como un secreto en GitHub (`WANDB_API_KEY`).

## Configuración del Flujo de Trabajo de GitHub Actions

El flujo de trabajo definido en `.github/workflows` se activa con cada push al archivo `source/load_n_classify.py` en la rama `master`. El flujo incluye los siguientes pasos:

1. **Checkout del Código**: Utiliza `actions/checkout@v3` para obtener el código más reciente.
2. **Configuración de Python**: Establece el entorno Python usando `actions/setup-python@v4`, específicamente la versión `3.9`.
3. **Instalación de Dependencias**: Instala todas las dependencias necesarias definidas en `requirements.txt`.
4. **Login en WandB**: Realiza el login en WandB utilizando la API KEY almacenada en los secretos de GitHub.
5. **Ejecución del Script**: Ejecuta `load_n_classify.py` pasando como argumento `--IdExecution` el número de ejecución (`run_number`) de GitHub Actions.

## Uso

Para utilizar este flujo de trabajo:

1. Realiza cambios en el script `source/load_n_classify.py` según sea necesario.
2. Haz push de tus cambios al archivo en la rama `master`.
3. GitHub Actions automáticamente ejecutará el flujo de trabajo, entrenando el modelo de clustering y registrando el experimento en WandB.

## Salidas

- El script registra los resultados del entrenamiento y las visualizaciones en tu proyecto de WandB.
- Puedes monitorear la ejecución y el resultado del flujo de trabajo en la pestaña `Actions` de tu repositorio GitHub.
