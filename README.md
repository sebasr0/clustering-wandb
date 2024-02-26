\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{hyperref}
\usepackage{listings}

\title{Clustering de KMeans en el Conjunto de Datos Iris con Registro en WandB y GitHub Actions}
\author{}
\date{}

\begin{document}

\maketitle

Este proyecto demuestra cómo automatizar el entrenamiento de un modelo de clustering KMeans en el conjunto de datos Iris y registrar los detalles del experimento utilizando Weights \& Biases (WandB), todo esto integrado con GitHub Actions para una ejecución automática.

\section*{Prerrequisitos}

Asegúrate de tener configurado tu entorno de GitHub y WandB con las siguientes consideraciones:

\begin{itemize}
  \item Una cuenta de GitHub.
  \item Una cuenta en WandB y una API KEY generada.
  \item Configurar la API KEY de WandB como un secreto en GitHub (\texttt{WANDB\_API\_KEY}).
\end{itemize}

\section*{Configuración del Flujo de Trabajo de GitHub Actions}

El flujo de trabajo definido en \texttt{.github/workflows} se activa con cada push al archivo \texttt{source/load\_n\_classify.py} en la rama \texttt{master}. El flujo incluye los siguientes pasos:

\begin{enumerate}
  \item \textbf{Checkout del Código}: Utiliza \texttt{actions/checkout@v3} para obtener el código más reciente.
  \item \textbf{Configuración de Python}: Establece el entorno Python usando \texttt{actions/setup-python@v4}, específicamente la versión \texttt{3.9}.
  \item \textbf{Instalación de Dependencias}: Instala todas las dependencias necesarias definidas en \texttt{requirements.txt}.
  \item \textbf{Login en WandB}: Realiza el login en WandB utilizando la API KEY almacenada en los secretos de GitHub.
  \item \textbf{Ejecución del Script}: Ejecuta \texttt{load\_n\_classify.py} pasando como argumento \texttt{--IdExecution} el número de ejecución (\texttt{run\_number}) de GitHub Actions.
\end{enumerate}

\section*{Uso}

Para utilizar este flujo de trabajo:

\begin{enumerate}
  \item Realiza cambios en el script \texttt{source/load\_n\_classify.py} según sea necesario.
  \item Haz push de tus cambios al archivo en la rama \texttt{master}.
  \item GitHub Actions automáticamente ejecutará el flujo de trabajo, entrenando el modelo de clustering y registrando el experimento en WandB.
\end{enumerate}

\section*{Salidas}

\begin{itemize}
  \item El script registra los resultados del entrenamiento y las visualizaciones en tu proyecto de WandB.
  \item Puedes monitorear la ejecución y el resultado del flujo de trabajo en la pestaña \texttt{Actions} de tu repositorio GitHub.
\end{itemize}

\section*{Contribuciones}

Siéntete libre de contribuir al proyecto mediante pull requests o abriendo issues para discutir mejoras o cambios.

\section*{Licencia}

Este proyecto se distribuye bajo la Licencia MIT, lo que permite su uso y modificación para proyectos personales y comerciales.

\end{document}
