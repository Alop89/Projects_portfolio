import os 
import time 
import logging
from dotenv import load_dotenv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Cargar variables de entorno
load_dotenv()
WATCH_FOLDER = os.getenv("WATCH_FOLDER", "./erp_inbox")

# Configuración de archivo log
logging.basicConfig(
    filename = "./logs/core_loop.log", 
    level = logging.INFO, 
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

# Manejador de eventos 
class ERPDataHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return
        logging.info(f"Subcarpeta detectada: {event.src_path}; se aborta el proceso")
        
        filepath = event.src_path
        filename = os.path.basename(filepath)

        # Validar reporte en csv 
        if filename.endswith(".csv") | filename.endswith(".xlsx"):
            print(f"Nuevo reporte detectado: {filename}")
            logging.info(f"Archivo detectado: {filename}, comienza proceso ETL")

            self.process_file(filepath)

    def process_file(self, filepath):
        print(f"Procesando archivo a base de datos: {filepath}")
        logging.info(f"Procesando archivo: {filepath}")
        time.sleep(2)
        print(f"Simulación completa para {filepath}")

def start_watcher():
    if not os.path.exists(WATCH_FOLDER):
        os.mkdir(WATCH_FOLDER)
        print("Carpeta no detectada..... carpeta creada")
        logging.info("Carpeta no detectada..... carpeta creada")
    
    event_handler = ERPDataHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()
    print(f"Monitoreando carpeta: {WATCH_FOLDER}")
    logging.info(f"Monitoreando carpeta: {WATCH_FOLDER}")

    print("Arrastra archivo nuevo a carpeta erp")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Monitoreo detenido por el usuario")
        logging.info("Monitoreo detenido por el usuario")
    observer.join()

if __name__ == "__main__":
    start_watcher()
            


