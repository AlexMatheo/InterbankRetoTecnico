import csv
from decimal import Decimal


class TransactionProcessor:

    # Clase para procesar transacciones financieras desde un archivo CSV.

    def __init__(self, file_path):
        
        # Inicializa el procesador con la ruta al archivo CSV.
        # Args:
        #   file_path (str): Ruta al archivo CSV que contiene las transacciones.

        self.file_path = file_path
        self.transactions = []
        self.balance = Decimal('0.00')
        self.credit_count = 0
        self.debit_count = 0
        self.max_transaction = None
        # self.min_transaction = None

    def load_transactions(self):
        
        # Carga las transacciones desde el archivo CSV.
        # Returns:
        #       bool: True si la carga fue exitosa, False en caso contrario.

        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    # Convertir el monto a Decimal para evitar problemas de precisión
                    transaction = {
                        'id': int(row['id']),
                        'tipo': row['tipo'],
                        'monto': Decimal(row['monto'])
                    }
                    self.transactions.append(transaction)
            return True
        except Exception as e:
            print(f"Error al cargar las transacciones: {e}")
            return False

    def process_transactions(self):
        
        # Procesa las transacciones cargadas para calcular el balance final,
        # contar por tipo y encontrar la de mayor monto.

        if not self.transactions:
            print("No hay transacciones para procesar.")
            return

        for transaction in self.transactions:
            # Actualizar el balance según el tipo de transacción
            if transaction['tipo'] == 'Crédito':
                self.balance += transaction['monto']
                self.credit_count += 1
            elif transaction['tipo'] == 'Débito':
                self.balance -= transaction['monto']
                self.debit_count += 1

            # Actualizar la transacción de mayor monto si corresponde
            if not self.max_transaction or transaction['monto'] > self.max_transaction['monto']:
                self.max_transaction = transaction
                
            # Actualizar la transacción de menor monto si corresponde
            # if not self.min_transaction or transaction['monto'] < self.min_transaction['monto']:
                # self.min_transaction = transaction

    def generate_report(self):
        
        # Genera un reporte con el balance final, la transacción de mayor monto
        # y el conteo de transacciones por tipo.
        # Returns:
        # str: Reporte formateado para mostrar en la terminal.

        report = "\nReporte de Transacciones\n"
        report += "---------------------------------------------\n"
        report += f"Balance Final: {self.balance:.2f}\n"
        
        if self.max_transaction:
            report += f"Transacción de Mayor Monto: ID {self.max_transaction['id']} - {self.max_transaction['monto']:.2f}\n"
            
        # if self.min_transaction:
            # report += f"Transacción de menor Monto: ID {self.min_transaction['id']} - {self.min_transaction['monto']:.2f}\n"
        
        else:
            report += "No hay transacciones para reportar.\n"
            
        report += f"Conteo de Transacciones: Crédito: {self.credit_count} Débito: {self.debit_count} \n"
        
        return report