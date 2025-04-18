import os
import sys
from transaction_processor import TransactionProcessor

def main():

    # Función principal del programa.
    # Lee un archivo de transacciones, procesa los datos y muestra un reporte.

    # Verificar argumentos de línea de comandos
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Usar archivo predeterminado si no se proporciona uno
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'data.csv')
    
    # Verificar que el archivo existe
    if not os.path.exists(file_path):
        print(f"Error: El archivo {file_path} no existe.")
        return
    
    # Crear el procesador y cargar las transacciones
    processor = TransactionProcessor(file_path)
    if processor.load_transactions():
        processor.process_transactions()
        report = processor.generate_report()
        print(report)
    else:
        print("No se pudo procesar el archivo de transacciones.")


if __name__ == "__main__":
    main()